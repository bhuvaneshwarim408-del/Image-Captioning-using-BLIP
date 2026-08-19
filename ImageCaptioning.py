# Image Captioning using a pretrained BLIP model (Hugging Face)
# BLIP looks at an image and generates a natural language caption describing it.

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load the pretrained processor and model (downloads automatically the first time)
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image_path):
    # Open the image file
    raw_image = Image.open(image_path).convert('RGB')

    # Preprocess the image into the format the model expects
    inputs = processor(raw_image, return_tensors="pt")

    # Generate a caption
    output = model.generate(**inputs, max_new_tokens=50)

    # Decode the output tokens into readable text
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption

def main():
    image_path = "sample.jpg"  # change this to your image filename
    print("Generating caption for:", image_path)

    caption = generate_caption(image_path)
    print("\nGenerated Caption:", caption)

if __name__ == "__main__":
    main()