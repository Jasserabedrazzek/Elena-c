def Type(name: str) -> str:
    Types_algo = ["entier", "reel", "rèel", "chaine", "chaine de caractère", "caractère", "caractere", "booleen", "booléen"]
    Types_C = ["int", "float", "float", "char", "char", "char", "char", "int", "int"]
    name = name.lower().strip()
    if name in Types_algo:
        return Types_C[Types_algo.index(name)]
    else:
        return False