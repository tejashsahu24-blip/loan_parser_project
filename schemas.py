from pydantic import BaseModel

class LoanAgreement(BaseModel):
    agreement_no: str
    customer_name: str
    loan_amount: float
    emi: float
    tenure: int