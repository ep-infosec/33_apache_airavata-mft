# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dropbox/DropboxSecretService.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from airavata_mft_sdk.dropbox import DropboxCredential_pb2 as dropbox_dot_DropboxCredential__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"dropbox/DropboxSecretService.proto\x12\x32org.apache.airavata.mft.credential.service.dropbox\x1a\x1f\x64ropbox/DropboxCredential.proto2\xc8\x05\n\x14\x44ropboxSecretService\x12\x9e\x01\n\x10getDropboxSecret\x12I.org.apache.airavata.mft.credential.stubs.dropbox.DropboxSecretGetRequest\x1a?.org.apache.airavata.mft.credential.stubs.dropbox.DropboxSecret\x12\xa4\x01\n\x13\x63reateDropboxSecret\x12L.org.apache.airavata.mft.credential.stubs.dropbox.DropboxSecretCreateRequest\x1a?.org.apache.airavata.mft.credential.stubs.dropbox.DropboxSecret\x12\xb2\x01\n\x13updateDropboxSecret\x12L.org.apache.airavata.mft.credential.stubs.dropbox.DropboxSecretUpdateRequest\x1aM.org.apache.airavata.mft.credential.stubs.dropbox.DropboxSecretUpdateResponse\x12\xb2\x01\n\x13\x64\x65leteDropboxSecret\x12L.org.apache.airavata.mft.credential.stubs.dropbox.DropboxSecretDeleteRequest\x1aM.org.apache.airavata.mft.credential.stubs.dropbox.DropboxSecretDeleteResponseB\x02P\x01\x62\x06proto3')



_DROPBOXSECRETSERVICE = DESCRIPTOR.services_by_name['DropboxSecretService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _DROPBOXSECRETSERVICE._serialized_start=124
  _DROPBOXSECRETSERVICE._serialized_end=836
# @@protoc_insertion_point(module_scope)
