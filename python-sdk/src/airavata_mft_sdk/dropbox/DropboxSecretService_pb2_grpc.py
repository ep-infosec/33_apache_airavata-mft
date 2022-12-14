# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from airavata_mft_sdk.dropbox import DropboxCredential_pb2 as dropbox_dot_DropboxCredential__pb2


class DropboxSecretServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getDropboxSecret = channel.unary_unary(
                '/org.apache.airavata.mft.credential.service.dropbox.DropboxSecretService/getDropboxSecret',
                request_serializer=dropbox_dot_DropboxCredential__pb2.DropboxSecretGetRequest.SerializeToString,
                response_deserializer=dropbox_dot_DropboxCredential__pb2.DropboxSecret.FromString,
                )
        self.createDropboxSecret = channel.unary_unary(
                '/org.apache.airavata.mft.credential.service.dropbox.DropboxSecretService/createDropboxSecret',
                request_serializer=dropbox_dot_DropboxCredential__pb2.DropboxSecretCreateRequest.SerializeToString,
                response_deserializer=dropbox_dot_DropboxCredential__pb2.DropboxSecret.FromString,
                )
        self.updateDropboxSecret = channel.unary_unary(
                '/org.apache.airavata.mft.credential.service.dropbox.DropboxSecretService/updateDropboxSecret',
                request_serializer=dropbox_dot_DropboxCredential__pb2.DropboxSecretUpdateRequest.SerializeToString,
                response_deserializer=dropbox_dot_DropboxCredential__pb2.DropboxSecretUpdateResponse.FromString,
                )
        self.deleteDropboxSecret = channel.unary_unary(
                '/org.apache.airavata.mft.credential.service.dropbox.DropboxSecretService/deleteDropboxSecret',
                request_serializer=dropbox_dot_DropboxCredential__pb2.DropboxSecretDeleteRequest.SerializeToString,
                response_deserializer=dropbox_dot_DropboxCredential__pb2.DropboxSecretDeleteResponse.FromString,
                )


class DropboxSecretServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getDropboxSecret(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createDropboxSecret(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateDropboxSecret(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteDropboxSecret(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DropboxSecretServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getDropboxSecret': grpc.unary_unary_rpc_method_handler(
                    servicer.getDropboxSecret,
                    request_deserializer=dropbox_dot_DropboxCredential__pb2.DropboxSecretGetRequest.FromString,
                    response_serializer=dropbox_dot_DropboxCredential__pb2.DropboxSecret.SerializeToString,
            ),
            'createDropboxSecret': grpc.unary_unary_rpc_method_handler(
                    servicer.createDropboxSecret,
                    request_deserializer=dropbox_dot_DropboxCredential__pb2.DropboxSecretCreateRequest.FromString,
                    response_serializer=dropbox_dot_DropboxCredential__pb2.DropboxSecret.SerializeToString,
            ),
            'updateDropboxSecret': grpc.unary_unary_rpc_method_handler(
                    servicer.updateDropboxSecret,
                    request_deserializer=dropbox_dot_DropboxCredential__pb2.DropboxSecretUpdateRequest.FromString,
                    response_serializer=dropbox_dot_DropboxCredential__pb2.DropboxSecretUpdateResponse.SerializeToString,
            ),
            'deleteDropboxSecret': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteDropboxSecret,
                    request_deserializer=dropbox_dot_DropboxCredential__pb2.DropboxSecretDeleteRequest.FromString,
                    response_serializer=dropbox_dot_DropboxCredential__pb2.DropboxSecretDeleteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'org.apache.airavata.mft.credential.service.dropbox.DropboxSecretService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DropboxSecretService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getDropboxSecret(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.credential.service.dropbox.DropboxSecretService/getDropboxSecret',
            dropbox_dot_DropboxCredential__pb2.DropboxSecretGetRequest.SerializeToString,
            dropbox_dot_DropboxCredential__pb2.DropboxSecret.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def createDropboxSecret(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.credential.service.dropbox.DropboxSecretService/createDropboxSecret',
            dropbox_dot_DropboxCredential__pb2.DropboxSecretCreateRequest.SerializeToString,
            dropbox_dot_DropboxCredential__pb2.DropboxSecret.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateDropboxSecret(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.credential.service.dropbox.DropboxSecretService/updateDropboxSecret',
            dropbox_dot_DropboxCredential__pb2.DropboxSecretUpdateRequest.SerializeToString,
            dropbox_dot_DropboxCredential__pb2.DropboxSecretUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteDropboxSecret(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.credential.service.dropbox.DropboxSecretService/deleteDropboxSecret',
            dropbox_dot_DropboxCredential__pb2.DropboxSecretDeleteRequest.SerializeToString,
            dropbox_dot_DropboxCredential__pb2.DropboxSecretDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
