# https://docs.nvidia.com/deeplearning/frameworks/pytorch-release-notes
ARG PYTORCH_VERSION=22.04
FROM nvcr.io/nvidia/pytorch:${PYTORCH_VERSION}-py3

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y sudo tree python3-pip libgl1-mesa-glx ffmpeg

RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh
RUN apt-get install -y git-lfs
    
RUN rm -rf /opt/conda/lib/python3.8/site-packages/cv2

RUN mkdir /app

ARG requirements
RUN echo "$requirements"
RUN echo "$requirements" > /app/requirements.txt
RUN pip install -r /app/requirements.txt --no-cache-dir
RUN pip install pillow --upgrade --no-cache-dir
RUN mim install mmengine
RUN mim install "mmcv>=2.0.1"
RUN mim install "mmdet>=3.1.0"
RUN mim install "mmpose>=1.1.0"
RUN conda install -c pytorch -c nvidia faiss-gpu=1.7.4 mkl=2021

ARG dockerfilesh
RUN echo "$dockerfilesh"
RUN echo "$dockerfilesh" > /app/dockerfile.sh
RUN chmod -R 755 /app/dockerfile.sh

ARG passwd
RUN /app/dockerfile.sh "$passwd"

RUN chmod -R 775 /var/lib

WORKDIR /Lion
RUN mkdir /data

RUN python --version && \
    pip --version && \
    pip list | grep torch && \
    python -c "import torch ; print(torch.__version__)"