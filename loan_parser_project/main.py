from fastapi import FastAPI

from parser import extract_text, parse_loan_data

app = FastAPI()

PDF_PATH = "agreements/loan1.pdf"


@app.get("/")
def home():
    return {"message": "Loan Parser API Running"}


@app.get("/loan")
def get_loan():
    text = extract_text(PDF_PATH)
    data = parse_loan_data(text)
    return data

