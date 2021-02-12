# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arrakisapi/api/core.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='arrakisapi/api/core.proto',
  package='',
  syntax='proto3',
  serialized_options=b'Z$github.com/petricorp/code/arrakisapi',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19\x61rrakisapi/api/core.proto\"U\n\rRelationTuple\x12/\n\x13object_and_relation\x18\x01 \x01(\x0b\x32\x12.ObjectAndRelation\x12\x13\n\x04user\x18\x02 \x01(\x0b\x32\x05.User\"K\n\x11ObjectAndRelation\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x11\n\tobject_id\x18\x02 \x01(\t\x12\x10\n\x08relation\x18\x03 \x01(\t\";\n\x04User\x12%\n\x07userset\x18\x02 \x01(\x0b\x32\x12.ObjectAndRelationH\x00\x42\x0c\n\nuser_oneof\"\x17\n\x06Zookie\x12\r\n\x05token\x18\x01 \x01(\t\"\xa4\x01\n\x13RelationTupleUpdate\x12\x31\n\toperation\x18\x01 \x01(\x0e\x32\x1e.RelationTupleUpdate.Operation\x12\x1d\n\x05tuple\x18\x02 \x01(\x0b\x32\x0e.RelationTuple\";\n\tOperation\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06\x43REATE\x10\x01\x12\t\n\x05TOUCH\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03\"\xa2\x01\n\x15RelationTupleTreeNode\x12\x31\n\x11intermediate_node\x18\x01 \x01(\x0b\x32\x14.SetOperationUsersetH\x00\x12#\n\tleaf_node\x18\x02 \x01(\x0b\x32\x0e.DirectUsersetH\x00\x12$\n\x08\x65xpanded\x18\x03 \x01(\x0b\x32\x12.ObjectAndRelationB\x0b\n\tnode_type\"\xbb\x01\n\x13SetOperationUserset\x12\x31\n\toperation\x18\x01 \x01(\x0e\x32\x1e.SetOperationUserset.Operation\x12+\n\x0b\x63hild_nodes\x18\x02 \x03(\x0b\x32\x16.RelationTupleTreeNode\"D\n\tOperation\x12\x0b\n\x07INVALID\x10\x00\x12\t\n\x05UNION\x10\x01\x12\x10\n\x0cINTERSECTION\x10\x02\x12\r\n\tEXCLUSION\x10\x03\"%\n\rDirectUserset\x12\x14\n\x05users\x18\x01 \x03(\x0b\x32\x05.UserB&Z$github.com/petricorp/code/arrakisapib\x06proto3'
)



_RELATIONTUPLEUPDATE_OPERATION = _descriptor.EnumDescriptor(
  name='Operation',
  full_name='RelationTupleUpdate.Operation',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CREATE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TOUCH', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=385,
  serialized_end=444,
)
_sym_db.RegisterEnumDescriptor(_RELATIONTUPLEUPDATE_OPERATION)

_SETOPERATIONUSERSET_OPERATION = _descriptor.EnumDescriptor(
  name='Operation',
  full_name='SetOperationUserset.Operation',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNION', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERSECTION', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXCLUSION', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=731,
  serialized_end=799,
)
_sym_db.RegisterEnumDescriptor(_SETOPERATIONUSERSET_OPERATION)


_RELATIONTUPLE = _descriptor.Descriptor(
  name='RelationTuple',
  full_name='RelationTuple',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_and_relation', full_name='RelationTuple.object_and_relation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='RelationTuple.user', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=29,
  serialized_end=114,
)


_OBJECTANDRELATION = _descriptor.Descriptor(
  name='ObjectAndRelation',
  full_name='ObjectAndRelation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='ObjectAndRelation.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='object_id', full_name='ObjectAndRelation.object_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='relation', full_name='ObjectAndRelation.relation', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=116,
  serialized_end=191,
)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userset', full_name='User.userset', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='user_oneof', full_name='User.user_oneof',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=193,
  serialized_end=252,
)


_ZOOKIE = _descriptor.Descriptor(
  name='Zookie',
  full_name='Zookie',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='Zookie.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=254,
  serialized_end=277,
)


_RELATIONTUPLEUPDATE = _descriptor.Descriptor(
  name='RelationTupleUpdate',
  full_name='RelationTupleUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='RelationTupleUpdate.operation', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tuple', full_name='RelationTupleUpdate.tuple', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RELATIONTUPLEUPDATE_OPERATION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=280,
  serialized_end=444,
)


_RELATIONTUPLETREENODE = _descriptor.Descriptor(
  name='RelationTupleTreeNode',
  full_name='RelationTupleTreeNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='intermediate_node', full_name='RelationTupleTreeNode.intermediate_node', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='leaf_node', full_name='RelationTupleTreeNode.leaf_node', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expanded', full_name='RelationTupleTreeNode.expanded', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='node_type', full_name='RelationTupleTreeNode.node_type',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=447,
  serialized_end=609,
)


_SETOPERATIONUSERSET = _descriptor.Descriptor(
  name='SetOperationUserset',
  full_name='SetOperationUserset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='SetOperationUserset.operation', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='child_nodes', full_name='SetOperationUserset.child_nodes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SETOPERATIONUSERSET_OPERATION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=612,
  serialized_end=799,
)


_DIRECTUSERSET = _descriptor.Descriptor(
  name='DirectUserset',
  full_name='DirectUserset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='users', full_name='DirectUserset.users', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=801,
  serialized_end=838,
)

_RELATIONTUPLE.fields_by_name['object_and_relation'].message_type = _OBJECTANDRELATION
_RELATIONTUPLE.fields_by_name['user'].message_type = _USER
_USER.fields_by_name['userset'].message_type = _OBJECTANDRELATION
_USER.oneofs_by_name['user_oneof'].fields.append(
  _USER.fields_by_name['userset'])
_USER.fields_by_name['userset'].containing_oneof = _USER.oneofs_by_name['user_oneof']
_RELATIONTUPLEUPDATE.fields_by_name['operation'].enum_type = _RELATIONTUPLEUPDATE_OPERATION
_RELATIONTUPLEUPDATE.fields_by_name['tuple'].message_type = _RELATIONTUPLE
_RELATIONTUPLEUPDATE_OPERATION.containing_type = _RELATIONTUPLEUPDATE
_RELATIONTUPLETREENODE.fields_by_name['intermediate_node'].message_type = _SETOPERATIONUSERSET
_RELATIONTUPLETREENODE.fields_by_name['leaf_node'].message_type = _DIRECTUSERSET
_RELATIONTUPLETREENODE.fields_by_name['expanded'].message_type = _OBJECTANDRELATION
_RELATIONTUPLETREENODE.oneofs_by_name['node_type'].fields.append(
  _RELATIONTUPLETREENODE.fields_by_name['intermediate_node'])
_RELATIONTUPLETREENODE.fields_by_name['intermediate_node'].containing_oneof = _RELATIONTUPLETREENODE.oneofs_by_name['node_type']
_RELATIONTUPLETREENODE.oneofs_by_name['node_type'].fields.append(
  _RELATIONTUPLETREENODE.fields_by_name['leaf_node'])
_RELATIONTUPLETREENODE.fields_by_name['leaf_node'].containing_oneof = _RELATIONTUPLETREENODE.oneofs_by_name['node_type']
_SETOPERATIONUSERSET.fields_by_name['operation'].enum_type = _SETOPERATIONUSERSET_OPERATION
_SETOPERATIONUSERSET.fields_by_name['child_nodes'].message_type = _RELATIONTUPLETREENODE
_SETOPERATIONUSERSET_OPERATION.containing_type = _SETOPERATIONUSERSET
_DIRECTUSERSET.fields_by_name['users'].message_type = _USER
DESCRIPTOR.message_types_by_name['RelationTuple'] = _RELATIONTUPLE
DESCRIPTOR.message_types_by_name['ObjectAndRelation'] = _OBJECTANDRELATION
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Zookie'] = _ZOOKIE
DESCRIPTOR.message_types_by_name['RelationTupleUpdate'] = _RELATIONTUPLEUPDATE
DESCRIPTOR.message_types_by_name['RelationTupleTreeNode'] = _RELATIONTUPLETREENODE
DESCRIPTOR.message_types_by_name['SetOperationUserset'] = _SETOPERATIONUSERSET
DESCRIPTOR.message_types_by_name['DirectUserset'] = _DIRECTUSERSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RelationTuple = _reflection.GeneratedProtocolMessageType('RelationTuple', (_message.Message,), {
  'DESCRIPTOR' : _RELATIONTUPLE,
  '__module__' : 'arrakisapi.api.core_pb2'
  # @@protoc_insertion_point(class_scope:RelationTuple)
  })
_sym_db.RegisterMessage(RelationTuple)

ObjectAndRelation = _reflection.GeneratedProtocolMessageType('ObjectAndRelation', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTANDRELATION,
  '__module__' : 'arrakisapi.api.core_pb2'
  # @@protoc_insertion_point(class_scope:ObjectAndRelation)
  })
_sym_db.RegisterMessage(ObjectAndRelation)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'arrakisapi.api.core_pb2'
  # @@protoc_insertion_point(class_scope:User)
  })
_sym_db.RegisterMessage(User)

Zookie = _reflection.GeneratedProtocolMessageType('Zookie', (_message.Message,), {
  'DESCRIPTOR' : _ZOOKIE,
  '__module__' : 'arrakisapi.api.core_pb2'
  # @@protoc_insertion_point(class_scope:Zookie)
  })
_sym_db.RegisterMessage(Zookie)

RelationTupleUpdate = _reflection.GeneratedProtocolMessageType('RelationTupleUpdate', (_message.Message,), {
  'DESCRIPTOR' : _RELATIONTUPLEUPDATE,
  '__module__' : 'arrakisapi.api.core_pb2'
  # @@protoc_insertion_point(class_scope:RelationTupleUpdate)
  })
_sym_db.RegisterMessage(RelationTupleUpdate)

RelationTupleTreeNode = _reflection.GeneratedProtocolMessageType('RelationTupleTreeNode', (_message.Message,), {
  'DESCRIPTOR' : _RELATIONTUPLETREENODE,
  '__module__' : 'arrakisapi.api.core_pb2'
  # @@protoc_insertion_point(class_scope:RelationTupleTreeNode)
  })
_sym_db.RegisterMessage(RelationTupleTreeNode)

SetOperationUserset = _reflection.GeneratedProtocolMessageType('SetOperationUserset', (_message.Message,), {
  'DESCRIPTOR' : _SETOPERATIONUSERSET,
  '__module__' : 'arrakisapi.api.core_pb2'
  # @@protoc_insertion_point(class_scope:SetOperationUserset)
  })
_sym_db.RegisterMessage(SetOperationUserset)

DirectUserset = _reflection.GeneratedProtocolMessageType('DirectUserset', (_message.Message,), {
  'DESCRIPTOR' : _DIRECTUSERSET,
  '__module__' : 'arrakisapi.api.core_pb2'
  # @@protoc_insertion_point(class_scope:DirectUserset)
  })
_sym_db.RegisterMessage(DirectUserset)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
