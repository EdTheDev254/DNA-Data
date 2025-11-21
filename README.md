# 🧬 DNA Data

This is a little project that turns an image into a DNA sequence (A, C, G, T) and creates a PDF with the sequence. Then, it reads that PDF and reconstructs the image.

## How it Works

1.  **Encoding (`dna-data.py`)**:
    *   Reads the raw binary bytes of `profile.jpg`.
    *   Converts those 0s and 1s into DNA bases (`00`=A, `01`=C, `10`=G, `11`=T).
    *   Generates a fancy "CONFIDENTIAL" PDF with the sequence.

2.  **Decoding (`dna-decoder.py`)**:
    *   Reads the `dna_sequence.pdf`.
    *   Ignores the headers/footers (because they stirred me for hours 😅).
    *   Converts the DNA back to binary.
    *   Saves it as `decoded_profile.jpg`.

## Getting Started

First, make sure you have the required libraries:

```bash
pip install fpdf pdfplumber Pillow
```

### To Encode (Image -> DNA PDF)
Drop a file named `profile.jpg` or any other image and change the name, in this folder and run:

```bash
python dna-data.py
```

### To Decode (DNA PDF -> Image)
Run this to get your image back:

```bash
python dna-decoder.py
```

## Why?
I was curious about it
