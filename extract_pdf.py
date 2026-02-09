import pdfplumber

with pdfplumber.open('images/Company profile.pdf') as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            print(text)