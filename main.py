import gradio as gr
from huggingface_hub import InferenceClient
from PIL import Image, ImageDraw, ImageFont
import json
import uuid


HF_TOKEN="Your TOKEN"
MODEL_ID = "stabilityai/stable-diffusion-xl-base-1.0"
client = InferenceClient(model=MODEL_ID, token=HF_TOKEN)
history = []


def platform_template(product, platform):
    if platform == "LinkedIn":
        return f"""
        professional advertisement of {product},
        clean background, minimal design,
        corporate style, subtle colors
        """

    elif platform == "Instagram":
        return f"""
        vibrant trendy advertisement of {product},
        colorful background, aesthetic style,
        eye-catching, modern social media vibe
        """


def refine_prompt(user_input, platform):
    base = platform_template(user_input, platform)

    enhanced = f"""
    {base},
    cinematic lighting, depth of field,
    ultra detailed, 8k, high-end photography
    """

    return enhanced

def generate_copy(product, tone):
    if tone == "Professional":
        return f"Experience unmatched quality with our {product}."

    elif tone == "Witty":
        return f"{product} so stylish, even your old ones are jealous."

    elif tone == "Urgent":
        return f"Hurry! Limited stock on {product} – grab yours now!"

    return f"Premium {product}"

def generate_multiple_images(prompt, num_images=3):
    images = []

    for _ in range(num_images):
        img = client.text_to_image(prompt)
        images.append(img)

    return images

def create_ad(image, text):
    img = image.convert("RGB")
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except:
        font = ImageFont.load_default()

    x, y = 30, img.height - 100
    text_width = draw.textlength(text, font=font)
    draw.rectangle([x - 10, y - 10, x + text_width + 20, y + 50], fill="black")
    draw.text((x, y), text, fill="white", font=font)

    return img


def generate_ad(user_input, tone, platform):

    prompt = refine_prompt(user_input, platform)
    copy = generate_copy(user_input, tone)
    images = generate_multiple_images(prompt, 3)
    final_images = []

    image_urls = []

    for img in images:
        final = create_ad(img, copy)

        final_images.append(final)

        image_urls.append(f"generated_image_{uuid.uuid4()}")

    response = {
        "product": user_input,
        "platform": platform,
        "tone": tone,
        "prompt": prompt,
        "generated_copy": copy,
        "images": image_urls,
        "num_images": len(final_images)
    }

    history.append(response)

    with open("history.json", "w") as f:
        json.dump(history, f, indent=4)

    print("\nJSON RESPONSE:")
    print(json.dumps(response, indent=4))

    return final_images, json.dumps(response, indent=4)

demo = gr.Interface(
    fn=generate_ad,
    inputs=[
        gr.Textbox(label="Enter Product (e.g., red running shoes)"),
        gr.Dropdown(["Professional", "Witty", "Urgent"], label="Brand Tone"),
        gr.Dropdown(["LinkedIn", "Instagram"], label="Platform")
    ],
    outputs=[
        gr.Gallery(label="Generated Ad Variations"),
        gr.JSON(label="Unified JSON Response")
    ],
    title="ViralGen AI - Multi-Modal Ad Generator",
    description="Generate multiple AI-powered ad variations with image + copy"
)

if __name__ == "__main__":
    demo.launch()