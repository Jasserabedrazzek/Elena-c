from symboles import Symbol
from remove_spaces import remove

def new_input_(Input):
    new_input = "";
    Input = remove(Input)
    for i in range(0, len(Input)):
        if Symbol(Input[i]):
            new_input += " " + Input[i] + " "
        else:
            new_input += Input[i]
    return new_input