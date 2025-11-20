# DNA Data - Project file

from PIL import Image
import os

# Define the image path
image_path = "profile.jpg"

# Check if file exists
if os.path.exists(image_path):
    try:
        # Load the image
        img = Image.open(image_path)
        print(f"Successfully loaded {image_path}")
        print(f"Format: {img.format}")
        print(f"Size: {img.size}")
        print(f"Mode: {img.mode}")
        
        # Optional: Show the image
        # img.show()
        
    except Exception as e:
        print(f"Error loading image: {e}")
else:
    print(f"Image not found at {image_path}")
