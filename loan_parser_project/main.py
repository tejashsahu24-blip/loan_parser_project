from fastapi import FastAPI
from parser import extract_text

app = FastAPI()
pdf_path = "agreements/loan1.pdf"

@app.get("/")
def home():
    return {"message": "Loan Parser API Running"}

@app.get("/loan")
def get_loan():
    text = extract_text("agreements/loan1.pdf")

    return {
        "pdf_text": text
    }