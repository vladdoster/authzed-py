"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class RelationTuple(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    OBJECT_AND_RELATION_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int

    @property
    def object_and_relation(self) -> global___ObjectAndRelation: ...

    @property
    def user(self) -> global___User: ...

    def __init__(self,
        *,
        object_and_relation : typing.Optional[global___ObjectAndRelation] = ...,
        user : typing.Optional[global___User] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"object_and_relation",b"object_and_relation",u"user",b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"object_and_relation",b"object_and_relation",u"user",b"user"]) -> None: ...
global___RelationTuple = RelationTuple

class ObjectAndRelation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAMESPACE_FIELD_NUMBER: builtins.int
    OBJECT_ID_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    namespace: typing.Text = ...
    object_id: typing.Text = ...
    relation: typing.Text = ...

    def __init__(self,
        *,
        namespace : typing.Text = ...,
        object_id : typing.Text = ...,
        relation : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"namespace",b"namespace",u"object_id",b"object_id",u"relation",b"relation"]) -> None: ...
global___ObjectAndRelation = ObjectAndRelation

class RelationReference(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAMESPACE_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    namespace: typing.Text = ...
    relation: typing.Text = ...

    def __init__(self,
        *,
        namespace : typing.Text = ...,
        relation : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"namespace",b"namespace",u"relation",b"relation"]) -> None: ...
global___RelationReference = RelationReference

class User(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    USERSET_FIELD_NUMBER: builtins.int

    @property
    def userset(self) -> global___ObjectAndRelation: ...

    def __init__(self,
        *,
        userset : typing.Optional[global___ObjectAndRelation] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"user_oneof",b"user_oneof",u"userset",b"userset"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"user_oneof",b"user_oneof",u"userset",b"userset"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"user_oneof",b"user_oneof"]) -> typing.Optional[typing_extensions.Literal["userset"]]: ...
global___User = User

class Zookie(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TOKEN_FIELD_NUMBER: builtins.int
    token: typing.Text = ...

    def __init__(self,
        *,
        token : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"token",b"token"]) -> None: ...
global___Zookie = Zookie

class RelationTupleUpdate(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Operation(metaclass=_Operation):
        V = typing.NewType('V', builtins.int)

    UNKNOWN = RelationTupleUpdate.Operation.V(0)
    CREATE = RelationTupleUpdate.Operation.V(1)
    TOUCH = RelationTupleUpdate.Operation.V(2)
    DELETE = RelationTupleUpdate.Operation.V(3)

    class _Operation(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Operation.V], builtins.type):  # type: ignore
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNKNOWN = RelationTupleUpdate.Operation.V(0)
        CREATE = RelationTupleUpdate.Operation.V(1)
        TOUCH = RelationTupleUpdate.Operation.V(2)
        DELETE = RelationTupleUpdate.Operation.V(3)

    OPERATION_FIELD_NUMBER: builtins.int
    TUPLE_FIELD_NUMBER: builtins.int
    operation: global___RelationTupleUpdate.Operation.V = ...

    @property
    def tuple(self) -> global___RelationTuple: ...

    def __init__(self,
        *,
        operation : global___RelationTupleUpdate.Operation.V = ...,
        tuple : typing.Optional[global___RelationTuple] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"tuple",b"tuple"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"operation",b"operation",u"tuple",b"tuple"]) -> None: ...
global___RelationTupleUpdate = RelationTupleUpdate

class RelationTupleTreeNode(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    INTERMEDIATE_NODE_FIELD_NUMBER: builtins.int
    LEAF_NODE_FIELD_NUMBER: builtins.int
    EXPANDED_FIELD_NUMBER: builtins.int

    @property
    def intermediate_node(self) -> global___SetOperationUserset: ...

    @property
    def leaf_node(self) -> global___DirectUserset: ...

    @property
    def expanded(self) -> global___ObjectAndRelation: ...

    def __init__(self,
        *,
        intermediate_node : typing.Optional[global___SetOperationUserset] = ...,
        leaf_node : typing.Optional[global___DirectUserset] = ...,
        expanded : typing.Optional[global___ObjectAndRelation] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"expanded",b"expanded",u"intermediate_node",b"intermediate_node",u"leaf_node",b"leaf_node",u"node_type",b"node_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"expanded",b"expanded",u"intermediate_node",b"intermediate_node",u"leaf_node",b"leaf_node",u"node_type",b"node_type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"node_type",b"node_type"]) -> typing.Optional[typing_extensions.Literal["intermediate_node","leaf_node"]]: ...
global___RelationTupleTreeNode = RelationTupleTreeNode

class SetOperationUserset(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Operation(metaclass=_Operation):
        V = typing.NewType('V', builtins.int)

    INVALID = SetOperationUserset.Operation.V(0)
    UNION = SetOperationUserset.Operation.V(1)
    INTERSECTION = SetOperationUserset.Operation.V(2)
    EXCLUSION = SetOperationUserset.Operation.V(3)

    class _Operation(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Operation.V], builtins.type):  # type: ignore
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        INVALID = SetOperationUserset.Operation.V(0)
        UNION = SetOperationUserset.Operation.V(1)
        INTERSECTION = SetOperationUserset.Operation.V(2)
        EXCLUSION = SetOperationUserset.Operation.V(3)

    OPERATION_FIELD_NUMBER: builtins.int
    CHILD_NODES_FIELD_NUMBER: builtins.int
    operation: global___SetOperationUserset.Operation.V = ...

    @property
    def child_nodes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RelationTupleTreeNode]: ...

    def __init__(self,
        *,
        operation : global___SetOperationUserset.Operation.V = ...,
        child_nodes : typing.Optional[typing.Iterable[global___RelationTupleTreeNode]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"child_nodes",b"child_nodes",u"operation",b"operation"]) -> None: ...
global___SetOperationUserset = SetOperationUserset

class DirectUserset(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    USERS_FIELD_NUMBER: builtins.int

    @property
    def users(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___User]: ...

    def __init__(self,
        *,
        users : typing.Optional[typing.Iterable[global___User]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"users",b"users"]) -> None: ...
global___DirectUserset = DirectUserset
