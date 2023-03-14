from dataclasses import dataclass
from execute import test_formula

@dataclass
class SequenceTerm:
    index: int
    value: float


def create_formula(sequence:list)-> str:
<<<<<<< HEAD
    result = ""
    for i in range(1,len(sequence)+1):
        nullifier = [f"*(n-{j+1})" for j in range(i)].join("") # all the (n-1)(n-2)... 
        coef = (sequence[i-1]-test_formula(result,i))/(test_formula(nullifier,i)# the coeficient of the nullifier
        result = f"{value}{nullifier}+{result}"
    return result
                                                       
=======
    formula = ""

    for term_index, term_value in enumerate(sequence, start=1):
        next_term = SequenceTerm(index=term_index, value=term_value)

        formula = update_existing_formula_with_next_term(formula, next_term)

    return formula


def update_existing_formula_with_next_term(formula: str, next_term: SequenceTerm) -> str:
    if next_term.index == 1:
        return str(next_term.value)

    nullifier = "".join([
        f"(n-{i})" for i in range(1, next_term.index)
    ]) # all the (n-1)(n-2)...

    # the coeficient of the nullifier is where all the magic resides
    coef = (
        next_term.value - test_formula(formula,next_term.index)
    ) / test_formula(nullifier, next_term.index)

    return f"{coef}*{nullifier}+{formula}"




>>>>>>> bfa2ec2 (First working version)
