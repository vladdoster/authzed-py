# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: authzed/api/materialize/v0/watchpermissionsets.proto
# Protobuf Python Version: 5.27.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    1,
    '',
    'authzed/api/materialize/v0/watchpermissionsets.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from authzed.api.v1 import core_pb2 as authzed_dot_api_dot_v1_dot_core__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4authzed/api/materialize/v0/watchpermissionsets.proto\x12\x1a\x61uthzed.api.materialize.v0\x1a\x19\x61uthzed/api/v1/core.proto\"n\n\x1aWatchPermissionSetsRequest\x12P\n\x17optional_starting_after\x18\x01 \x01(\x0b\x32\x18.authzed.api.v1.ZedTokenR\x15optionalStartingAfter\"\xc3\x02\n\x1bWatchPermissionSetsResponse\x12I\n\x06\x63hange\x18\x01 \x01(\x0b\x32/.authzed.api.materialize.v0.PermissionSetChangeH\x00R\x06\x63hange\x12I\n\x12\x63ompleted_revision\x18\x02 \x01(\x0b\x32\x18.authzed.api.v1.ZedTokenH\x00R\x11\x63ompletedRevision\x12\x81\x01\n\x1flookup_permission_sets_required\x18\x03 \x01(\x0b\x32\x38.authzed.api.materialize.v0.LookupPermissionSetsRequiredH\x00R\x1clookupPermissionSetsRequiredB\n\n\x08response\"\xa2\x01\n\x06\x43ursor\x12\x14\n\x05limit\x18\x01 \x01(\rR\x05limit\x12.\n\x05token\x18\x04 \x01(\x0b\x32\x18.authzed.api.v1.ZedTokenR\x05token\x12%\n\x0estarting_index\x18\x05 \x01(\rR\rstartingIndex\x12+\n\x11\x63ompleted_members\x18\x06 \x01(\x08R\x10\x63ompletedMembers\"\x9c\x01\n\x1bLookupPermissionSetsRequest\x12\x14\n\x05limit\x18\x01 \x01(\rR\x05limit\x12g\n\x1eoptional_starting_after_cursor\x18\x04 \x01(\x0b\x32\".authzed.api.materialize.v0.CursorR\x1boptionalStartingAfterCursor\"\xa3\x01\n\x1cLookupPermissionSetsResponse\x12G\n\x06\x63hange\x18\x01 \x01(\x0b\x32/.authzed.api.materialize.v0.PermissionSetChangeR\x06\x63hange\x12:\n\x06\x63ursor\x18\x02 \x01(\x0b\x32\".authzed.api.materialize.v0.CursorR\x06\x63ursor\"\xfc\x03\n\x13PermissionSetChange\x12\x39\n\x0b\x61t_revision\x18\x01 \x01(\x0b\x32\x18.authzed.api.v1.ZedTokenR\natRevision\x12Z\n\toperation\x18\x02 \x01(\x0e\x32<.authzed.api.materialize.v0.PermissionSetChange.SetOperationR\toperation\x12G\n\nparent_set\x18\x03 \x01(\x0b\x32(.authzed.api.materialize.v0.SetReferenceR\tparentSet\x12G\n\tchild_set\x18\x04 \x01(\x0b\x32(.authzed.api.materialize.v0.SetReferenceH\x00R\x08\x63hildSet\x12P\n\x0c\x63hild_member\x18\x05 \x01(\x0b\x32+.authzed.api.materialize.v0.MemberReferenceH\x00R\x0b\x63hildMember\"a\n\x0cSetOperation\x12\x1d\n\x19SET_OPERATION_UNSPECIFIED\x10\x00\x12\x17\n\x13SET_OPERATION_ADDED\x10\x01\x12\x19\n\x15SET_OPERATION_REMOVED\x10\x02\x42\x07\n\x05\x63hild\"\x82\x01\n\x0cSetReference\x12\x1f\n\x0bobject_type\x18\x01 \x01(\tR\nobjectType\x12\x1b\n\tobject_id\x18\x02 \x01(\tR\x08objectId\x12\x34\n\x16permission_or_relation\x18\x03 \x01(\tR\x14permissionOrRelation\"\x96\x01\n\x0fMemberReference\x12\x1f\n\x0bobject_type\x18\x01 \x01(\tR\nobjectType\x12\x1b\n\tobject_id\x18\x02 \x01(\tR\x08objectId\x12\x45\n\x1foptional_permission_or_relation\x18\x03 \x01(\tR\x1coptionalPermissionOrRelation\"f\n\x1cLookupPermissionSetsRequired\x12\x46\n\x12required_lookup_at\x18\x01 \x01(\x0b\x32\x18.authzed.api.v1.ZedTokenR\x10requiredLookupAt2\xb9\x02\n\x1aWatchPermissionSetsService\x12\x8a\x01\n\x13WatchPermissionSets\x12\x36.authzed.api.materialize.v0.WatchPermissionSetsRequest\x1a\x37.authzed.api.materialize.v0.WatchPermissionSetsResponse\"\x00\x30\x01\x12\x8d\x01\n\x14LookupPermissionSets\x12\x37.authzed.api.materialize.v0.LookupPermissionSetsRequest\x1a\x38.authzed.api.materialize.v0.LookupPermissionSetsResponse\"\x00\x30\x01\x42\x62\n\x1e\x63om.authzed.api.materialize.v0P\x01Z>github.com/authzed/authzed-go/proto/authzed/api/materialize/v0b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'authzed.api.materialize.v0.watchpermissionsets_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.authzed.api.materialize.v0P\001Z>github.com/authzed/authzed-go/proto/authzed/api/materialize/v0'
  _globals['_WATCHPERMISSIONSETSREQUEST']._serialized_start=111
  _globals['_WATCHPERMISSIONSETSREQUEST']._serialized_end=221
  _globals['_WATCHPERMISSIONSETSRESPONSE']._serialized_start=224
  _globals['_WATCHPERMISSIONSETSRESPONSE']._serialized_end=547
  _globals['_CURSOR']._serialized_start=550
  _globals['_CURSOR']._serialized_end=712
  _globals['_LOOKUPPERMISSIONSETSREQUEST']._serialized_start=715
  _globals['_LOOKUPPERMISSIONSETSREQUEST']._serialized_end=871
  _globals['_LOOKUPPERMISSIONSETSRESPONSE']._serialized_start=874
  _globals['_LOOKUPPERMISSIONSETSRESPONSE']._serialized_end=1037
  _globals['_PERMISSIONSETCHANGE']._serialized_start=1040
  _globals['_PERMISSIONSETCHANGE']._serialized_end=1548
  _globals['_PERMISSIONSETCHANGE_SETOPERATION']._serialized_start=1442
  _globals['_PERMISSIONSETCHANGE_SETOPERATION']._serialized_end=1539
  _globals['_SETREFERENCE']._serialized_start=1551
  _globals['_SETREFERENCE']._serialized_end=1681
  _globals['_MEMBERREFERENCE']._serialized_start=1684
  _globals['_MEMBERREFERENCE']._serialized_end=1834
  _globals['_LOOKUPPERMISSIONSETSREQUIRED']._serialized_start=1836
  _globals['_LOOKUPPERMISSIONSETSREQUIRED']._serialized_end=1938
  _globals['_WATCHPERMISSIONSETSSERVICE']._serialized_start=1941
  _globals['_WATCHPERMISSIONSETSSERVICE']._serialized_end=2254
# @@protoc_insertion_point(module_scope)