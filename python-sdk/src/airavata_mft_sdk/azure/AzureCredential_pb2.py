# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: azure/AzureCredential.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import airavata_mft_sdk.CredCommon_pb2 as CredCommon__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x61zure/AzureCredential.proto\x12.org.apache.airavata.mft.credential.stubs.azure\x1a\x10\x43redCommon.proto\"9\n\x0b\x41zureSecret\x12\x10\n\x08secretId\x18\x01 \x01(\t\x12\x18\n\x10\x63onnectionString\x18\x02 \x01(\t\"h\n\x15\x41zureSecretGetRequest\x12\x10\n\x08secretId\x18\x01 \x01(\t\x12=\n\nauthzToken\x18\x02 \x01(\x0b\x32).org.apache.airavata.mft.common.AuthToken\"s\n\x18\x41zureSecretCreateRequest\x12\x18\n\x10\x63onnectionString\x18\x01 \x01(\t\x12=\n\nauthzToken\x18\x02 \x01(\x0b\x32).org.apache.airavata.mft.common.AuthToken\"\x85\x01\n\x18\x41zureSecretUpdateRequest\x12\x10\n\x08secretId\x18\x01 \x01(\t\x12\x18\n\x10\x63onnectionString\x18\x02 \x01(\t\x12=\n\nauthzToken\x18\x03 \x01(\x0b\x32).org.apache.airavata.mft.common.AuthToken\"-\n\x19\x41zureSecretUpdateResponse\x12\x10\n\x08secretId\x18\x01 \x01(\t\"k\n\x18\x41zureSecretDeleteRequest\x12\x10\n\x08secretId\x18\x01 \x01(\t\x12=\n\nauthzToken\x18\x02 \x01(\x0b\x32).org.apache.airavata.mft.common.AuthToken\"+\n\x19\x41zureSecretDeleteResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x42\x02P\x01\x62\x06proto3')



_AZURESECRET = DESCRIPTOR.message_types_by_name['AzureSecret']
_AZURESECRETGETREQUEST = DESCRIPTOR.message_types_by_name['AzureSecretGetRequest']
_AZURESECRETCREATEREQUEST = DESCRIPTOR.message_types_by_name['AzureSecretCreateRequest']
_AZURESECRETUPDATEREQUEST = DESCRIPTOR.message_types_by_name['AzureSecretUpdateRequest']
_AZURESECRETUPDATERESPONSE = DESCRIPTOR.message_types_by_name['AzureSecretUpdateResponse']
_AZURESECRETDELETEREQUEST = DESCRIPTOR.message_types_by_name['AzureSecretDeleteRequest']
_AZURESECRETDELETERESPONSE = DESCRIPTOR.message_types_by_name['AzureSecretDeleteResponse']
AzureSecret = _reflection.GeneratedProtocolMessageType('AzureSecret', (_message.Message,), {
  'DESCRIPTOR' : _AZURESECRET,
  '__module__' : 'azure.AzureCredential_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.credential.stubs.azure.AzureSecret)
  })
_sym_db.RegisterMessage(AzureSecret)

AzureSecretGetRequest = _reflection.GeneratedProtocolMessageType('AzureSecretGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _AZURESECRETGETREQUEST,
  '__module__' : 'azure.AzureCredential_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.credential.stubs.azure.AzureSecretGetRequest)
  })
_sym_db.RegisterMessage(AzureSecretGetRequest)

AzureSecretCreateRequest = _reflection.GeneratedProtocolMessageType('AzureSecretCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _AZURESECRETCREATEREQUEST,
  '__module__' : 'azure.AzureCredential_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.credential.stubs.azure.AzureSecretCreateRequest)
  })
_sym_db.RegisterMessage(AzureSecretCreateRequest)

AzureSecretUpdateRequest = _reflection.GeneratedProtocolMessageType('AzureSecretUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _AZURESECRETUPDATEREQUEST,
  '__module__' : 'azure.AzureCredential_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.credential.stubs.azure.AzureSecretUpdateRequest)
  })
_sym_db.RegisterMessage(AzureSecretUpdateRequest)

AzureSecretUpdateResponse = _reflection.GeneratedProtocolMessageType('AzureSecretUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _AZURESECRETUPDATERESPONSE,
  '__module__' : 'azure.AzureCredential_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.credential.stubs.azure.AzureSecretUpdateResponse)
  })
_sym_db.RegisterMessage(AzureSecretUpdateResponse)

AzureSecretDeleteRequest = _reflection.GeneratedProtocolMessageType('AzureSecretDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _AZURESECRETDELETEREQUEST,
  '__module__' : 'azure.AzureCredential_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.credential.stubs.azure.AzureSecretDeleteRequest)
  })
_sym_db.RegisterMessage(AzureSecretDeleteRequest)

AzureSecretDeleteResponse = _reflection.GeneratedProtocolMessageType('AzureSecretDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _AZURESECRETDELETERESPONSE,
  '__module__' : 'azure.AzureCredential_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.credential.stubs.azure.AzureSecretDeleteResponse)
  })
_sym_db.RegisterMessage(AzureSecretDeleteResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _AZURESECRET._serialized_start=97
  _AZURESECRET._serialized_end=154
  _AZURESECRETGETREQUEST._serialized_start=156
  _AZURESECRETGETREQUEST._serialized_end=260
  _AZURESECRETCREATEREQUEST._serialized_start=262
  _AZURESECRETCREATEREQUEST._serialized_end=377
  _AZURESECRETUPDATEREQUEST._serialized_start=380
  _AZURESECRETUPDATEREQUEST._serialized_end=513
  _AZURESECRETUPDATERESPONSE._serialized_start=515
  _AZURESECRETUPDATERESPONSE._serialized_end=560
  _AZURESECRETDELETEREQUEST._serialized_start=562
  _AZURESECRETDELETEREQUEST._serialized_end=669
  _AZURESECRETDELETERESPONSE._serialized_start=671
  _AZURESECRETDELETERESPONSE._serialized_end=714
# @@protoc_insertion_point(module_scope)
