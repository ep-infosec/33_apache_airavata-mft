# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gcs/GCSStorage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14gcs/GCSStorage.proto\x12\x32org.apache.airavata.mft.resource.stubs.gcs.storage\"A\n\nGCSStorage\x12\x11\n\tstorageId\x18\x01 \x01(\t\x12\x12\n\nbucketName\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"6\n\x15GCSStorageListRequest\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05\"j\n\x16GCSStorageListResponse\x12P\n\x08storages\x18\x01 \x03(\x0b\x32>.org.apache.airavata.mft.resource.stubs.gcs.storage.GCSStorage\")\n\x14GCSStorageGetRequest\x12\x11\n\tstorageId\x18\x01 \x01(\t\"N\n\x17GCSStorageCreateRequest\x12\x12\n\nbucketName\x18\x01 \x01(\t\x12\x11\n\tstorageId\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"N\n\x17GCSStorageUpdateRequest\x12\x11\n\tstorageId\x18\x01 \x01(\t\x12\x12\n\nbucketName\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"-\n\x18GCSStorageUpdateResponse\x12\x11\n\tstorageId\x18\x01 \x01(\t\",\n\x17GCSStorageDeleteRequest\x12\x11\n\tstorageId\x18\x01 \x01(\t\"*\n\x18GCSStorageDeleteResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x42\x02P\x01\x62\x06proto3')



_GCSSTORAGE = DESCRIPTOR.message_types_by_name['GCSStorage']
_GCSSTORAGELISTREQUEST = DESCRIPTOR.message_types_by_name['GCSStorageListRequest']
_GCSSTORAGELISTRESPONSE = DESCRIPTOR.message_types_by_name['GCSStorageListResponse']
_GCSSTORAGEGETREQUEST = DESCRIPTOR.message_types_by_name['GCSStorageGetRequest']
_GCSSTORAGECREATEREQUEST = DESCRIPTOR.message_types_by_name['GCSStorageCreateRequest']
_GCSSTORAGEUPDATEREQUEST = DESCRIPTOR.message_types_by_name['GCSStorageUpdateRequest']
_GCSSTORAGEUPDATERESPONSE = DESCRIPTOR.message_types_by_name['GCSStorageUpdateResponse']
_GCSSTORAGEDELETEREQUEST = DESCRIPTOR.message_types_by_name['GCSStorageDeleteRequest']
_GCSSTORAGEDELETERESPONSE = DESCRIPTOR.message_types_by_name['GCSStorageDeleteResponse']
GCSStorage = _reflection.GeneratedProtocolMessageType('GCSStorage', (_message.Message,), {
  'DESCRIPTOR' : _GCSSTORAGE,
  '__module__' : 'gcs.GCSStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.gcs.storage.GCSStorage)
  })
_sym_db.RegisterMessage(GCSStorage)

GCSStorageListRequest = _reflection.GeneratedProtocolMessageType('GCSStorageListRequest', (_message.Message,), {
  'DESCRIPTOR' : _GCSSTORAGELISTREQUEST,
  '__module__' : 'gcs.GCSStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.gcs.storage.GCSStorageListRequest)
  })
_sym_db.RegisterMessage(GCSStorageListRequest)

GCSStorageListResponse = _reflection.GeneratedProtocolMessageType('GCSStorageListResponse', (_message.Message,), {
  'DESCRIPTOR' : _GCSSTORAGELISTRESPONSE,
  '__module__' : 'gcs.GCSStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.gcs.storage.GCSStorageListResponse)
  })
_sym_db.RegisterMessage(GCSStorageListResponse)

GCSStorageGetRequest = _reflection.GeneratedProtocolMessageType('GCSStorageGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GCSSTORAGEGETREQUEST,
  '__module__' : 'gcs.GCSStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.gcs.storage.GCSStorageGetRequest)
  })
_sym_db.RegisterMessage(GCSStorageGetRequest)

GCSStorageCreateRequest = _reflection.GeneratedProtocolMessageType('GCSStorageCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _GCSSTORAGECREATEREQUEST,
  '__module__' : 'gcs.GCSStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.gcs.storage.GCSStorageCreateRequest)
  })
_sym_db.RegisterMessage(GCSStorageCreateRequest)

GCSStorageUpdateRequest = _reflection.GeneratedProtocolMessageType('GCSStorageUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _GCSSTORAGEUPDATEREQUEST,
  '__module__' : 'gcs.GCSStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.gcs.storage.GCSStorageUpdateRequest)
  })
_sym_db.RegisterMessage(GCSStorageUpdateRequest)

GCSStorageUpdateResponse = _reflection.GeneratedProtocolMessageType('GCSStorageUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _GCSSTORAGEUPDATERESPONSE,
  '__module__' : 'gcs.GCSStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.gcs.storage.GCSStorageUpdateResponse)
  })
_sym_db.RegisterMessage(GCSStorageUpdateResponse)

GCSStorageDeleteRequest = _reflection.GeneratedProtocolMessageType('GCSStorageDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _GCSSTORAGEDELETEREQUEST,
  '__module__' : 'gcs.GCSStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.gcs.storage.GCSStorageDeleteRequest)
  })
_sym_db.RegisterMessage(GCSStorageDeleteRequest)

GCSStorageDeleteResponse = _reflection.GeneratedProtocolMessageType('GCSStorageDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _GCSSTORAGEDELETERESPONSE,
  '__module__' : 'gcs.GCSStorage_pb2'
  # @@protoc_insertion_point(class_scope:org.apache.airavata.mft.resource.stubs.gcs.storage.GCSStorageDeleteResponse)
  })
_sym_db.RegisterMessage(GCSStorageDeleteResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _GCSSTORAGE._serialized_start=76
  _GCSSTORAGE._serialized_end=141
  _GCSSTORAGELISTREQUEST._serialized_start=143
  _GCSSTORAGELISTREQUEST._serialized_end=197
  _GCSSTORAGELISTRESPONSE._serialized_start=199
  _GCSSTORAGELISTRESPONSE._serialized_end=305
  _GCSSTORAGEGETREQUEST._serialized_start=307
  _GCSSTORAGEGETREQUEST._serialized_end=348
  _GCSSTORAGECREATEREQUEST._serialized_start=350
  _GCSSTORAGECREATEREQUEST._serialized_end=428
  _GCSSTORAGEUPDATEREQUEST._serialized_start=430
  _GCSSTORAGEUPDATEREQUEST._serialized_end=508
  _GCSSTORAGEUPDATERESPONSE._serialized_start=510
  _GCSSTORAGEUPDATERESPONSE._serialized_end=555
  _GCSSTORAGEDELETEREQUEST._serialized_start=557
  _GCSSTORAGEDELETEREQUEST._serialized_end=601
  _GCSSTORAGEDELETERESPONSE._serialized_start=603
  _GCSSTORAGEDELETERESPONSE._serialized_end=645
# @@protoc_insertion_point(module_scope)
