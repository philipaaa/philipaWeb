#!/usr/bin/env python3
"""Extract text from PDF resume"""
import sys
import os

pdf_path = "/Users/philipa/Desktop/philipaWeb/resume.pdf"

# Try different PDF libraries
try:
    import PyPDF2
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        print(text)
        sys.exit(0)
except ImportError:
    pass
except Exception as e:
    print(f"PyPDF2 error: {e}", file=sys.stderr)

try:
    import pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
        print(text)
        sys.exit(0)
except ImportError:
    pass
except Exception as e:
    print(f"pdfplumber error: {e}", file=sys.stderr)

try:
    import pypdf
    with open(pdf_path, 'rb') as file:
        reader = pypdf.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        print(text)
        sys.exit(0)
except ImportError:
    pass
except Exception as e:
    print(f"pypdf error: {e}", file=sys.stderr)

print("No PDF library available. Please install one: pip3 install PyPDF2", file=sys.stderr)
sys.exit(1)
