# Architecture · Kiến trúc

Tiếng Việt · English

## Tiếng Việt

### Tổng quan

`qwen-image-2512-spark-ai-hub` là một **bộ đóng gói mỏng**: một tệp ứng dụng Gradio
(`app.py`) chạy trong container CUDA trên NVIDIA DGX Spark, tải mô hình
[`Qwen/Qwen-Image-2512`](https://huggingface.co/Qwen/Qwen-Image-2512) từ Hugging Face
và phục vụ giao diện web tại cổng 7860.

### Sơ đồ thành phần

```
┌────────────────────────────────────────────────────┐
│  Container (linux/arm64, CUDA 13.0.1, Ubuntu 24.04)│
│                                                    │
│  ┌──────────────┐    ┌──────────────────────────┐  │
│  │  app.py      │───▶│ diffusers                │  │
│  │  (Gradio UI) │    │ DiffusionPipeline        │  │
│  └──────┬───────┘    │ Qwen/Qwen-Image-2512     │  │
│         │            └──────────┬───────────────┘  │
│         ▼                       ▼                  │
│  /data/output (volume)   HF cache (volume)         │
└────────────────────────────────────────────────────┘
```

### Các quyết định chính

- **Nạp pipeline lười (lazy), thread-safe:** mô hình chỉ được nạp một lần khi có yêu cầu
  đầu tiên (hoặc khi khởi động), được bảo vệ bằng `PIPELINE_LOCK`.
- **CUDA-aware:** dùng `torch.bfloat16` trên GPU, tự động fallback sang CPU/float32 khi
  không có GPU; `ENABLE_CPU_OFFLOAD=1` bật offload sang CPU để tiết kiệm VRAM.
- **Ảnh lưu vào volume:** kết quả ghi vào `OUTPUT_DIR` (mặc định `/data/output`) —
  mount volume để giữ ảnh qua các lần khởi động lại.
- **Mô hình cache vào volume:** mount `/root/.cache/huggingface` để không phải tải lại mô hình.

### Phụ thuộc cốt lõi

| Thành phần | Vai trò |
| --- | --- |
| `diffusers` (git main) | `DiffusionPipeline` cho Qwen Image |
| `torch` (cu130) | Suy luận GPU trên DGX Spark |
| `gradio` | Giao diện web |
| `transformers`, `peft`, `torchao`, `accelerate` | Runtime mô hình |

## English

### Overview

`qwen-image-2512-spark-ai-hub` is a **thin container wrapper**: a single Gradio app
(`app.py`) running in a CUDA container on NVIDIA DGX Spark, downloading the
[`Qwen/Qwen-Image-2512`](https://huggingface.co/Qwen/Qwen-Image-2512) model from Hugging Face
and serving a web UI on port 7860.

### Component diagram

```
┌────────────────────────────────────────────────────┐
│  Container (linux/arm64, CUDA 13.0.1, Ubuntu 24.04)│
│                                                    │
│  ┌──────────────┐    ┌──────────────────────────┐  │
│  │  app.py      │───▶│ diffusers                │  │
│  │  (Gradio UI) │    │ DiffusionPipeline        │  │
│  └──────┬───────┘    │ Qwen/Qwen-Image-2512     │  │
│         │            └──────────┬───────────────┘  │
│         ▼                       ▼                  │
│  /data/output (volume)   HF cache (volume)         │
└────────────────────────────────────────────────────┘
```

### Key decisions

- **Lazy, thread-safe pipeline load:** the model is loaded exactly once on first use
  (or at startup), guarded by `PIPELINE_LOCK`.
- **CUDA-aware:** uses `torch.bfloat16` on GPU, falls back to CPU/float32 without a GPU;
  `ENABLE_CPU_OFFLOAD=1` enables CPU offloading to save VRAM.
- **Images saved to volume:** results go to `OUTPUT_DIR` (default `/data/output`) —
  mount a volume to persist images across restarts.
- **Model cached in volume:** mount `/root/.cache/huggingface` to avoid re-downloading the model.

### Core dependencies

| Component | Role |
| --- | --- |
| `diffusers` (git main) | `DiffusionPipeline` for Qwen Image |
| `torch` (cu130) | GPU inference on DGX Spark |
| `gradio` | Web UI |
| `transformers`, `peft`, `torchao`, `accelerate` | Model runtime |
