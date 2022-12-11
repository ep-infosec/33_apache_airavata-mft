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

package org.apache.airavata.mft.transport.ftp;

import org.apache.airavata.mft.common.AuthToken;
import org.apache.airavata.mft.core.ConnectorContext;
import org.apache.airavata.mft.core.api.Connector;
import org.apache.airavata.mft.credential.stubs.ftp.FTPSecret;
import org.apache.airavata.mft.credential.stubs.ftp.FTPSecretGetRequest;
import org.apache.airavata.mft.resource.client.ResourceServiceClient;
import org.apache.airavata.mft.resource.client.ResourceServiceClientBuilder;
import org.apache.airavata.mft.resource.stubs.common.GenericResource;
import org.apache.airavata.mft.resource.stubs.common.GenericResourceGetRequest;
import org.apache.airavata.mft.resource.stubs.ftp.storage.FTPStorage;
import org.apache.airavata.mft.secret.client.SecretServiceClient;
import org.apache.airavata.mft.secret.client.SecretServiceClientBuilder;
import org.apache.commons.net.ftp.FTPClient;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.InputStream;
import java.io.OutputStream;

public class FTPReceiver implements Connector {

    private static final Logger logger = LoggerFactory.getLogger(FTPReceiver.class);

    private boolean initialized;
    private FTPClient ftpClient;

    private String resourceServiceHost;
    private int resourceServicePort;
    private String secretServiceHost;
    private int secretServicePort;

    @Override
    public void init(String resourceServiceHost, int resourceServicePort, String secretServiceHost, int secretServicePort) throws Exception {
        this.initialized = true;

        this.resourceServiceHost = resourceServiceHost;
        this.resourceServicePort = resourceServicePort;
        this.secretServiceHost = secretServiceHost;
        this.secretServicePort = secretServicePort;
    }


    @Override
    public void destroy() {
        FTPTransportUtil.disconnectFTP(ftpClient);
    }

    @Override
    public void startStream(AuthToken authToken, String resourceId, String credentialToken, ConnectorContext context) throws Exception {

        logger.info("Starting FTP receiver stream for transfer {}", context.getTransferId());

        checkInitialized();

        ResourceServiceClient resourceClient = ResourceServiceClientBuilder.buildClient(resourceServiceHost, resourceServicePort);
        GenericResource resource = resourceClient.get().getGenericResource(GenericResourceGetRequest.newBuilder()
                .setResourceId(resourceId).build());

        if (resource.getStorageCase() != GenericResource.StorageCase.FTPSTORAGE) {
            logger.error("Invalid storage type {} specified for resource {}", resource.getStorageCase(), resourceId);
            throw new Exception("Invalid storage type specified for resource " + resourceId);
        }

        FTPStorage ftpStorage = resource.getFtpStorage();

        SecretServiceClient secretClient = SecretServiceClientBuilder.buildClient(secretServiceHost, secretServicePort);
        FTPSecret ftpSecret = secretClient.ftp().getFTPSecret(FTPSecretGetRequest.newBuilder().setSecretId(credentialToken).build());

        this.ftpClient = FTPTransportUtil.getFTPClient(ftpStorage, ftpSecret);

        OutputStream streamOs = context.getStreamBuffer().getOutputStream();
        InputStream inputStream = ftpClient.retrieveFileStream(resource.getFile().getResourcePath());

        long fileSize = context.getMetadata().getResourceSize();

        byte[] buf = new byte[1024];
        while (true) {
            int bufSize;

            if (buf.length < fileSize) {
                bufSize = buf.length;
            } else {
                bufSize = (int) fileSize;
            }
            bufSize = inputStream.read(buf, 0, bufSize);

            if (bufSize < 0) {
                break;
            }

            streamOs.write(buf, 0, bufSize);
            streamOs.flush();

            fileSize -= bufSize;
            if (fileSize == 0L)
                break;
        }

        inputStream.close();
        streamOs.close();
        logger.info("Completed FTP receiver stream for transfer {}", context.getTransferId());

    }

    private void checkInitialized() {
        if (!initialized) {
            throw new IllegalStateException("FTP Receiver is not initialized");
        }
    }

    @Override
    public void startStream(AuthToken authToken, String resourceId, String childResourcePath, String credentialToken,
                            ConnectorContext context) throws Exception {
        throw new UnsupportedOperationException();
    }
}
