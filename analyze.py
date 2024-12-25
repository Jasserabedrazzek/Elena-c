from CodeC import *
from random import randint
def analyze_input(Input:str) -> str:
    Lines = Input.strip().split('\n')
    res = []
    r = [];
    for i in range(0, len(Lines)):
        if Lines[i].lower().startswith('fonction'):
            func = Function(Lines[i])
            res.append(func.function_output)
            r.append(func.function_formation)   
            
    return res,r

def Variable(Input:str) -> str:
    va = Variables(Input)
