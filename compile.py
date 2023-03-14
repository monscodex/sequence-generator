def create_formula(sequence:list)-> str:
    result = ""
    for i in range(1,len(sequence)+1):
        nullifier = [f"*(n-{j+1})" for j in range(i)].join("") # all the (n-1)(n-2)... 
        coef = (sequence[i-1]-test_formula(result,i))/(test_formula(nullifier,i)# the coeficient of the nullifier
        result = f"{value}{nullifier}+{result}"
    return result
                                                       
