import re
import pdfplumber

def extract_text(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text

def parse_loan_data(text):

    # ✅ YAHAN ADD KARO (FIRST LINE INSIDE FUNCTION)
    text = text.replace("\n", " ")

    loan_no = re.search(
        r"Application No\s*[:\-]?\s*([A-Za-z0-9\-]+)",
        text
    )

    name = re.search(
        r"Mr\.?\s+[A-Za-z\s]+",
        text
    )

    address = re.search(
        r"([A-Za-z\s,]+,\s*[A-Za-z\s]+,\s*[A-Za-z\s]+\s*\d{6})",
        text
    )

    return {
        "loan_number": loan_no.group(1).strip() if loan_no else "",
        "name": name.group(0).strip() if name else "",
        "address": address.group(0).strip() if address else ""
    }