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

package org.apache.airavata.mft.transport.swift;

import org.apache.airavata.mft.agent.stub.*;
import org.apache.airavata.mft.core.api.MetadataCollector;
import org.apache.airavata.mft.credential.stubs.swift.SwiftSecret;
import org.apache.airavata.mft.resource.stubs.swift.storage.SwiftStorage;
import org.jclouds.ContextBuilder;
import org.jclouds.openstack.keystone.auth.config.CredentialTypes;
import org.jclouds.openstack.keystone.config.KeystoneProperties;
import org.jclouds.openstack.swift.v1.SwiftApi;
import org.jclouds.openstack.swift.v1.domain.ObjectList;
import org.jclouds.openstack.swift.v1.domain.SwiftObject;
import org.jclouds.openstack.swift.v1.features.ObjectApi;

import java.util.Properties;

public class SwiftMetadataCollector implements MetadataCollector {
    boolean initialized = false;
    private SwiftStorage swiftStorage;
    private SwiftSecret swiftSecret;

    @Override
    public void init(StorageWrapper storage, SecretWrapper secret) {
        this.swiftStorage = storage.getSwift();
        this.swiftSecret = secret.getSwift();
        this.initialized = true;
    }

    private void checkInitialized() {
        if (!initialized) {
            throw new IllegalStateException("Swift Metadata Collector is not initialized");
        }
    }

    private SwiftApi getSwiftApi(SwiftStorage swiftStorage, SwiftSecret swiftSecret) {
        String provider = "openstack-swift";

        Properties overrides = new Properties();
        overrides.put(KeystoneProperties.KEYSTONE_VERSION, swiftStorage.getKeystoneVersion() + "");

        String identity = null;
        String credential = null;
        switch (swiftSecret.getSecretCase()) {
            case PASSWORDSECRET:
                identity = swiftSecret.getPasswordSecret().getDomainId() + ":" + swiftSecret.getPasswordSecret().getUserName();
                credential = swiftSecret.getPasswordSecret().getPassword();
                overrides.put(KeystoneProperties.SCOPE, "projectId:" + swiftSecret.getPasswordSecret().getProjectId());
                overrides.put(KeystoneProperties.CREDENTIAL_TYPE, CredentialTypes.PASSWORD_CREDENTIALS);
                break;
            case AUTHCREDENTIALSECRET:
                identity = swiftSecret.getAuthCredentialSecret().getCredentialId();
                credential = swiftSecret.getAuthCredentialSecret().getCredentialSecret();
                overrides.put(KeystoneProperties.CREDENTIAL_TYPE, CredentialTypes.API_ACCESS_KEY_CREDENTIALS);
                break;
        }

        return ContextBuilder.newBuilder(provider)
                .endpoint(swiftStorage.getEndpoint())
                .credentials(identity, credential)
                .overrides(overrides)
                .buildApi(SwiftApi.class);
    }

    @Override
    public ResourceMetadata getResourceMetadata(String resourcePath) throws Exception {
        checkInitialized();

        SwiftApi swiftApi = getSwiftApi(swiftStorage, swiftSecret);

        ObjectApi objectApi = swiftApi.getObjectApi(swiftStorage.getRegion(), swiftStorage.getContainer());

        ResourceMetadata.Builder resourceBuilder = ResourceMetadata.newBuilder();
        if ("".equals(resourcePath)) {
            DirectoryMetadata.Builder rootDirBuilder = DirectoryMetadata.newBuilder();

            ObjectList objectList = objectApi.list();
            objectList.forEach(swiftObject -> {
                FileMetadata.Builder fileBuilder = FileMetadata.newBuilder();
                fileBuilder.setFriendlyName(swiftObject.getName());
                fileBuilder.setResourcePath(swiftObject.getName());
                fileBuilder.setCreatedTime(swiftObject.getLastModified().getTime());
                fileBuilder.setUpdateTime(swiftObject.getLastModified().getTime());
                fileBuilder.setResourceSize(swiftObject.getPayload().getContentMetadata().getContentLength());
                rootDirBuilder.addFiles(fileBuilder);
            });
            resourceBuilder.setDirectory(rootDirBuilder);
        } else {
            SwiftObject swiftObject = objectApi.get(resourcePath);

            if (swiftObject == null) {
                resourceBuilder.setError(MetadataFetchError.NOT_FOUND);
                return resourceBuilder.build();
            }

            FileMetadata.Builder fileBuilder = FileMetadata.newBuilder();
            fileBuilder.setFriendlyName(swiftObject.getName());
            fileBuilder.setResourcePath(swiftObject.getName());
            fileBuilder.setCreatedTime(swiftObject.getLastModified().getTime());
            fileBuilder.setUpdateTime(swiftObject.getLastModified().getTime());
            fileBuilder.setResourceSize(swiftObject.getPayload().getContentMetadata().getContentLength());
            resourceBuilder.setFile(fileBuilder);
        }
        return resourceBuilder.build();
    }

    @Override
    public Boolean isAvailable(String resourcePath) throws Exception {
        checkInitialized();

        SwiftApi swiftApi = getSwiftApi(swiftStorage, swiftSecret);

        ObjectApi objectApi = swiftApi.getObjectApi(swiftStorage.getRegion(), swiftStorage.getContainer());

        SwiftObject swiftObject = objectApi.get(resourcePath);

        return swiftObject != null;
    }
}
