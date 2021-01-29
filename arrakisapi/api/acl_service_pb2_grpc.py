# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from arrakisapi.api import acl_service_pb2 as arrakisapi_dot_api_dot_acl__service__pb2


class ACLServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Read = channel.unary_unary(
                '/ACLService/Read',
                request_serializer=arrakisapi_dot_api_dot_acl__service__pb2.ReadRequest.SerializeToString,
                response_deserializer=arrakisapi_dot_api_dot_acl__service__pb2.ReadResponse.FromString,
                )
        self.Write = channel.unary_unary(
                '/ACLService/Write',
                request_serializer=arrakisapi_dot_api_dot_acl__service__pb2.WriteRequest.SerializeToString,
                response_deserializer=arrakisapi_dot_api_dot_acl__service__pb2.WriteResponse.FromString,
                )
        self.Check = channel.unary_unary(
                '/ACLService/Check',
                request_serializer=arrakisapi_dot_api_dot_acl__service__pb2.CheckRequest.SerializeToString,
                response_deserializer=arrakisapi_dot_api_dot_acl__service__pb2.CheckResponse.FromString,
                )
        self.ContentChangeCheck = channel.unary_unary(
                '/ACLService/ContentChangeCheck',
                request_serializer=arrakisapi_dot_api_dot_acl__service__pb2.ContentChangeCheckRequest.SerializeToString,
                response_deserializer=arrakisapi_dot_api_dot_acl__service__pb2.CheckResponse.FromString,
                )
        self.Expand = channel.unary_unary(
                '/ACLService/Expand',
                request_serializer=arrakisapi_dot_api_dot_acl__service__pb2.ExpandRequest.SerializeToString,
                response_deserializer=arrakisapi_dot_api_dot_acl__service__pb2.ExpandResponse.FromString,
                )


class ACLServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Write(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Check(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ContentChangeCheck(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Expand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ACLServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=arrakisapi_dot_api_dot_acl__service__pb2.ReadRequest.FromString,
                    response_serializer=arrakisapi_dot_api_dot_acl__service__pb2.ReadResponse.SerializeToString,
            ),
            'Write': grpc.unary_unary_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=arrakisapi_dot_api_dot_acl__service__pb2.WriteRequest.FromString,
                    response_serializer=arrakisapi_dot_api_dot_acl__service__pb2.WriteResponse.SerializeToString,
            ),
            'Check': grpc.unary_unary_rpc_method_handler(
                    servicer.Check,
                    request_deserializer=arrakisapi_dot_api_dot_acl__service__pb2.CheckRequest.FromString,
                    response_serializer=arrakisapi_dot_api_dot_acl__service__pb2.CheckResponse.SerializeToString,
            ),
            'ContentChangeCheck': grpc.unary_unary_rpc_method_handler(
                    servicer.ContentChangeCheck,
                    request_deserializer=arrakisapi_dot_api_dot_acl__service__pb2.ContentChangeCheckRequest.FromString,
                    response_serializer=arrakisapi_dot_api_dot_acl__service__pb2.CheckResponse.SerializeToString,
            ),
            'Expand': grpc.unary_unary_rpc_method_handler(
                    servicer.Expand,
                    request_deserializer=arrakisapi_dot_api_dot_acl__service__pb2.ExpandRequest.FromString,
                    response_serializer=arrakisapi_dot_api_dot_acl__service__pb2.ExpandResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ACLService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ACLService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ACLService/Read',
            arrakisapi_dot_api_dot_acl__service__pb2.ReadRequest.SerializeToString,
            arrakisapi_dot_api_dot_acl__service__pb2.ReadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Write(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ACLService/Write',
            arrakisapi_dot_api_dot_acl__service__pb2.WriteRequest.SerializeToString,
            arrakisapi_dot_api_dot_acl__service__pb2.WriteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Check(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ACLService/Check',
            arrakisapi_dot_api_dot_acl__service__pb2.CheckRequest.SerializeToString,
            arrakisapi_dot_api_dot_acl__service__pb2.CheckResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ContentChangeCheck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ACLService/ContentChangeCheck',
            arrakisapi_dot_api_dot_acl__service__pb2.ContentChangeCheckRequest.SerializeToString,
            arrakisapi_dot_api_dot_acl__service__pb2.CheckResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Expand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ACLService/Expand',
            arrakisapi_dot_api_dot_acl__service__pb2.ExpandRequest.SerializeToString,
            arrakisapi_dot_api_dot_acl__service__pb2.ExpandResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
