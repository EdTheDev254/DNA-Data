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
        
        # Convert image to binary data (raw pixel values)
        pixel_data = img.tobytes()
        
        # Convert to a string of 0s and 1s
        binary_data = ''.join(format(byte, '08b') for byte in pixel_data)
        
        print(f"Binary data generated. Length: {len(binary_data)} bits")
        
        # Optional: Show the image
        # img.show()
        
    except Exception as e:
        print(f"Error loading image: {e}")
else:
    print(f"Image not found at {image_path}")
