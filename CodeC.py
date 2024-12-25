from symboles import Symbol,Logic
from type_ import Type
from remove_spaces import remove
from lines import Lines
from newInput import new_input_

class Write:
    def __init__(self,Input):
        self.new_input = new_input_(Input)
        self.new_input = remove(self.new_input[self.new_input.find("("):])
        self.new_input = remove(self.new_input[1:])
        self.new_input = remove(self.new_input[:-1])
        self.comma = self.new_input.split(",")
        self.output = []
        if len(self.comma )>0 and len(self.comma) == 1 :
            self.output.clear()
            if '"' in self.comma[0]:
                self.output.append("".join(self.comma))
            else:
                self.output.append('"%t",'+"".join(self.comma))
        else :
            self.output.clear()
            for i in range(0, len(self.comma)):
                if '"' in self.comma[i] :
                    self.output.append(self.comma[i])
                else:
                    self.output.append('"%t",'+(self.comma[i]))
        self.printf = f"""printf({",".join(self.output)});"""
        self.o = "";
        for i in range(len(self.comma)):
            if '"' not in self.comma[i] and "'" not in self.comma[i] :
                self.o += f"""* Assurez-vous de remplacer %t par le type correspondant à `{remove(self.comma[i])}` attendu dans la déclaration ou l'expression.\n"""

class Read:
    def __init__(self, Input):
        self.new_input = new_input_(Input)
        self.new_input = remove(self.new_input[self.new_input.find("("):])
        self.new_input = remove(self.new_input[1:])
        self.new_input = remove(self.new_input[:-1])
        self.comma = self.new_input.split(",")
        res = '';
        for i in range(0, len(self.comma)):
            res += '"%t",&'+ self.comma[i]
        self.scan = f"""scanf({res})"""
        self.o = "";
        for i in range(len(self.comma)):
            if '"' not in self.comma[i] and "'" not in self.comma[i] :
                self.o += f"""* Assurez-vous de remplacer %t par le type correspondant à `{remove(self.comma[i])}` attendu dans la déclaration ou l'expression.\n"""
class Function:
    def __init__(self, input_data):
        try:
            self.input_data = input_data.strip()
            self.new_input_data = ""
            for i in range(len(input_data)):
                if Symbol(input_data[i]):  
                    self.new_input_data += " " + input_data[i] + ' '
                else:
                    self.new_input_data += input_data[i]
            self.space = self.new_input_data.strip().split(" ")
            self.name_of_Function = self.space[1]
            self.parameters = remove(self.new_input_data[self.new_input_data.find("("):self.new_input_data.find(")")+1])
            self.p = self.parameters.split(" ")
            self.TYPES = []
            for i in range(len(self.p)):
                if Type(self.p[i]):
                    self.TYPES.append(f'{Type(self.p[i])} {self.p[i-2]}')
                    print(self.p[i-2])
            self.return_type = Type(self.space[len(self.space)-1])
            self.function_output = f'{self.return_type} {self.name_of_Function}({",".join(self.TYPES)})' 
            self.function_formation = f"""
            * La fonction `{self.name_of_Function}` prend {str(len(self.TYPES)) }  paramètre{'' if len(self.TYPES) == 1 else 's'} qui devraient être des valeurs fournies par l'utilisateur ou une autre partie du programme. 
            Ces paramètres doivent correspondre aux types attendus, à savoir : `{', '.join(self.TYPES)}`. 
            La fonction retourne une valeur de type `{self.return_type}`, qui représente le résultat de l'opération ou du calcul effectué par la fonction. 
            Le corps de la fonction est utilisé pour déclarer des variables locales, effectuer des opérations, et renvoyer la valeur de retour.
            """

        except Exception as e:
            self.error = e;
class Procedure:
    def __init__(self,Input):
        self.newInput = '';
        for i in range(len(Input)):
            if Symbol(Input[i]):
                self.newInput += " " + Input[i] + ' '
            else:
                self.newInput += Input[i]
        self.newInput = remove(self.newInput)
        self.space = self.newInput.split(' ')
        self.name_of_Procedure = self.space[1]
        self.parameters = remove(self.newInput[self.newInput.find("(")+1:self.newInput.find(")")])
        self.p = self.parameters.split(" ")
        self.TYPES = []
        for i in range(len(self.p)):
            if Type(self.p[i]):
                self.TYPES.append(f'{Type(self.p[i])} {self.p[i-2]}') 
        self.procedure_output = f'void {self.name_of_Procedure}({",".join(self.TYPES)})'

class Variables:
    def __init__(self, Input):
        try:
            self.input_data = Lines(Input)
            self.table_name = ''
            self.size = ''
            self.type_ = ''
            self.res = ''
            self.vr = ''
            self.tableau = ''
            for i in range(len(self.input_data)):
                line = self.input_data[i].lower()
                if line.startswith("types") or line.startswith("type"):
                    if i + 1 < len(self.input_data):
                        next_line = self.input_data[i + 1].replace("�", "e")
                        self.spaces = remove(next_line).lower().split(" ")
                        self.table_name = next_line.split(":")[0].strip()
                        dimensions = next_line[next_line.find("["):next_line.find("]") + 1]
                        self.size = dimensions.replace("..", ":")
                        self.type_ = self.spaces[-1]
                        c_type = Type(self.type_)
                        if c_type:
                            self.tableau += f"{c_type} {self.table_name}{self.size};\n"
                        
                
                if ":" in self.input_data[i]:
                    vars_ = self.input_data[i].split(":")
                    self.v = vars_[0].strip()
                    self.t = vars_[1].lower().strip()
                    c_type = Type(self.t)
                    if c_type:
                        self.vr += f"{c_type} {self.v};\n"

        except Exception as e:
            self.error = e

class Condition:
    def __init__(self, Input):
        self.output_logic = ""
        self.output = ""
        self.spaces = remove(Input).split(' ')
        self.remove_spaces = remove(Input)
        self.condition_lists = ['si', 'sinon si', 'sinon']
        self.type_conditions = self.remove_spaces[:self.remove_spaces.find("(")].strip() if "(" in self.remove_spaces else self.remove_spaces.strip()
        if self.type_conditions in self.condition_lists[:2]:
            self.new_input = new_input_(self.remove_spaces[self.remove_spaces.find("(") + 1 : self.remove_spaces.rfind(")")].strip())
            self.struct = self.new_input.split(" ")
            for item in self.struct:
                if Logic(item):
                    self.output_logic += f" {Logic(item)} "
                else:
                    self.output_logic += item
            self.output_logic = self.output_logic.strip()
            if remove(self.type_conditions) == "si":
                self.output = f"if ({self.output_logic})"
            elif remove(self.type_conditions) == "sinon si":
                self.output = f"else if ({self.output_logic})"
        elif remove(self.type_conditions) == "sinon":
            self.output = "else"

class For_loop:
    def __init__(self,Input):
        self.output = ""
        self.newInput = new_input_(Input)
        self.Spaces = remove(self.newInput).split(" ")
        if "[" not in self.Spaces and "]" not in self.Spaces:
            self.output = f"""for({self.Spaces[1]} = {self.Spaces[3]} ; {self.Spaces[1]} < {self.Spaces[5]} ; {self.Spaces[1]}++)"""
        else:
            p1 = 0;
            p2 = 0;
            for i in range(len(self.Spaces)):
                if self.Spaces[i] == "[": 
                    p1 = i
                if self.Spaces[i] == "]": 
                    p2 = i
            self.p = self.Spaces[p1+2:p2]
            self.num = self.p[1:]
            if "-" not in self.num and "*" not in self.num and "/" not in self.num:
                self.output = f"""for({self.Spaces[1]} = {self.Spaces[3]} ; {self.Spaces[1]} < {self.Spaces[5]} ; {self.Spaces[1]}+={self.num[-1]})"""
            else:
                self.output = f"""for({self.Spaces[1]} = {self.Spaces[3]} ; {self.Spaces[1]} < {self.Spaces[5]} ; {self.Spaces[1]}{self.num[-2]}={self.num[-1]})"""

class While_loop:
    def __init__(self,Input):
        self.newInput = new_input_(Input)

text = """jusqu'a ((a>b) et (a<b) ou n mod 2)"""
text1 = """Tant que ((a>b) et (a<b) ou n mod 2) faire""" 

var = While_loop(text)
var1 = While_loop(text1)
# print((var.Spaces))
# print((var1.Spaces)) 
print((var.newInput)) 
print((var1.newInput)) 
# print((var1.num)) 
# print((var))
  
