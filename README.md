# Qwen Image 2512 — Spark AI Hub

[![CI](https://github.com/hitechcloudvn/qwen-image-2512-spark-ai-hub/actions/workflows/ci.yml/badge.svg)](https://github.com/hitechcloudvn/qwen-image-2512-spark-ai-hub/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/hitechcloudvn/qwen-image-2512-spark-ai-hub)](https://github.com/hitechcloudvn/qwen-image-2512-spark-ai-hub/releases)
[![GHCR](https://img.shields.io/badge/GHCR-qwen--image--2512--spark--ai--hub-blue)](https://github.com/hitechcloudvn/qwen-image-2512-spark-ai-hub/pkgs/container/qwen-image-2512-spark-ai-hub)

**Tiếng Việt** · [English](#english)

> Bộ đóng gói mỏng (thin container wrapper) chạy Gradio UI cho mô hình chính thức
> [`Qwen/Qwen-Image-2512`](https://huggingface.co/Qwen/Qwen-Image-2512) trên **NVIDIA DGX Spark** —
> một phần của hệ sinh thái **Spark AI Hub**.

---

## Tiếng Việt

### Mục tiêu

- Không build Docker trực tiếp trên thiết bị trong quá trình cài đặt Spark AI Hub.
- Ảnh `linux/arm64` với CUDA 13 tương thích NVIDIA DGX Spark (GB10).
- Mô hình được tải xuống và lưu trong Docker volume lúc chạy.

### Thành phần

- Cài wheel PyTorch tương thích CUDA 13 cho ARM64.
- Cài runtime dựa trên diffusers cần thiết cho Qwen Image.
- Chạy ứng dụng Gradio nhỏ để tạo ảnh từ lời nhắc (prompt).

### Chạy nhanh

```bash
docker run --gpus all -p 7860:7860 \
  -v qwen-image-2512-output:/data/output \
  -v qwen-image-2512-hf-cache:/root/.cache/huggingface \
  ghcr.io/hitechcloudvn/qwen-image-2512-spark-ai-hub:latest
```

Lần khởi động đầu tiên sẽ tải mô hình vào volume, vì vậy có thể hơi lâu.
Mở giao diện tại `http://<host>:7860`.

### Biến môi trường

| Biến | Mặc định | Mô tả |
| --- | --- | --- |
| `MODEL_ID` | `Qwen/Qwen-Image-2512` | ID mô hình trên Hugging Face |
| `OUTPUT_DIR` | `/data/output` | Thư mục lưu ảnh kết quả |
| `PORT` | `7860` | Cổng Gradio |
| `ENABLE_CPU_OFFLOAD` | `0` | `1` = offload mô hình sang CPU (tiết kiệm VRAM) |

### Kho mã & hình ảnh

- GitHub: <https://github.com/hitechcloudvn/qwen-image-2512-spark-ai-hub>
- GitLab: <https://gitlab.com/hitechcloudvn/qwen-image-2512-spark-ai-hub>
- Ảnh container (GHCR): `ghcr.io/hitechcloudvn/qwen-image-2512-spark-ai-hub`
- Releases: <https://github.com/hitechcloudvn/qwen-image-2512-spark-ai-hub/releases>

### Tài liệu

- [Kiến trúc / Architecture](docs/architecture.md)
- [Triển khai / Deployment](docs/deployment.md)
- [Phát hành / Releasing](docs/releasing.md)
- [Đóng góp / Contributing](CONTRIBUTING.md)
- [Nhật ký thay đổi / Changelog](CHANGELOG.md)

---

## English

> Thin container wrapper running a Gradio UI around the official
> [`Qwen/Qwen-Image-2512`](https://huggingface.co/Qwen/Qwen-Image-2512) model on **NVIDIA DGX Spark** —
> part of the **Spark AI Hub** ecosystem.

### Goals

- No on-device Docker build during the Spark AI Hub install.
- `linux/arm64` CUDA 13 image compatible with NVIDIA DGX Spark (GB10).
- The model is downloaded and stored in Docker volumes at runtime.

### Components

- Installs the CUDA 13-compatible ARM64 PyTorch wheels.
- Installs the minimal diffusers-based runtime needed for Qwen Image.
- Runs a small Gradio app for text-to-image generation.

### Quick start

```bash
docker run --gpus all -p 7860:7860 \
  -v qwen-image-2512-output:/data/output \
  -v qwen-image-2512-hf-cache:/root/.cache/huggingface \
  ghcr.io/hitechcloudvn/qwen-image-2512-spark-ai-hub:latest
```

First launch downloads the model into the volume, so initial startup can take a while.
Open the UI at `http://<host>:7860`.

### Environment variables

| Variable | Default | Description |
| --- | --- | --- |
| `MODEL_ID` | `Qwen/Qwen-Image-2512` | Hugging Face model ID |
| `OUTPUT_DIR` | `/data/output` | Directory for generated images |
| `PORT` | `7860` | Gradio port |
| `ENABLE_CPU_OFFLOAD` | `0` | `1` = offload model to CPU (saves VRAM) |

### Repositories & images

- GitHub: <https://github.com/hitechcloudvn/qwen-image-2512-spark-ai-hub>
- GitLab: <https://gitlab.com/hitechcloudvn/qwen-image-2512-spark-ai-hub>
- Container image (GHCR): `ghcr.io/hitechcloudvn/qwen-image-2512-spark-ai-hub`
- Releases: <https://github.com/hitechcloudvn/qwen-image-2512-spark-ai-hub/releases>

### Documentation

- [Architecture / Kiến trúc](docs/architecture.md)
- [Deployment / Triển khai](docs/deployment.md)
- [Releasing / Phát hành](docs/releasing.md)
- [Contributing / Đóng góp](CONTRIBUTING.md)
- [Changelog / Nhật ký thay đổi](CHANGELOG.md)
