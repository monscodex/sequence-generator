def test_formula(formula: str, term_index: int) -> float:
    formula_with_replaced_term_index = formula.replace("n", str(term_index))

    sequence_term = eval(formula_with_replaced_term_index)

    return sequence_term

def verify_formula(formula: str, expected_terms: dict[int, float]) -> bool:
    return all(
        term_value == test_formula(formula, term_index)
        for term_index, term_value in expected_terms.items()
    )
