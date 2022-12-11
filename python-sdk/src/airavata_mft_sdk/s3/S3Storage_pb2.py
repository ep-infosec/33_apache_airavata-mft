# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: s3/S3Storage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12s3/S3Storage.proto\x12\x31org.apache.airavata.mft.resource.stubs.s3.storage\"r\n\tS3Storage\x12\x11\n\tstorageId\x18\x01 \x01(\t\x12\x12\n\nbucketName\x18\x02 \x01(\t\x12\x0e\n\x06region\x18\x03 \x01(\t\x12\x10\n\x08\x65ndpoint\x18\x04 \x01(\t\x12\x0e\n\x06useTLS\x18\x05 \x01(\x08\x12\x0c\n\x04name\x18\x06 \x01(\t\"5\n\x14S3StorageListRequest\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05\"g\n\x15S3StorageListResponse\x12N\n\x08storages\x18\x01 \x03(\x0b\x32<.org.apache.airavata.mft.resource.stubs.s3.storage.S3Storage\"(\n\x13S3StorageGetRequest\x12\x11\n\tstorageId\x18\x01 \x01(\t\"\x7f\n\x16S3StorageCreateRequest\x12\x12\n\nbucketName\x18\x01 \x01(\t\x12\x0e\n\x06region\x18\x02 \x01(\t\x12\x11\n\tstorageId\x18\x03 \x01(\t\x12\x10\n\x08\x65ndpoint\x18\x04 \x01(\t\x12\x0e\n\x06useTLS\x18\x05 \x01(\x08\x12\x0c\n\x04name\x18\x06 \x01(\t\"\x7f\n\x16S3StorageUpdateRequest\x12\x11\n\tstorageId\x18\x01 \x01(\t\x12\x12\n\nbucketName\x18\x02 \x01(\t\x12\x0e\n\x06region\x18\x03 \x01(\t\x12\x10\n\x08\x65ndpoint\x18\x04 \x01(\t\x12\x0e\n\x06useTLS\x18\x05 \x01(\x08\x12\x0c\n\x04name\x18\x06 \x01(\t\",\n\x17S3StorageUpdateResponse\x12\x11\n\tstorageId\x18\x01 \x01(\t\"+\n\x16S3StorageDeleteRequest\x12\x11\n\tstorageId\x18\x01 \x01(\t\")\n\x17S3StorageDeleteResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x42\x02P\x01\x62\x06proto3')



_S3STORAGE = DESCRIPTOR.message_types_by_name['S3Storage']
_S3STORAGELISTREQUEST = DESCRIPTOR.message_types_by_name['S3StorageListRequest']
_S3STORAGELISTRESPONSE = DESCRIPTOR.message_types_by_name['S3StorageListResponse']
_S3STORAGEGETREQUEST = DESCRIPTOR.message_types_by_name['S3StorageGetRequest']
_S3STORAGECREATEREQUEST = DESCRIPTOR.message_types_by_name['S3StorageCreateRequest']
_S3STORAGEUPDATEREQUEST = DESCRIPTOR.message_types_by_name['S3StorageUpdateRequest']
_S3STORAGEUPDATERESPONSE = DESCRIPTOR.message_types_by_name['S3StorageUpdateResponse']
_S3STORAGEDELETEREQUEST = DESCRIPTOR.message_types_by_name['S3StorageDeleteRequest']
_S3STORAGEDELETERESPONSE = DESCRIPTOR.message_types_by_name['S3StorageDeleteResponse']
S3Storage = _reflection.GeneratedProtocolMessageType('S3Storage', (_message.Message,), {
  'DESCRIPTOR' : _S3STORAGE,
  '__module__' : 's3.S3Storage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.s3.storage.S3Storage)
  })
_sym_db.RegisterMessage(S3Storage)

S3StorageListRequest = _reflection.GeneratedProtocolMessageType('S3StorageListRequest', (_message.Message,), {
  'DESCRIPTOR' : _S3STORAGELISTREQUEST,
  '__module__' : 's3.S3Storage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.s3.storage.S3StorageListRequest)
  })
_sym_db.RegisterMessage(S3StorageListRequest)

S3StorageListResponse = _reflection.GeneratedProtocolMessageType('S3StorageListResponse', (_message.Message,), {
  'DESCRIPTOR' : _S3STORAGELISTRESPONSE,
  '__module__' : 's3.S3Storage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.s3.storage.S3StorageListResponse)
  })
_sym_db.RegisterMessage(S3StorageListResponse)

S3StorageGetRequest = _reflection.GeneratedProtocolMessageType('S3StorageGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _S3STORAGEGETREQUEST,
  '__module__' : 's3.S3Storage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.s3.storage.S3StorageGetRequest)
  })
_sym_db.RegisterMessage(S3StorageGetRequest)

S3StorageCreateRequest = _reflection.GeneratedProtocolMessageType('S3StorageCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _S3STORAGECREATEREQUEST,
  '__module__' : 's3.S3Storage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.s3.storage.S3StorageCreateRequest)
  })
_sym_db.RegisterMessage(S3StorageCreateRequest)

S3StorageUpdateRequest = _reflection.GeneratedProtocolMessageType('S3StorageUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _S3STORAGEUPDATEREQUEST,
  '__module__' : 's3.S3Storage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.s3.storage.S3StorageUpdateRequest)
  })
_sym_db.RegisterMessage(S3StorageUpdateRequest)

S3StorageUpdateResponse = _reflection.GeneratedProtocolMessageType('S3StorageUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _S3STORAGEUPDATERESPONSE,
  '__module__' : 's3.S3Storage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.s3.storage.S3StorageUpdateResponse)
  })
_sym_db.RegisterMessage(S3StorageUpdateResponse)

S3StorageDeleteRequest = _reflection.GeneratedProtocolMessageType('S3StorageDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _S3STORAGEDELETEREQUEST,
  '__module__' : 's3.S3Storage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.s3.storage.S3StorageDeleteRequest)
  })
_sym_db.RegisterMessage(S3StorageDeleteRequest)

S3StorageDeleteResponse = _reflection.GeneratedProtocolMessageType('S3StorageDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _S3STORAGEDELETERESPONSE,
  '__module__' : 's3.S3Storage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.s3.storage.S3StorageDeleteResponse)
  })
_sym_db.RegisterMessage(S3StorageDeleteResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _S3STORAGE._serialized_start=73
  _S3STORAGE._serialized_end=187
  _S3STORAGELISTREQUEST._serialized_start=189
  _S3STORAGELISTREQUEST._serialized_end=242
  _S3STORAGELISTRESPONSE._serialized_start=244
  _S3STORAGELISTRESPONSE._serialized_end=347
  _S3STORAGEGETREQUEST._serialized_start=349
  _S3STORAGEGETREQUEST._serialized_end=389
  _S3STORAGECREATEREQUEST._serialized_start=391
  _S3STORAGECREATEREQUEST._serialized_end=518
  _S3STORAGEUPDATEREQUEST._serialized_start=520
  _S3STORAGEUPDATEREQUEST._serialized_end=647
  _S3STORAGEUPDATERESPONSE._serialized_start=649
  _S3STORAGEUPDATERESPONSE._serialized_end=693
  _S3STORAGEDELETEREQUEST._serialized_start=695
  _S3STORAGEDELETEREQUEST._serialized_end=738
  _S3STORAGEDELETERESPONSE._serialized_start=740
  _S3STORAGEDELETERESPONSE._serialized_end=781
# @@protoc_insertion_point(module_scope)
