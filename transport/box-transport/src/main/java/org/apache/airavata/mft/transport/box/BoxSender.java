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

package org.apache.airavata.mft.transport.box;


import com.box.sdk.BoxAPIConnection;
import com.box.sdk.BoxFile;
import org.apache.airavata.mft.common.AuthToken;
import org.apache.airavata.mft.core.ConnectorContext;
import org.apache.airavata.mft.core.api.Connector;
import org.apache.airavata.mft.credential.stubs.box.BoxSecret;
import org.apache.airavata.mft.credential.stubs.box.BoxSecretGetRequest;
import org.apache.airavata.mft.resource.client.ResourceServiceClient;
import org.apache.airavata.mft.resource.client.ResourceServiceClientBuilder;
import org.apache.airavata.mft.resource.stubs.common.GenericResource;
import org.apache.airavata.mft.resource.stubs.common.GenericResourceGetRequest;
import org.apache.airavata.mft.secret.client.SecretServiceClient;
import org.apache.airavata.mft.secret.client.SecretServiceClientBuilder;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class BoxSender implements Connector {

    private static final Logger logger = LoggerFactory.getLogger(BoxSender.class);
    private BoxAPIConnection boxClient;

    private String resourceServiceHost;
    private int resourceServicePort;
    private String secretServiceHost;
    private int secretServicePort;

    @Override
    public void init(String resourceServiceHost, int resourceServicePort,
                     String secretServiceHost, int secretServicePort) throws Exception {
        this.resourceServiceHost = resourceServiceHost;
        this.resourceServicePort = resourceServicePort;
        this.secretServiceHost = secretServiceHost;
        this.secretServicePort = secretServicePort;
    }

    @Override
    public void destroy() {

    }

    @Override
    public void startStream(AuthToken authToken, String resourceId, String credentialToken, ConnectorContext context) throws Exception {

        logger.info("Starting Box Sender stream for transfer {}", context.getTransferId());
        logger.debug("Content length for transfer {} {}", context.getTransferId(), context.getMetadata().getResourceSize());

        ResourceServiceClient resourceClient = ResourceServiceClientBuilder.buildClient(resourceServiceHost, resourceServicePort);
        GenericResource resource = resourceClient.get().getGenericResource(GenericResourceGetRequest.newBuilder()
                .setResourceId(resourceId).build());

        if (resource.getStorageCase() != GenericResource.StorageCase.BOXSTORAGE) {
            logger.error("Invalid storage type {} specified for resource {}", resource.getStorageCase(), resourceId);
            throw new Exception("Invalid storage type specified for resource " + resourceId);
        }

        SecretServiceClient secretClient = SecretServiceClientBuilder.buildClient(secretServiceHost, secretServicePort);
        BoxSecret boxSecret = secretClient.box().getBoxSecret(BoxSecretGetRequest.newBuilder().setSecretId(credentialToken).build());

        boxClient = new BoxAPIConnection(boxSecret.getAccessToken());

        BoxFile file = new BoxFile(this.boxClient, resource.getFile().getResourcePath());

        // Upload chunks only if the file size is > 20mb
        // Ref: https://developer.box.com/guides/uploads/chunked/
        if (context.getMetadata().getResourceSize() > 20971520) {
            file.uploadLargeFile(context.getStreamBuffer().getInputStream(), context.getMetadata().getResourceSize());
        } else {
            file.uploadNewVersion(context.getStreamBuffer().getInputStream());
        }

        logger.info("Completed Box Sender stream for transfer {}", context.getTransferId());

    }

    @Override
    public void startStream(AuthToken authToken, String resourceId, String childResourcePath, String credentialToken,
                            ConnectorContext context) throws Exception {
        throw new UnsupportedOperationException();
    }
}
