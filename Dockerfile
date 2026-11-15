# Qwen Image 2512 — Spark AI Hub
# Ảnh ARM64 (CUDA 13) cho NVIDIA DGX Spark / ARM64 (CUDA 13) image for NVIDIA DGX Spark
# Tổ chức / Org: hitechcloudvn — GitHub · GitLab
FROM nvcr.io/nvidia/cuda:13.0.1-devel-ubuntu24.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV PIP_PREFER_BINARY=1

# Gói hệ thống cần thiết / Required system packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv python3-dev \
    git curl \
    libglib2.0-0 libgl1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Môi trường ảo Python / Python virtual environment
RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:${PATH}"

# PyTorch (CUDA 13.0) + phụ thuộc runtime Gradio/diffusers
# PyTorch (CUDA 13.0) + Gradio/diffusers runtime dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu130 && \
    pip install --no-cache-dir \
      gradio \
      accelerate \
      transformers \
      safetensors \
      sentencepiece \
      peft \
      kernels \
      torchao==0.11.0 \
      numpy \
      Pillow \
      protobuf \
      "huggingface_hub[hf_xet]" && \
    pip install --no-cache-dir git+https://github.com/huggingface/diffusers.git

# Mã nguồn ứng dụng / Application source code
COPY app.py /app/app.py

# Thư mục kết quả mặc định / Default output directory (volume)
RUN mkdir -p /data/output

# Cổng Gradio / Gradio port
EXPOSE 7860

CMD ["python", "/app/app.py"]
