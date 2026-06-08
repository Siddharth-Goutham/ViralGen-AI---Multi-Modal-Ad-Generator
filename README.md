ViralGen AI - Multi-Modal Ad Generator
An AI-powered Gradio web application that generates platform-specific ad variations, complete with high-quality images and tailored marketing copy.

ViralGen AI takes a simple product description and automatically crafts targeted advertisements. It uses Stable Diffusion XL to generate imagery optimized for specific social media platforms and overlays dynamic ad copy tailored to your brand's tone.

✨ Features
Platform-Specific Imagery: Automatically refines image prompts based on the target platform (e.g., clean and corporate for LinkedIn; vibrant and trendy for Instagram).
Dynamic Copywriting: Generates text copy based on the selected brand tone (Professional, Witty, or Urgent).
Automated Text Overlay: Uses Pillow (PIL) to seamlessly overlay the generated ad copy directly onto the AI-generated images.
Multiple Variations: Generates 3 distinct image variations per request to give you multiple creative options.
JSON Data Logging: Outputs a unified JSON response containing the prompt, generated copy, and metadata in the UI, while saving all generation history locally to history.json.

🛠️ Prerequisites
Before running the application, ensure you have Python installed along with the required libraries.
You will also need a Hugging Face Access Token to use the Stable Diffusion XL model via the Inference API.
Create an account at Hugging Face.
Navigate to your Settings > Access Tokens to generate a token.

🚀 Installation & Setup
1. Clone or download the repository
Ensure the Python script (e.g., app.py) is in your working directory.

2. Install dependencies
Install the required Python packages using pip:

Bash
pip install gradio huggingface_hub Pillow

3. Configure your API Token
Open the Python script and replace the placeholder HF_TOKEN with your actual Hugging Face access token:

Python
# Replace "Your TOKEN" with your actual Hugging Face API key
HF_TOKEN = "hf_your_actual_token_here" 
4. Run the application
Execute the script from your terminal:

Bash
python app.py
The terminal will provide a local URL (usually http://127.0.0.1:7860). Open this link in your web browser to access the Gradio interface.

🖥️ How to Use
Once the Gradio UI is running, follow these steps:

Enter Product: Type a brief description of what you are advertising (e.g., "red running shoes", "sleek coffee maker").
Select Brand Tone: Choose how you want the ad copy to sound (Professional, Witty, or Urgent).
Select Platform: Choose the target social media platform to dictate the visual style (LinkedIn or Instagram).
Generate: Click the Submit button.

Outputs
Generated Ad Variations: A gallery displaying 3 generated images with the marketing copy overlaid in a black text box at the bottom.
Unified JSON Response: A structured JSON object detailing the exact prompt used, the text generated, and local image tracking references.

📂 Project Architecture
platform_template(): Injects platform-specific aesthetic keywords into the base prompt.
refine_prompt(): Enhances the prompt with high-quality photographic keywords (e.g., cinematic lighting, 8k).
generate_copy(): Acts as a simple rule-based engine to generate text based on the chosen tone.
create_ad(): Handles the PIL image processing to draw the text and background box onto the generated image.
history.json: An automatically generated local file that archives the JSON data of every ad generated during your session.
