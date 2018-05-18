FROM nvcr.io/nvidia/tensorflow:18.04-py3

# ========== Install packages ==========
RUN apt-get update
RUN pip3 install grpcio grpcio-tools
CMD ["bash"]
