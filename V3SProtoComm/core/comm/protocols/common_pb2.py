# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common.proto',
  package='fira_message',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0c\x63ommon.proto\x12\x0c\x66ira_message\"K\n\x04\x42\x61ll\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x12\n\n\x02vx\x18\x04 \x01(\x01\x12\n\n\x02vy\x18\x05 \x01(\x01\x12\n\n\x02vz\x18\x06 \x01(\x01\"r\n\x05Robot\x12\x10\n\x08robot_id\x18\x01 \x01(\r\x12\t\n\x01x\x18\x02 \x01(\x01\x12\t\n\x01y\x18\x03 \x01(\x01\x12\x13\n\x0borientation\x18\x04 \x01(\x01\x12\n\n\x02vx\x18\x05 \x01(\x01\x12\n\n\x02vy\x18\x06 \x01(\x01\x12\x14\n\x0cvorientation\x18\x07 \x01(\x01\"N\n\x05\x46ield\x12\r\n\x05width\x18\x01 \x01(\x01\x12\x0e\n\x06length\x18\x02 \x01(\x01\x12\x12\n\ngoal_width\x18\x03 \x01(\x01\x12\x12\n\ngoal_depth\x18\x04 \x01(\x01\"\x7f\n\x05\x46rame\x12 \n\x04\x62\x61ll\x18\x01 \x01(\x0b\x32\x12.fira_message.Ball\x12*\n\rrobots_yellow\x18\x02 \x03(\x0b\x32\x13.fira_message.Robot\x12(\n\x0brobots_blue\x18\x03 \x03(\x0b\x32\x13.fira_message.Robotb\x06proto3')
)




_BALL = _descriptor.Descriptor(
  name='Ball',
  full_name='fira_message.Ball',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='fira_message.Ball.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='fira_message.Ball.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='fira_message.Ball.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vx', full_name='fira_message.Ball.vx', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vy', full_name='fira_message.Ball.vy', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vz', full_name='fira_message.Ball.vz', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=30,
  serialized_end=105,
)


_ROBOT = _descriptor.Descriptor(
  name='Robot',
  full_name='fira_message.Robot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='robot_id', full_name='fira_message.Robot.robot_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x', full_name='fira_message.Robot.x', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='fira_message.Robot.y', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='fira_message.Robot.orientation', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vx', full_name='fira_message.Robot.vx', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vy', full_name='fira_message.Robot.vy', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vorientation', full_name='fira_message.Robot.vorientation', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=107,
  serialized_end=221,
)


_FIELD = _descriptor.Descriptor(
  name='Field',
  full_name='fira_message.Field',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='fira_message.Field.width', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length', full_name='fira_message.Field.length', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='goal_width', full_name='fira_message.Field.goal_width', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='goal_depth', full_name='fira_message.Field.goal_depth', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=223,
  serialized_end=301,
)


_FRAME = _descriptor.Descriptor(
  name='Frame',
  full_name='fira_message.Frame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ball', full_name='fira_message.Frame.ball', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='robots_yellow', full_name='fira_message.Frame.robots_yellow', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='robots_blue', full_name='fira_message.Frame.robots_blue', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=303,
  serialized_end=430,
)

_FRAME.fields_by_name['ball'].message_type = _BALL
_FRAME.fields_by_name['robots_yellow'].message_type = _ROBOT
_FRAME.fields_by_name['robots_blue'].message_type = _ROBOT
DESCRIPTOR.message_types_by_name['Ball'] = _BALL
DESCRIPTOR.message_types_by_name['Robot'] = _ROBOT
DESCRIPTOR.message_types_by_name['Field'] = _FIELD
DESCRIPTOR.message_types_by_name['Frame'] = _FRAME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Ball = _reflection.GeneratedProtocolMessageType('Ball', (_message.Message,), dict(
  DESCRIPTOR = _BALL,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:fira_message.Ball)
  ))
_sym_db.RegisterMessage(Ball)

Robot = _reflection.GeneratedProtocolMessageType('Robot', (_message.Message,), dict(
  DESCRIPTOR = _ROBOT,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:fira_message.Robot)
  ))
_sym_db.RegisterMessage(Robot)

Field = _reflection.GeneratedProtocolMessageType('Field', (_message.Message,), dict(
  DESCRIPTOR = _FIELD,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:fira_message.Field)
  ))
_sym_db.RegisterMessage(Field)

Frame = _reflection.GeneratedProtocolMessageType('Frame', (_message.Message,), dict(
  DESCRIPTOR = _FRAME,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:fira_message.Frame)
  ))
_sym_db.RegisterMessage(Frame)


# @@protoc_insertion_point(module_scope)