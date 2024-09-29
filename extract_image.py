import pytesseract
from PIL import Image

img_file = "D:/Projects/python-project/docs/invoices.png"  # Replace with the path to your PDF file

# Open the image file
image = Image.open(img_file)

# Perform OCR on the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print("Extracted Text:")
print(text)
