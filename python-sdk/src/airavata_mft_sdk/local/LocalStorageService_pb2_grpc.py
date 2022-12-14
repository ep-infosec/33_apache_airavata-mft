# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from airavata_mft_sdk.local import LocalStorage_pb2 as local_dot_LocalStorage__pb2


class LocalStorageServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.listLocalStorage = channel.unary_unary(
                '/org.apache.airavata.mft.resource.service.local.LocalStorageService/listLocalStorage',
                request_serializer=local_dot_LocalStorage__pb2.LocalStorageListRequest.SerializeToString,
                response_deserializer=local_dot_LocalStorage__pb2.LocalStorageListResponse.FromString,
                )
        self.getLocalStorage = channel.unary_unary(
                '/org.apache.airavata.mft.resource.service.local.LocalStorageService/getLocalStorage',
                request_serializer=local_dot_LocalStorage__pb2.LocalStorageGetRequest.SerializeToString,
                response_deserializer=local_dot_LocalStorage__pb2.LocalStorage.FromString,
                )
        self.createLocalStorage = channel.unary_unary(
                '/org.apache.airavata.mft.resource.service.local.LocalStorageService/createLocalStorage',
                request_serializer=local_dot_LocalStorage__pb2.LocalStorageCreateRequest.SerializeToString,
                response_deserializer=local_dot_LocalStorage__pb2.LocalStorage.FromString,
                )
        self.updateLocalStorage = channel.unary_unary(
                '/org.apache.airavata.mft.resource.service.local.LocalStorageService/updateLocalStorage',
                request_serializer=local_dot_LocalStorage__pb2.LocalStorageUpdateRequest.SerializeToString,
                response_deserializer=local_dot_LocalStorage__pb2.LocalStorageUpdateResponse.FromString,
                )
        self.deleteLocalStorage = channel.unary_unary(
                '/org.apache.airavata.mft.resource.service.local.LocalStorageService/deleteLocalStorage',
                request_serializer=local_dot_LocalStorage__pb2.LocalStorageDeleteRequest.SerializeToString,
                response_deserializer=local_dot_LocalStorage__pb2.LocalStorageDeleteResponse.FromString,
                )


class LocalStorageServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def listLocalStorage(self, request, context):
        """Storage
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getLocalStorage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createLocalStorage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateLocalStorage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteLocalStorage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LocalStorageServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'listLocalStorage': grpc.unary_unary_rpc_method_handler(
                    servicer.listLocalStorage,
                    request_deserializer=local_dot_LocalStorage__pb2.LocalStorageListRequest.FromString,
                    response_serializer=local_dot_LocalStorage__pb2.LocalStorageListResponse.SerializeToString,
            ),
            'getLocalStorage': grpc.unary_unary_rpc_method_handler(
                    servicer.getLocalStorage,
                    request_deserializer=local_dot_LocalStorage__pb2.LocalStorageGetRequest.FromString,
                    response_serializer=local_dot_LocalStorage__pb2.LocalStorage.SerializeToString,
            ),
            'createLocalStorage': grpc.unary_unary_rpc_method_handler(
                    servicer.createLocalStorage,
                    request_deserializer=local_dot_LocalStorage__pb2.LocalStorageCreateRequest.FromString,
                    response_serializer=local_dot_LocalStorage__pb2.LocalStorage.SerializeToString,
            ),
            'updateLocalStorage': grpc.unary_unary_rpc_method_handler(
                    servicer.updateLocalStorage,
                    request_deserializer=local_dot_LocalStorage__pb2.LocalStorageUpdateRequest.FromString,
                    response_serializer=local_dot_LocalStorage__pb2.LocalStorageUpdateResponse.SerializeToString,
            ),
            'deleteLocalStorage': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteLocalStorage,
                    request_deserializer=local_dot_LocalStorage__pb2.LocalStorageDeleteRequest.FromString,
                    response_serializer=local_dot_LocalStorage__pb2.LocalStorageDeleteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'org.apache.airavata.mft.resource.service.local.LocalStorageService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LocalStorageService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def listLocalStorage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.resource.service.local.LocalStorageService/listLocalStorage',
            local_dot_LocalStorage__pb2.LocalStorageListRequest.SerializeToString,
            local_dot_LocalStorage__pb2.LocalStorageListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getLocalStorage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.resource.service.local.LocalStorageService/getLocalStorage',
            local_dot_LocalStorage__pb2.LocalStorageGetRequest.SerializeToString,
            local_dot_LocalStorage__pb2.LocalStorage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def createLocalStorage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.resource.service.local.LocalStorageService/createLocalStorage',
            local_dot_LocalStorage__pb2.LocalStorageCreateRequest.SerializeToString,
            local_dot_LocalStorage__pb2.LocalStorage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateLocalStorage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.resource.service.local.LocalStorageService/updateLocalStorage',
            local_dot_LocalStorage__pb2.LocalStorageUpdateRequest.SerializeToString,
            local_dot_LocalStorage__pb2.LocalStorageUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteLocalStorage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.resource.service.local.LocalStorageService/deleteLocalStorage',
            local_dot_LocalStorage__pb2.LocalStorageDeleteRequest.SerializeToString,
            local_dot_LocalStorage__pb2.LocalStorageDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
