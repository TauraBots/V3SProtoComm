# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vssref_placement.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import vssref_common_pb2 as vssref__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='vssref_placement.proto',
  package='VSSRef.team_to_ref',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16vssref_placement.proto\x12\x12VSSRef.team_to_ref\x1a\x13vssref_common.proto\"0\n\x10VSSRef_Placement\x12\x1c\n\x05world\x18\x01 \x01(\x0b\x32\r.VSSRef.Frameb\x06proto3')
  ,
  dependencies=[vssref__common__pb2.DESCRIPTOR,])




_VSSREF_PLACEMENT = _descriptor.Descriptor(
  name='VSSRef_Placement',
  full_name='VSSRef.team_to_ref.VSSRef_Placement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='world', full_name='VSSRef.team_to_ref.VSSRef_Placement.world', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=115,
)

_VSSREF_PLACEMENT.fields_by_name['world'].message_type = vssref__common__pb2._FRAME
DESCRIPTOR.message_types_by_name['VSSRef_Placement'] = _VSSREF_PLACEMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VSSRef_Placement = _reflection.GeneratedProtocolMessageType('VSSRef_Placement', (_message.Message,), dict(
  DESCRIPTOR = _VSSREF_PLACEMENT,
  __module__ = 'vssref_placement_pb2'
  # @@protoc_insertion_point(class_scope:VSSRef.team_to_ref.VSSRef_Placement)
  ))
_sym_db.RegisterMessage(VSSRef_Placement)


# @@protoc_insertion_point(module_scope)s