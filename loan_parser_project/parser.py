import pdfplumber
import re


def extract_text(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text


def parse_loan_data(text):

    agreement_no = re.search(
        r"Agreement No[:\s]+(.+)",
        text
    )

    customer_name = re.search(
        r"Customer Name[:\s]+(.+)",
        text
    )

    loan_amount = re.search(
        r"Loan Amount[:\s]+(.+)",
        text
    )

    return {
        "agreement_no":
            agreement_no.group(1).strip()
            if agreement_no else "",

        "customer_name":
            customer_name.group(1).strip()
            if customer_name else "",

        "loan_amount":
            loan_amount.group(1).strip()
            if loan_amount else ""
    }   