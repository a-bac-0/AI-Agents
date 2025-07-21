import requests
from instagrapi import Client

# --- Step 1: Save image from URL ---
image_url = "YOUR_IMAGE_URL_HERE"  # Replace with Unsplash or Huggingface image URL
image_path = "generated_image.jpg"
response = requests.get(image_url)
with open(image_path, "wb") as f:
    f.write(response.content)

# --- Step 2: Prepare caption ---
caption = "YOUR_GENERATED_CAPTION_HERE"  # Replace with your generated text

# --- Step 3: Login and post to Instagram ---
username = "YOUR_INSTAGRAM_USERNAME"
password = "YOUR_INSTAGRAM_PASSWORD"

cl = Client()
cl.login(username, password)
cl.photo_upload(image_path, caption)

print("Posted to Instagram!")