# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SimpleCal.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fSimpleCal.proto\".\n\nAddRequest\x12\x0f\n\x07number1\x18\x01 \x01(\x05\x12\x0f\n\x07number2\x18\x02 \x01(\x05\"3\n\x0fMultiplyRequest\x12\x0f\n\x07number1\x18\x01 \x01(\x05\x12\x0f\n\x07number2\x18\x02 \x01(\x05\"\x1d\n\x0bResultReply\x12\x0e\n\x06number\x18\x01 \x01(\x05\x32W\n\x03\x43\x61l\x12\"\n\x03\x41\x64\x64\x12\x0b.AddRequest\x1a\x0c.ResultReply\"\x00\x12,\n\x08Multiply\x12\x10.MultiplyRequest\x1a\x0c.ResultReply\"\x00\x62\x06proto3')



_ADDREQUEST = DESCRIPTOR.message_types_by_name['AddRequest']
_MULTIPLYREQUEST = DESCRIPTOR.message_types_by_name['MultiplyRequest']
_RESULTREPLY = DESCRIPTOR.message_types_by_name['ResultReply']
AddRequest = _reflection.GeneratedProtocolMessageType('AddRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDREQUEST,
  '__module__' : 'SimpleCal_pb2'
  # @@protoc_insertion_point(class_scope:AddRequest)
  })
_sym_db.RegisterMessage(AddRequest)

MultiplyRequest = _reflection.GeneratedProtocolMessageType('MultiplyRequest', (_message.Message,), {
  'DESCRIPTOR' : _MULTIPLYREQUEST,
  '__module__' : 'SimpleCal_pb2'
  # @@protoc_insertion_point(class_scope:MultiplyRequest)
  })
_sym_db.RegisterMessage(MultiplyRequest)

ResultReply = _reflection.GeneratedProtocolMessageType('ResultReply', (_message.Message,), {
  'DESCRIPTOR' : _RESULTREPLY,
  '__module__' : 'SimpleCal_pb2'
  # @@protoc_insertion_point(class_scope:ResultReply)
  })
_sym_db.RegisterMessage(ResultReply)

_CAL = DESCRIPTOR.services_by_name['Cal']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ADDREQUEST._serialized_start=19
  _ADDREQUEST._serialized_end=65
  _MULTIPLYREQUEST._serialized_start=67
  _MULTIPLYREQUEST._serialized_end=118
  _RESULTREPLY._serialized_start=120
  _RESULTREPLY._serialized_end=149
  _CAL._serialized_start=151
  _CAL._serialized_end=238
# @@protoc_insertion_point(module_scope)
