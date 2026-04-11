import os
import random
from datetime import datetime
from pathlib import Path
from threading import Lock

import gradio as gr
import numpy as np
import torch
from diffusers import DiffusionPipeline


MODEL_ID = os.getenv("MODEL_ID", "Qwen/Qwen-Image-2512")
OUTPUT_DIR = Path(os.getenv("OUTPUT_DIR", "/data/output"))
PORT = int(os.getenv("PORT", "7860"))
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
TORCH_DTYPE = torch.bfloat16 if DEVICE == "cuda" else torch.float32
MAX_SEED = np.iinfo(np.int32).max
PIPELINE = None
PIPELINE_LOCK = Lock()

ASPECT_RATIOS = {
    "1:1 Square": (1328, 1328),
    "16:9 Landscape": (1664, 928),
    "9:16 Portrait": (928, 1664),
    "4:3 Classic": (1472, 1104),
    "3:4 Portrait": (1104, 1472),
    "3:2 Photo": (1584, 1056),
    "2:3 Poster": (1056, 1584),
}


def get_pipeline():
    global PIPELINE
    with PIPELINE_LOCK:
        if PIPELINE is None:
            pipe = DiffusionPipeline.from_pretrained(MODEL_ID, torch_dtype=TORCH_DTYPE)
            pipe.set_progress_bar_config(disable=True)
            if hasattr(pipe, "enable_attention_slicing"):
                pipe.enable_attention_slicing()
            if hasattr(pipe, "enable_vae_slicing"):
                pipe.enable_vae_slicing()
            if DEVICE == "cuda" and os.getenv("ENABLE_CPU_OFFLOAD", "0") == "1":
                pipe.enable_model_cpu_offload()
            else:
                pipe = pipe.to(DEVICE)
            PIPELINE = pipe
    return PIPELINE


def save_image(image, seed):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    path = OUTPUT_DIR / f"qwen-image-2512-{stamp}-seed{seed}.png"
    image.save(path)
    return str(path)


def generate_image(
    prompt,
    negative_prompt,
    aspect_ratio,
    seed,
    randomize_seed,
    num_inference_steps,
    true_cfg_scale,
):
    if not prompt.strip():
        raise gr.Error("Prompt is required.")

    if randomize_seed:
        seed = random.randint(0, MAX_SEED)

    width, height = ASPECT_RATIOS[aspect_ratio]
    generator = torch.Generator(device=DEVICE).manual_seed(int(seed))
    pipe = get_pipeline()

    result = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt or None,
        width=width,
        height=height,
        num_inference_steps=int(num_inference_steps),
        true_cfg_scale=float(true_cfg_scale),
        generator=generator,
    )
    image = result.images[0]
    saved_path = save_image(image, int(seed))
    return image, saved_path, int(seed)


with gr.Blocks(title="Qwen Image 2512") as demo:
    gr.Markdown(
        """
        # Qwen Image 2512
        Latest official Qwen text-to-image model.
        First launch downloads the model into the app volume, so initial startup can take a while.
        """
    )

    with gr.Row():
        with gr.Column():
            prompt = gr.Textbox(
                label="Prompt",
                lines=5,
                value="A cinematic photo of a retro-futurist bookstore on Mars, warm sunlight through domed glass, detailed shelves, realistic textures, subtle dust in the air.",
            )
            negative_prompt = gr.Textbox(
                label="Negative Prompt",
                lines=2,
                value="blurry, low quality, distorted hands, malformed text, extra limbs, oversaturated",
            )
            aspect_ratio = gr.Dropdown(
                choices=list(ASPECT_RATIOS.keys()),
                value="1:1 Square",
                label="Aspect Ratio",
            )
            with gr.Row():
                seed = gr.Slider(0, MAX_SEED, value=42, step=1, label="Seed")
                randomize_seed = gr.Checkbox(value=True, label="Randomize Seed")
            with gr.Row():
                num_inference_steps = gr.Slider(8, 60, value=40, step=1, label="Steps")
                true_cfg_scale = gr.Slider(1.0, 10.0, value=4.0, step=0.1, label="True CFG Scale")
            generate = gr.Button("Generate", variant="primary")

        with gr.Column():
            output_image = gr.Image(label="Generated Image")
            output_file = gr.File(label="Download Image")
            final_seed = gr.Number(label="Final Seed", precision=0)

    generate.click(
        fn=generate_image,
        inputs=[
            prompt,
            negative_prompt,
            aspect_ratio,
            seed,
            randomize_seed,
            num_inference_steps,
            true_cfg_scale,
        ],
        outputs=[output_image, output_file, final_seed],
    )


if __name__ == "__main__":
    get_pipeline()
    demo.queue(default_concurrency_limit=1, max_size=16).launch(
        server_name="0.0.0.0",
        server_port=PORT,
        share=False,
        allowed_paths=[str(OUTPUT_DIR)],
    )
