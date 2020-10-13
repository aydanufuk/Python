from datetime import *

def validate(expDate):
    if expDate > datetime.now().date():
        print("valid")
    else:
        print("expired")

validate(date(2200,12,2))