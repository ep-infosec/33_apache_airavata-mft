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

package org.apache.airavata.mft.admin.models;

import java.util.List;

public class AgentInfo {
    private String id;
    private String host;
    private String user;
    private boolean sudo;
    private String sessionId;
    private List<String> supportedProtocols;
    private List<String> localStorages;

    public String getId() {
        return id;
    }

    public AgentInfo setId(String id) {
        this.id = id;
        return this;
    }

    public String getHost() {
        return host;
    }

    public AgentInfo setHost(String host) {
        this.host = host;
        return this;
    }

    public String getUser() {
        return user;
    }

    public AgentInfo setUser(String user) {
        this.user = user;
        return this;
    }

    public boolean isSudo() {
        return sudo;
    }

    public AgentInfo setSudo(boolean sudo) {
        this.sudo = sudo;
        return this;
    }

    public List<String> getSupportedProtocols() {
        return supportedProtocols;
    }

    public AgentInfo setSupportedProtocols(List<String> supportedProtocols) {
        this.supportedProtocols = supportedProtocols;
        return this;
    }

    public List<String> getLocalStorages() {
        return localStorages;
    }

    public AgentInfo setLocalStorages(List<String> localStorages) {
        this.localStorages = localStorages;
        return this;
    }

    public String getSessionId() {
        return sessionId;
    }

    public AgentInfo setSessionId(String sessionId) {
        this.sessionId = sessionId;
        return this;
    }
}
