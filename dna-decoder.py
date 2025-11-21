import pdfplumber
import os

def decode_dna_pdf(pdf_path, output_image_path):
    print(f"Decoding {pdf_path}...")
    
    # 1. Extract text from PDF
    full_text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    # Remove header and footer text if they appear in the extraction
                    # Note: This is a simple cleanup. Depending on extraction, 
                    # headers/footers might need more robust removal.
                    # Because it stired me for hours
                    lines = text.split('\n')
                    
                    # Filter out known header/footer lines
                    filtered_lines = []
                    for line in lines:
                        if "CONFIDENTIAL // DNA SEQUENCE DATA" in line:
                            continue
                        if line.strip().startswith("Page ") and len(line.strip()) < 10:
                            continue
                        filtered_lines.append(line)
                        
                    full_text += "".join(filtered_lines)
                    
        # Clean up the text to ensure only A, C, G, T remain
        dna_sequence = "".join(c for c in full_text if c in "ACGT")
        print(f"Extracted DNA Sequence Length: {len(dna_sequence)}")
        
        # 2. Convert DNA to Binary
        dna_to_binary = {
            'A': '00',
            'C': '01',
            'G': '10',
            'T': '11'
        }
        
        binary_string = ""
        for base in dna_sequence:
            binary_string += dna_to_binary[base]
            
        print(f"Recovered Binary Length: {len(binary_string)} bits")
        
        # 3. Convert Binary to Bytes
        # We need to split the binary string into 8-bit chunks
        byte_array = bytearray()
        for i in range(0, len(binary_string), 8):
            byte_chunk = binary_string[i:i+8]
            if len(byte_chunk) == 8:
                byte_val = int(byte_chunk, 2)
                byte_array.append(byte_val)
                
        # 4. Save to Image File
        with open(output_image_path, "wb") as f:
            f.write(byte_array)
            
        print(f"Successfully saved decoded image to {output_image_path}")
        
        # Verify the first byte
        if len(byte_array) > 0:
            print(f"First byte: {hex(byte_array[0])} (Should be 0xff)")
            
    except Exception as e:
        print(f"Error decoding PDF: {e}")

if __name__ == "__main__":
    decode_dna_pdf("dna_sequence.pdf", "decoded_profile.jpg")
