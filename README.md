# Inference Server

Build the gRPC image from the Dockerfile:

```bash
docker build -t inference_server .
```

Run the server:

```bash
docker run -it --rm -d -u $(id -u):$(id -g) -v $PWD:$PWD -w $PWD inference_server python inference_server/inference_server.py
```

Use the `<docker_id>` that was printed to the screen and run the client:

```bash
docker exec <docker_id> python inference_server/inference_client.py 42
```

Use the following to re-compile the Python protobuff code if necessary:

```bash
docker run -d -u $(id -u):$(id -g) -v $PWD:$PWD -w $PWD inference_server \
  python -m grpc_tools.protoc -I . \
  --python_out=inference_server --grpc_python_out=inference_server inference_server.proto
```
