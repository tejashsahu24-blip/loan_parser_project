import re

def parse_aadhaar(text):

    aadhaar = re.search(
        r"\d{4}\s\d{4}\s\d{4}",
        text
    )

    return {
        "aadhaar_number":
            aadhaar.group() if aadhaar else ""
    }