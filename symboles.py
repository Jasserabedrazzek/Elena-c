def Symbol(s:str) -> bool:
    sym = """(),=:<>#*+-/[]"""
    return s in sym

def Logic(s:str) -> str:
    if s == "vrai":
        return 1
    elif s == "faux":
        return 0
    elif s == "et":
        return '&&'
    elif s == "ou":
        return "||"
    elif s == "div":
        return "/"
    elif s == "mod":
        return "%"
    elif s == 'non':
        return "!"
    else:
        return False
