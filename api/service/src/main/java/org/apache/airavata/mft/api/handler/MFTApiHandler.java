/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.airavata.mft.api.handler;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.google.protobuf.util.JsonFormat;
import io.grpc.Status;
import io.grpc.stub.StreamObserver;
import org.apache.airavata.mft.admin.MFTConsulClient;
import org.apache.airavata.mft.admin.SyncRPCClient;
import org.apache.airavata.mft.admin.models.AgentInfo;
import org.apache.airavata.mft.admin.models.TransferState;
import org.apache.airavata.mft.admin.models.rpc.SyncRPCRequest;
import org.apache.airavata.mft.admin.models.rpc.SyncRPCResponse;
import org.apache.airavata.mft.agent.stub.DirectoryMetadata;
import org.apache.airavata.mft.agent.stub.FileMetadata;
import org.apache.airavata.mft.api.service.*;
import org.apache.commons.lang3.tuple.Pair;
import org.dozer.DozerBeanMapper;
import org.lognet.springboot.grpc.GRpcService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.*;
import java.util.concurrent.*;

@GRpcService
public class MFTApiHandler extends MFTTransferServiceGrpc.MFTTransferServiceImplBase {

    private static final Logger logger = LoggerFactory.getLogger(MFTApiHandler.class);

    @Autowired
    private MFTConsulClient mftConsulClient;

    @Autowired
    private DozerBeanMapper dozerBeanMapper;

    private ObjectMapper jsonMapper = new ObjectMapper();

    @Autowired
    private SyncRPCClient agentRPCClient;

    @org.springframework.beans.factory.annotation.Value("${resource.service.host}")
    private String resourceServiceHost;

    @org.springframework.beans.factory.annotation.Value("${resource.service.port}")
    private int resourceServicePort;

    @org.springframework.beans.factory.annotation.Value("${secret.service.host}")
    private String secretServiceHost;

    @org.springframework.beans.factory.annotation.Value("${secret.service.port}")
    private int secretServicePort;

    @Override
    public void submitTransfer(TransferApiRequest request, StreamObserver<TransferApiResponse> responseObserver) {
        try {
            String transferId = mftConsulClient.submitTransfer(request);
            logger.info("Submitted the transfer request {}", transferId);

            mftConsulClient.saveTransferState(transferId, new TransferState()
                    .setUpdateTimeMils(System.currentTimeMillis())
                    .setState("RECEIVED").setPercentage(0)
                    .setPublisher("api")
                    .setDescription("Received transfer job " + transferId));

            responseObserver.onNext(TransferApiResponse.newBuilder().setTransferId(transferId).build());
            responseObserver.onCompleted();
        } catch (Exception e) {
            logger.error("Error in submitting transfer request", e);
            responseObserver.onError(Status.INTERNAL
                    .withDescription("Failed to submit transfer request. " + e.getMessage())
                    .asException());
        }
    }

    private class BatchTransferSubmitter implements Callable<Pair<Integer, String>> {
        private int index = 0;
        private TransferApiRequest apiRequest;

        public BatchTransferSubmitter(int index, TransferApiRequest apiRequest) {
            this.index = index;
            this.apiRequest = apiRequest;
        }

        @Override
        public Pair<Integer, String> call() throws Exception {

            String transferId = mftConsulClient.submitTransfer(apiRequest);
            logger.info("Submitted the transfer request {}", transferId);

            mftConsulClient.saveTransferState(transferId, new TransferState()
                    .setUpdateTimeMils(System.currentTimeMillis())
                    .setState("RECEIVED").setPercentage(0)
                    .setPublisher("api")
                    .setDescription("Received transfer job " + transferId));

            return Pair.of(index, transferId);
        }
    }

    @Override
    public void submitBatchTransfer(BatchTransferApiRequest request, StreamObserver<BatchTransferApiResponse> responseObserver) {
        ExecutorService executorService = Executors.newFixedThreadPool(20);

        try {
            List<TransferApiRequest> transferRequests = request.getTransferRequestsList();
            BatchTransferApiResponse.Builder responseBuilder = BatchTransferApiResponse.newBuilder();

            ExecutorCompletionService<Pair<Integer,String>> completionService = new ExecutorCompletionService<>(executorService);

            for (int index = 0; index < transferRequests.size(); index ++) {
                completionService.submit(new BatchTransferSubmitter(index, transferRequests.get(index)));
            }

            Map<Integer, String> resultMap = new HashMap<>();
            for (int index = 0; index < transferRequests.size(); index ++) {
                Future<Pair<Integer, String>> futureResult = completionService.take();
                Pair<Integer, String> result = futureResult.get();
                resultMap.put(result.getLeft(), result.getRight());
            }

            for (int index = 0; index < transferRequests.size(); index ++) {
                responseBuilder.addTransferIds(resultMap.get(index));
            }

            responseObserver.onNext(responseBuilder.build());
            responseObserver.onCompleted();

        } catch (Exception e) {
            logger.error("Error in submitting batch transfer request", e);
            responseObserver.onError(Status.INTERNAL
                    .withDescription("Failed to submit batch transfer request. " + e.getMessage())
                    .asException());
        } finally {
            executorService.shutdown();
        }
    }

    @Override
    public void submitHttpUpload(HttpUploadApiRequest request, StreamObserver<HttpUploadApiResponse> responseObserver) {
        super.submitHttpUpload(request, responseObserver);
    }

    @Override
    public void submitHttpDownload(HttpDownloadApiRequest request, StreamObserver<HttpDownloadApiResponse> responseObserver) {
        try {
            // TODO : Automatically derive agent if the target agent is empty

            logger.info("Processing submit http download for resource path {}", request.getResourcePath());

            String targetAgent = derriveTargetAgent(request.getTargetAgent());

            SyncRPCRequest.SyncRPCRequestBuilder requestBuilder = SyncRPCRequest.SyncRPCRequestBuilder.builder()
                    .withAgentId(targetAgent)
                    .withMessageId(UUID.randomUUID().toString())
                    .withMethod("submitHttpDownload")
                    .withParameter("resourcePath", request.getResourcePath())
                    .withParameter("sourceStorageId", request.getSourceStorageId())
                    .withParameter("sourceToken", request.getSourceToken())
                    .withParameter("mftAuthorizationToken", JsonFormat.printer().print(request.getMftAuthorizationToken()));

            SyncRPCResponse rpcResponse = agentRPCClient.sendSyncRequest(requestBuilder.build());

            switch (rpcResponse.getResponseStatus()) {
                case SUCCESS:
                    String url = rpcResponse.getResponseAsStr();
                    HttpDownloadApiResponse downloadResponse = HttpDownloadApiResponse.newBuilder()
                            .setUrl(url)
                            .setTargetAgent(request.getTargetAgent()).build();
                    responseObserver.onNext(downloadResponse);
                    responseObserver.onCompleted();
                    return;
                case FAIL:
                    logger.error("Errored while processing the download request to resource path {}. Error msg : {}",
                            request.getResourcePath(), rpcResponse.getErrorAsStr());

                    responseObserver.onError(Status.INTERNAL
                            .withDescription("Errored while processing the the fetch file metadata response. Error msg : " +
                                    rpcResponse.getErrorAsStr())
                            .asException());
            }

        } catch (Exception e) {
            logger.error("Error while submitting http download request to resource path {}",
                                                request.getResourcePath() , e);
            responseObserver.onError(Status.INTERNAL
                    .withDescription("Failed to submit http download request. " + e.getMessage())
                    .asException());
        }
    }

    @Override
    public void getTransferStates(TransferStateApiRequest request, StreamObserver<TransferStateApiResponse> responseObserver) {
        try {
            List<TransferState> states = mftConsulClient.getTransferStates(request.getTransferId());
            states.forEach(st -> {
                TransferStateApiResponse s = dozerBeanMapper.map(st, TransferStateApiResponse.newBuilder().getClass()).build();
                responseObserver.onNext(s);
            });
            responseObserver.onCompleted();
        } catch (Exception e) {
            logger.error("Error in fetching transfer states", e);
            responseObserver.onError(Status.INTERNAL
                    .withDescription("Failed to retrieve transfer states. " + e.getMessage())
                    .asException());
        }
    }

    @Override
    public void getTransferState(TransferStateApiRequest request, StreamObserver<TransferStateApiResponse> responseObserver) {
        try {
            Optional<TransferState> stateOp = mftConsulClient.getTransferState(request.getTransferId());

            if (stateOp.isPresent()) {
                TransferStateApiResponse s = dozerBeanMapper.map(stateOp.get(),
                        TransferStateApiResponse.newBuilder().getClass()).build();
                responseObserver.onNext(s);
                responseObserver.onCompleted();
            } else {
                logger.error("There is no state for transfer " + request.getTransferId());
                responseObserver.onError(Status.NOT_FOUND
                        .withDescription("There is no state for transfer " + request.getTransferId())
                        .asRuntimeException());
            }
        } catch (Exception e) {
            logger.error("Error in fetching transfer state", e);
            responseObserver.onError(Status.INTERNAL
                    .withDescription("Failed to retrieve transfer state. " + e.getMessage())
                    .asException());
        }
    }

    /**
     * Fetches metadata for a specified file resource.  This has 2 modes
     * 1. Fetch the metadata of the exact file pointed in the resourceId. This assumes resourceId is an id of a file resource
     * 2. Fetch the metadata of a child directory in the parent directory. To do this, childPath should be provided explicitly
     * and resourceId is the parent resource id. Here resource id should be an id of directory resource
     */
    @Override
    public void getFileResourceMetadata(FetchResourceMetadataRequest request, StreamObserver<FileMetadataResponse> responseObserver) {

        try {

            logger.info("Calling get file resource metadata for resource path {}", request.getResourcePath());

            String targetAgent = derriveTargetAgent(request.getTargetAgentId());

            SyncRPCRequest.SyncRPCRequestBuilder requestBuilder = SyncRPCRequest.SyncRPCRequestBuilder.builder()
                    .withAgentId(targetAgent)
                    .withMessageId(UUID.randomUUID().toString())
                    .withParameter("resourcePath", request.getResourcePath())
                    .withParameter("storageId", request.getStorageId())
                    .withParameter("resourceToken", request.getResourceToken())
                    .withParameter("mftAuthorizationToken", JsonFormat.printer().print(request.getMftAuthorizationToken()));

            requestBuilder.withMethod("getFileResourceMetadata");

            SyncRPCResponse rpcResponse = agentRPCClient.sendSyncRequest(requestBuilder.build());

            switch (rpcResponse.getResponseStatus()) {
                case SUCCESS:
                    FileMetadata fileResourceMetadata = jsonMapper.readValue(rpcResponse.getResponseAsStr(), FileMetadata.class);
                    FileMetadataResponse.Builder responseBuilder = FileMetadataResponse.newBuilder();
                    dozerBeanMapper.map(fileResourceMetadata, responseBuilder);
                    responseObserver.onNext(responseBuilder.build());
                    responseObserver.onCompleted();
                    return;
                case FAIL:
                    logger.error("Errored while processing the fetch file metadata response for resource path {}. Error msg : {}",
                            request.getResourcePath(), rpcResponse.getErrorAsStr());
                    responseObserver.onError(Status.INTERNAL
                            .withDescription("Errored while processing the the fetch file metadata response. Error msg : " +
                                    rpcResponse.getErrorAsStr())
                            .asException());
            }
        } catch (Exception e) {
            logger.error("Error while fetching resource metadata for file resource " + request.getResourcePath(), e);
            responseObserver.onError(Status.INTERNAL
                    .withDescription("Failed to fetch file resource metadata. " + e.getMessage())
                    .asException());
        }
    }

    /**
     * Fetches metadata for a specified directory resource. This method assumes that the resourceId is an id of
     * a directory resource. This has 2 modes
     * 1. Fetch the metadata of the exact directory pointed in the resourceId
     * 2. Fetch the metadata of a child directory in the parent directory. To do this, childPath should be provided explicitly
     * and resourceId is the parent resource id.
     */
    @Override
    public void getDirectoryResourceMetadata(FetchResourceMetadataRequest request, StreamObserver<DirectoryMetadataResponse> responseObserver) {
        try {

            logger.info("Calling get directory metadata for resource path {}", request.getResourcePath());
            String targetAgent = derriveTargetAgent(request.getTargetAgentId());

            SyncRPCRequest.SyncRPCRequestBuilder requestBuilder = SyncRPCRequest.SyncRPCRequestBuilder.builder()
                    .withAgentId(targetAgent)
                    .withMessageId(UUID.randomUUID().toString())
                    .withParameter("resourcePath", request.getResourcePath())
                    .withParameter("storageId", request.getStorageId())
                    .withParameter("resourceToken", request.getResourceToken())
                    .withParameter("mftAuthorizationToken", JsonFormat.printer().print(request.getMftAuthorizationToken()));

            requestBuilder.withMethod("getDirectoryResourceMetadata");

            SyncRPCResponse rpcResponse = agentRPCClient.sendSyncRequest(requestBuilder.build());

            switch (rpcResponse.getResponseStatus()) {
                case SUCCESS:
                    DirectoryMetadata dirResourceMetadata = jsonMapper.readValue(rpcResponse.getResponseAsStr(), DirectoryMetadata.class);
                    DirectoryMetadataResponse.Builder responseBuilder = DirectoryMetadataResponse.newBuilder();
                    dozerBeanMapper.map(dirResourceMetadata, responseBuilder);

                    // As dozer mapper can't map collections in protobuf, do it manually for directories and files
                    for (DirectoryMetadata dm : dirResourceMetadata.getDirectoriesList()) {
                        DirectoryMetadataResponse.Builder db = DirectoryMetadataResponse.newBuilder();
                        dozerBeanMapper.map(dm, db);
                        responseBuilder.addDirectories(db);
                    }

                    for (FileMetadata fm : dirResourceMetadata.getFilesList()) {
                        FileMetadataResponse.Builder fb = FileMetadataResponse.newBuilder();
                        dozerBeanMapper.map(fm, fb);
                        responseBuilder.addFiles(fb);
                    }

                    responseObserver.onNext(responseBuilder.build());
                    responseObserver.onCompleted();
                    return;
                case FAIL:
                    logger.error("Errored while processing the fetch directory metadata response for resource path {}. Error msg : {}",
                            request.getResourcePath(), rpcResponse.getErrorAsStr());
                    responseObserver.onError(Status.INTERNAL
                            .withDescription("Errored while processing the the fetch directory metadata response. Error msg : " +
                                    rpcResponse.getErrorAsStr())
                            .asException());
            }
        } catch (Exception e) {
            logger.error("Error while fetching directory resource metadata for resource path {}", request.getResourcePath(), e);
            responseObserver.onError(Status.INTERNAL
                    .withDescription("Failed to fetch directory resource metadata. " + e.getMessage())
                    .asException());
        }
    }

    private String derriveTargetAgent(String targetAgent) throws Exception {
        if (targetAgent.isEmpty()) {
            List<String> liveAgentIds = mftConsulClient.getLiveAgentIds();
            if (liveAgentIds.isEmpty()) {
                throw new Exception("No agent is available to perform the operation");
            }
            targetAgent = liveAgentIds.get(0);
            logger.info("Using agent {} for processing the operation", targetAgent);
        } else {
            Optional<AgentInfo> agentInfo = mftConsulClient.getAgentInfo(targetAgent);
            if (agentInfo.isEmpty()) {
                throw new Exception("Target agent " + targetAgent + " is not available");
            }
        }
        return targetAgent;
    }
}
