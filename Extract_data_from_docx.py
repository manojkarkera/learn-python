import re
from docx import Document

def extract_data_from_docx(file_path):
    doc = Document(file_path)
    results = []
    current_name = None
    current_answer = None

    for paragraph in doc.paragraphs:
        text = paragraph.text
        # Check for the presence of 'Name :-' pattern
        name_match = re.search(r'Name\s*:-\s*([\w\s]+)', text)
        if name_match:
            current_name = name_match.group(1).strip()
        # Check for the presence of question-answer pairs
        question_answer_match = re.search(r'Do you have a biometric residence permit\?\s*‘?(Yes|No)’?', text)
        if question_answer_match:
            current_answer = question_answer_match.group(1)
            if current_name and current_answer:
                results.append((current_name, current_answer))
                # Reset name and answer after processing
                current_name = None
                current_answer = None
    
    return results

# Example usage:
file_path = "D:/Projects/python-project/docs/Step 1 - Online Right to Work check.docx"  

print(file_path)

data = extract_data_from_docx(file_path)
print(data)
for name, answer in data:
    print(f"Name: {name}, Answer: {answer}")
