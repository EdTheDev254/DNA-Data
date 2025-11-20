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
        
        # DNA Mapping
        binary_to_dna = {
            '00': 'A',
            '01': 'C',
            '10': 'G',
            '11': 'T'
        }
        
        dna_sequence = []
        # Process 2 bits at a time
        for i in range(0, len(binary_data), 2):
            chunk = binary_data[i:i+2]
            if len(chunk) == 2:
                dna_sequence.append(binary_to_dna[chunk])
                
        dna_string = "".join(dna_sequence)
        
        print(f"DNA Sequence generated. Length: {len(dna_string)} bases")
        print(f"Sample (first 100 bases): {dna_string[:100]}...")
        
    except Exception as e:
        print(f"Error loading image: {e}")
else:
    print(f"Image not found at {image_path}")
