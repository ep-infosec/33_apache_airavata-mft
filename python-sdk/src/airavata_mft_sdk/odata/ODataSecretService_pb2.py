# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: odata/ODataSecretService.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from airavata_mft_sdk.odata import ODataCredential_pb2 as odata_dot_ODataCredential__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eodata/ODataSecretService.proto\x12\x30org.apache.airavata.mft.credential.service.odata\x1a\x1bodata/ODataCredential.proto2\x9e\x05\n\x12ODataSecretService\x12\x94\x01\n\x0egetODataSecret\x12\x45.org.apache.airavata.mft.credential.stubs.odata.ODataSecretGetRequest\x1a;.org.apache.airavata.mft.credential.stubs.odata.ODataSecret\x12\x9a\x01\n\x11\x63reateODataSecret\x12H.org.apache.airavata.mft.credential.stubs.odata.ODataSecretCreateRequest\x1a;.org.apache.airavata.mft.credential.stubs.odata.ODataSecret\x12\xa8\x01\n\x11updateODataSecret\x12H.org.apache.airavata.mft.credential.stubs.odata.ODataSecretUpdateRequest\x1aI.org.apache.airavata.mft.credential.stubs.odata.ODataSecretUpdateResponse\x12\xa8\x01\n\x11\x64\x65leteODataSecret\x12H.org.apache.airavata.mft.credential.stubs.odata.ODataSecretDeleteRequest\x1aI.org.apache.airavata.mft.credential.stubs.odata.ODataSecretDeleteResponseB\x02P\x01\x62\x06proto3')



_ODATASECRETSERVICE = DESCRIPTOR.services_by_name['ODataSecretService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _ODATASECRETSERVICE._serialized_start=114
  _ODATASECRETSERVICE._serialized_end=784
# @@protoc_insertion_point(module_scope)
