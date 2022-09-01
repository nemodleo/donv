# https://docs.nvidia.com/deeplearning/frameworks/pytorch-release-notes
ARG PYTORCH_VERSION=22.04
FROM nvcr.io/nvidia/pytorch:${PYTORCH_VERSION}-py3

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y sudo tree python3-pip libgl1-mesa-glx
    
RUN rm -rf /opt/conda/lib/python3.8/site-packages/cv2


RUN mkdir /app
COPY docker/dockerfile.sh /app/dockerfile.sh
RUN chmod -R 755 /app/dockerfile.sh

# COPY requirements.txt /app/requirements.txt
# WORKDIR /app
# RUN pip install -r requirements.txt --no-cache-dir
RUN pip install omegaconf h5py pytorch_lightning onnxruntime-gpu==1.8.0 \
                insightface==0.2.1 scikit-image opencv-contrib-python \
                dominate streamlit stqdm streamlit-webrtc Tmlog  slack_async_alert \
                onnx2torch cucim albumentations kornia nvitop tictectoc alert2me --no-cache-dir


# RUN rm -rf /opt/conda/lib/python3.8/site-packages/scipy*
# RUN apt-get install -y libblas-dev liblapack-dev libatlas-base-dev gfortran
# RUN pip install scipy==1.1.0 tensorboard_logger
                

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