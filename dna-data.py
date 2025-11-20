# DNA Data - Project file

from PIL import Image
import os

# Define the image path
image_path = "profile.jpg"

# Check if file exists
if os.path.exists(image_path):

    try:
        # Read the raw file bytes directly
        with open(image_path, "rb") as f:
            raw_bytes = f.read()
            
        print(f"Successfully read {image_path}")
        print(f"First byte: {hex(raw_bytes[0])} (Should be 0xff for JPEG)")
        
        # Convert raw bytes to a string of 0s and 1s
        binary_data = ''.join(format(byte, '08b') for byte in raw_bytes)
        
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
        
        # Generate PDF
        from fpdf import FPDF
        
        class PDF(FPDF):
            def header(self):
                self.set_font('Courier', 'B', 12)
                self.cell(0, 10, 'CONFIDENTIAL // DNA SEQUENCE DATA', 0, 1, 'C')
                self.ln(10)
                
            def footer(self):
                self.set_y(-15)
                self.set_font('Courier', 'I', 8)
                self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
                
        pdf = PDF()
        pdf.add_page()
        pdf.set_font("Courier", size=10)
        pdf.multi_cell(0, 5, dna_string)
        
        output_filename = "dna_sequence.pdf"
        pdf.output(output_filename)
        print(f"PDF generated successfully: {output_filename}")
        
    except Exception as e:
        print(f"Error: {e}")
else:
    print(f"Image not found at {image_path}")
