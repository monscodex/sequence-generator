sequence = input("Insert sequence following this pattern, '1;2;3;4'")
sequence = sequence.split(";")

def compile(S:list)-> str:
    result = ""
    for i in range(1,len(S)+1):
        nullifier = "" # all the (n-1)(n-2)... 
        X = ""# the coeficient of the nullifier
        result = f"{value}*{nullifier}+{result}"
    return result

def execute():
    pass

print(compile(sequence))
