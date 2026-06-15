import easyocr
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)
reader = easyocr.Reader(['en'])

def extract_text(image_path):

    result = reader.readtext(
        image_path,
        detail=0
    )

    return " ".join(result)