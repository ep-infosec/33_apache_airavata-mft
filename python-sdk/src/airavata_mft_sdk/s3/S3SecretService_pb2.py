# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: s3/S3SecretService.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from airavata_mft_sdk.s3 import S3Credential_pb2 as s3_dot_S3Credential__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18s3/S3SecretService.proto\x12-org.apache.airavata.mft.credential.service.s3\x1a\x15s3/S3Credential.proto2\xdf\x04\n\x0fS3SecretService\x12\x85\x01\n\x0bgetS3Secret\x12?.org.apache.airavata.mft.credential.stubs.s3.S3SecretGetRequest\x1a\x35.org.apache.airavata.mft.credential.stubs.s3.S3Secret\x12\x8b\x01\n\x0e\x63reateS3Secret\x12\x42.org.apache.airavata.mft.credential.stubs.s3.S3SecretCreateRequest\x1a\x35.org.apache.airavata.mft.credential.stubs.s3.S3Secret\x12\x99\x01\n\x0eupdateS3Secret\x12\x42.org.apache.airavata.mft.credential.stubs.s3.S3SecretUpdateRequest\x1a\x43.org.apache.airavata.mft.credential.stubs.s3.S3SecretUpdateResponse\x12\x99\x01\n\x0e\x64\x65leteS3Secret\x12\x42.org.apache.airavata.mft.credential.stubs.s3.S3SecretDeleteRequest\x1a\x43.org.apache.airavata.mft.credential.stubs.s3.S3SecretDeleteResponseB\x02P\x01\x62\x06proto3')



_S3SECRETSERVICE = DESCRIPTOR.services_by_name['S3SecretService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _S3SECRETSERVICE._serialized_start=99
  _S3SECRETSERVICE._serialized_end=706
# @@protoc_insertion_point(module_scope)
