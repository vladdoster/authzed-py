# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arrakisapi/api/namespace_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from arrakisapi.api import core_pb2 as arrakisapi_dot_api_dot_core__pb2
from arrakisapi.api import namespace_pb2 as arrakisapi_dot_api_dot_namespace__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='arrakisapi/api/namespace_service.proto',
  package='',
  syntax='proto3',
  serialized_options=b'Z$github.com/petricorp/code/arrakisapi',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&arrakisapi/api/namespace_service.proto\x1a\x19\x61rrakisapi/api/core.proto\x1a\x1e\x61rrakisapi/api/namespace.proto\"D\n\x11ReadConfigRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x1c\n\x0b\x61t_revision\x18\x02 \x01(\x0b\x32\x07.Zookie\"h\n\x12ReadConfigResponse\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12$\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x14.NamespaceDefinition\x12\x19\n\x08revision\x18\x04 \x01(\x0b\x32\x07.Zookie\":\n\x12WriteConfigRequest\x12$\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x14.NamespaceDefinition\"0\n\x13WriteConfigResponse\x12\x19\n\x08revision\x18\x01 \x01(\x0b\x32\x07.Zookie2\x87\x01\n\x10NamespaceService\x12\x37\n\nReadConfig\x12\x12.ReadConfigRequest\x1a\x13.ReadConfigResponse\"\x00\x12:\n\x0bWriteConfig\x12\x13.WriteConfigRequest\x1a\x14.WriteConfigResponse\"\x00\x42&Z$github.com/petricorp/code/arrakisapib\x06proto3'
  ,
  dependencies=[arrakisapi_dot_api_dot_core__pb2.DESCRIPTOR,arrakisapi_dot_api_dot_namespace__pb2.DESCRIPTOR,])




_READCONFIGREQUEST = _descriptor.Descriptor(
  name='ReadConfigRequest',
  full_name='ReadConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='ReadConfigRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='at_revision', full_name='ReadConfigRequest.at_revision', index=1,
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
  serialized_start=101,
  serialized_end=169,
)


_READCONFIGRESPONSE = _descriptor.Descriptor(
  name='ReadConfigResponse',
  full_name='ReadConfigResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='ReadConfigResponse.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='ReadConfigResponse.config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='revision', full_name='ReadConfigResponse.revision', index=2,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=171,
  serialized_end=275,
)


_WRITECONFIGREQUEST = _descriptor.Descriptor(
  name='WriteConfigRequest',
  full_name='WriteConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='WriteConfigRequest.config', index=0,
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
  serialized_start=277,
  serialized_end=335,
)


_WRITECONFIGRESPONSE = _descriptor.Descriptor(
  name='WriteConfigResponse',
  full_name='WriteConfigResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='revision', full_name='WriteConfigResponse.revision', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=337,
  serialized_end=385,
)

_READCONFIGREQUEST.fields_by_name['at_revision'].message_type = arrakisapi_dot_api_dot_core__pb2._ZOOKIE
_READCONFIGRESPONSE.fields_by_name['config'].message_type = arrakisapi_dot_api_dot_namespace__pb2._NAMESPACEDEFINITION
_READCONFIGRESPONSE.fields_by_name['revision'].message_type = arrakisapi_dot_api_dot_core__pb2._ZOOKIE
_WRITECONFIGREQUEST.fields_by_name['config'].message_type = arrakisapi_dot_api_dot_namespace__pb2._NAMESPACEDEFINITION
_WRITECONFIGRESPONSE.fields_by_name['revision'].message_type = arrakisapi_dot_api_dot_core__pb2._ZOOKIE
DESCRIPTOR.message_types_by_name['ReadConfigRequest'] = _READCONFIGREQUEST
DESCRIPTOR.message_types_by_name['ReadConfigResponse'] = _READCONFIGRESPONSE
DESCRIPTOR.message_types_by_name['WriteConfigRequest'] = _WRITECONFIGREQUEST
DESCRIPTOR.message_types_by_name['WriteConfigResponse'] = _WRITECONFIGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReadConfigRequest = _reflection.GeneratedProtocolMessageType('ReadConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _READCONFIGREQUEST,
  '__module__' : 'arrakisapi.api.namespace_service_pb2'
  # @@protoc_insertion_point(class_scope:ReadConfigRequest)
  })
_sym_db.RegisterMessage(ReadConfigRequest)

ReadConfigResponse = _reflection.GeneratedProtocolMessageType('ReadConfigResponse', (_message.Message,), {
  'DESCRIPTOR' : _READCONFIGRESPONSE,
  '__module__' : 'arrakisapi.api.namespace_service_pb2'
  # @@protoc_insertion_point(class_scope:ReadConfigResponse)
  })
_sym_db.RegisterMessage(ReadConfigResponse)

WriteConfigRequest = _reflection.GeneratedProtocolMessageType('WriteConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _WRITECONFIGREQUEST,
  '__module__' : 'arrakisapi.api.namespace_service_pb2'
  # @@protoc_insertion_point(class_scope:WriteConfigRequest)
  })
_sym_db.RegisterMessage(WriteConfigRequest)

WriteConfigResponse = _reflection.GeneratedProtocolMessageType('WriteConfigResponse', (_message.Message,), {
  'DESCRIPTOR' : _WRITECONFIGRESPONSE,
  '__module__' : 'arrakisapi.api.namespace_service_pb2'
  # @@protoc_insertion_point(class_scope:WriteConfigResponse)
  })
_sym_db.RegisterMessage(WriteConfigResponse)


DESCRIPTOR._options = None

_NAMESPACESERVICE = _descriptor.ServiceDescriptor(
  name='NamespaceService',
  full_name='NamespaceService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=388,
  serialized_end=523,
  methods=[
  _descriptor.MethodDescriptor(
    name='ReadConfig',
    full_name='NamespaceService.ReadConfig',
    index=0,
    containing_service=None,
    input_type=_READCONFIGREQUEST,
    output_type=_READCONFIGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='WriteConfig',
    full_name='NamespaceService.WriteConfig',
    index=1,
    containing_service=None,
    input_type=_WRITECONFIGREQUEST,
    output_type=_WRITECONFIGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_NAMESPACESERVICE)

DESCRIPTOR.services_by_name['NamespaceService'] = _NAMESPACESERVICE

# @@protoc_insertion_point(module_scope)
