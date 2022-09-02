# https://docs.nvidia.com/deeplearning/frameworks/pytorch-release-notes
ARG PYTORCH_VERSION=22.04
FROM nvcr.io/nvidia/pytorch:${PYTORCH_VERSION}-py3

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y sudo tree python3-pip libgl1-mesa-glx
    
RUN rm -rf /opt/conda/lib/python3.8/site-packages/cv2

RUN mkdir /app

ARG requirements
RUN echo "$requirements"
RUN echo "$requirements" > /app/requirements.txt
RUN pip install -r /app/requirements.txt --no-cache-dir

ARG dockerfilesh
RUN echo "$dockerfilesh"
RUN echo "$dockerfilesh" > /app/dockerfile.sh
RUN chmod -R 755 /app/dockerfile.sh

ARG passwd
RUN /app/dockerfile.sh "$passwd"

RUN chmod -R 775 /var/lib

RUN mkdir -p /Lion/LR_VISION
WORKDIR /Lion
RUN mkdir /data

RUN python --version && \
    pip --version && \
    pip list | grep torch && \
    python -c "import torch ; print(torch.__version__)"