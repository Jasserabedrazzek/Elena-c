import re
try:
    def remove(text:str) -> str:
        if (len(text)):
            return re.sub(r'\s+', ' ',text).strip()
        else :
            print("The input text is empty.")
except Exception as e:
    print(e)
