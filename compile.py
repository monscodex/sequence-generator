sequence = input("Insert sequence following this pattern, '1;2;3;4'")
sequence = sequence.split(";")

def compile(S:list)-> str:
    result = S[0]
    for i in range(1,len(S)):
        nullifier = [f"(n-{j})" for j in range(i)].join("") 
        value = (execute(result)-S[i])/(i-2)
        result = value+"*"+nullifier+f"+{result}"
    return result

def execute():
    pass

