from concurrent import futures
import time

import grpc

import inference_server_pb2
import inference_server_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class InferenceService(inference_server_pb2_grpc.InferenceServicer):

    def Compute(self, request, context):
        return inference_server_pb2.Output(batch_id=request.batch_id)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inference_server_pb2_grpc.add_InferenceServicer_to_server(InferenceService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
