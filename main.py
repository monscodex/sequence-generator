# Starts the program, while loop and prompts the user for terms in the formula
# Every time the next term is entered the new formula is calculated and printed.

# The user can then test the formula for all the past values (may be in a visual way??? -> Formula stays still and  the  n  is replaced with its value and dynamically calculated in the formula)

from compile import create_formula

from typing import Callable

# @dataclass
# class InterfaceCommand:
#     description: str
#     executed_function: Callable
#
# COMMANDS = {
#     "next": InterfaceCommand(
#         description="Add next term to the sequence and update formula",
#         executed_function=get_updated_formula_with_next_term,
#     )
# }

def main():
    formula = ""
    terms = []

    while True:
        next_term = get_float_from_input(initial_prompt="Please enter the sequence's next term: ", error_message="You can only type an integer or a floating point number using a dot (Ex: 9 or 3.4)")

        terms.append(next_term)

        formula = create_formula(terms)

        print_raw_formula(formula)


def print_raw_formula(raw_formula: str) -> None:
    print(f"Un = {raw_formula}")
def get_float_from_input(initial_prompt: str, error_message: str) -> float:
    while True:
        raw_input = input(initial_prompt)

        try:
            return float(raw_input)
        except ValueError:
            print(f"ERROR: {error_message}")

if __name__ == "__main__":
    main()
