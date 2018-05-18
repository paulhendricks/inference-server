from __future__ import print_function

import argparse
import grpc

import inference_server_pb2
import inference_server_pb2_grpc


parser = argparse.ArgumentParser(description='Perform inference.')
parser.add_argument('--batch_id', metavar='N', type=int,
                    help='an integer specifying the batch id')


def run(args):
    channel = grpc.insecure_channel('localhost:50051')
    stub = inference_server_pb2_grpc.InferenceStub(channel)
    response = stub.Compute(inference_server_pb2.Input(batch_id=args.batch_id))
    print('Batch ID received: ' + str(response.batch_id))


if __name__ == '__main__':
    args = parser.parse_args()
    run(args)
