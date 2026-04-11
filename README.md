# Qwen Image 2512 Spark AI Hub Image

Thin container wrapper for running a Gradio UI around the official `Qwen/Qwen-Image-2512` model on NVIDIA DGX Spark.

Goals:
- no on-device Docker build during Spark AI Hub install
- ARM64 CUDA 13 image suitable for DGX Spark
- model downloads stored in Docker volumes at runtime

This image:
- installs CUDA 13 compatible PyTorch wheels for ARM64
- installs the diffusers-based runtime needed for Qwen Image
- runs a small Gradio app for prompt-based image generation

Model:
- https://huggingface.co/Qwen/Qwen-Image-2512
