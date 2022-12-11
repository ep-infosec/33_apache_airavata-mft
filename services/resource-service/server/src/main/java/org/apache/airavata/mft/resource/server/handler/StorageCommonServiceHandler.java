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

package org.apache.airavata.mft.resource.server.handler;

import io.grpc.Status;
import io.grpc.stub.StreamObserver;
import org.apache.airavata.mft.resource.server.backend.ResourceBackend;
import org.apache.airavata.mft.resource.stubs.scp.storage.SCPStorageListResponse;
import org.apache.airavata.mft.resource.stubs.storage.common.StorageCommonServiceGrpc;
import org.apache.airavata.mft.resource.stubs.storage.common.StorageTypeResolveRequest;
import org.apache.airavata.mft.resource.stubs.storage.common.StorageTypeResolveResponse;
import org.lognet.springboot.grpc.GRpcService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;

@GRpcService
public class StorageCommonServiceHandler extends StorageCommonServiceGrpc.StorageCommonServiceImplBase {

    private static final Logger logger = LoggerFactory.getLogger(StorageCommonServiceHandler.class);

    @Autowired
    private ResourceBackend backend;

    @Override
    public void resolveStorageType(StorageTypeResolveRequest request, StreamObserver<StorageTypeResolveResponse> responseObserver) {
        try {
            StorageTypeResolveResponse storageTypeResolveResponse = this.backend.resolveStorageType(request);
            responseObserver.onNext(storageTypeResolveResponse);
            responseObserver.onCompleted();
        } catch (Exception e) {
            logger.error("Failed in retrieving storage type for storage id {}", request.getStorageId(), e);

            responseObserver.onError(Status.INTERNAL.withCause(e)
                    .withDescription("Failed in retrieving storage type")
                    .asRuntimeException());
        }
    }

}
