# Deployment · Triển khai

Tiếng Việt · English

## Tiếng Việt

### Yêu cầu

- NVIDIA DGX Spark (hoặc máy ARM64 có GPU CUDA 13 tương thích).
- Docker với [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).
- Kết nối mạng để tải mô hình từ Hugging Face ở lần chạy đầu tiên.

### Chạy bằng Docker

```bash
docker run --gpus all -p 7860:7860 \
  -v qwen-image-2512-output:/data/output \
  -v qwen-image-2512-hf-cache:/root/.cache/huggingface \
  ghcr.io/hitechcloudvn/qwen-image-2512-spark-ai-hub:latest
```

Truy cập giao diện tại `http://<host>:7860`.

### Biến môi trường

| Biến | Mặc định | Mô tả |
| --- | --- | --- |
| `MODEL_ID` | `Qwen/Qwen-Image-2512` | ID mô hình trên Hugging Face |
| `OUTPUT_DIR` | `/data/output` | Thư mục lưu ảnh kết quả |
| `PORT` | `7860` | Cổng Gradio |
| `ENABLE_CPU_OFFLOAD` | `0` | `1` = offload mô hình sang CPU (tiết kiệm VRAM) |

Ví dụ:

```bash
docker run --gpus all -p 8080:8080 \
  -e PORT=8080 \
  -e ENABLE_CPU_OFFLOAD=1 \
  -v qwen-image-2512-output:/data/output \
  ghcr.io/hitechcloudvn/qwen-image-2512-spark-ai-hub:latest
```

### Tích hợp Spark AI Hub

Ảnh được Spark AI Hub kéo từ GHCR và khởi động cùng các ứng dụng khác —
không build Docker trên thiết bị trong quá trình cài đặt.

### Khắc phục sự cố

- **Chậm ở lần đầu:** mô hình (~lớn) đang được tải vào volume — hãy kiên nhẫn hoặc xem log container.
- **Hết VRAM:** đặt `ENABLE_CPU_OFFLOAD=1`.
- **Không có GPU:** ứng dụng vẫn chạy ở chế độ CPU (`float32`) nhưng rất chậm.

## English

### Requirements

- NVIDIA DGX Spark (or an ARM64 machine with compatible CUDA 13 GPU).
- Docker with the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).
- Network access to download the model from Hugging Face on first launch.

### Run with Docker

```bash
docker run --gpus all -p 7860:7860 \
  -v qwen-image-2512-output:/data/output \
  -v qwen-image-2512-hf-cache:/root/.cache/huggingface \
  ghcr.io/hitechcloudvn/qwen-image-2512-spark-ai-hub:latest
```

Open the UI at `http://<host>:7860`.

### Environment variables

| Variable | Default | Description |
| --- | --- | --- |
| `MODEL_ID` | `Qwen/Qwen-Image-2512` | Hugging Face model ID |
| `OUTPUT_DIR` | `/data/output` | Directory for generated images |
| `PORT` | `7860` | Gradio port |
| `ENABLE_CPU_OFFLOAD` | `0` | `1` = offload model to CPU (saves VRAM) |

Example:

```bash
docker run --gpus all -p 8080:8080 \
  -e PORT=8080 \
  -e ENABLE_CPU_OFFLOAD=1 \
  -v qwen-image-2512-output:/data/output \
  ghcr.io/hitechcloudvn/qwen-image-2512-spark-ai-hub:latest
```

### Spark AI Hub integration

Spark AI Hub pulls the image from GHCR and starts it alongside the other apps —
no on-device Docker build during installation.

### Troubleshooting

- **Slow on first launch:** the (large) model is being downloaded into the volume —
  wait or watch the container logs.
- **Out of VRAM:** set `ENABLE_CPU_OFFLOAD=1`.
- **No GPU:** the app still runs on CPU (`float32`) but is very slow.
