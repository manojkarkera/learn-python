import pdfplumber
import re
def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        first_page = pdf.pages[0]  # Access the first page
        text = first_page.extract_text()
        print(text)
        invoice_match = re.search(r'Invoice\s+Number:\s*#(\d+)', text)
        if invoice_match:
                invoice_number = invoice_match.group(1)
                return invoice_number
    return None

# Example usage:
pdf_file = "D:/Projects/python-project/docs/invoicesample.pdf"  # Replace with the path to your PDF file
pdf_file = "D:/Projects/python-project/docs/NSDLe-CAS_107508039_APR_2024_1.PDF"  # Replace with the path to your PDF file


text = extract_text_from_pdf(pdf_file)
print("Text extracted from PDF:")
print(text)
