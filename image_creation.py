from diffusers import AutoPipelineForText2Image

pipe = AutoPipelineForText2Image.from_pretrained("stabilityai/sdxl-turbo")
pipe.to("cuda")


def generate_art(prompt):
    return pipe(prompt=prompt, num_inference_steps=4, guidance_scale=0.0, width=320*4, height=232*4).images[0]
