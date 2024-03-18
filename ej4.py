def subtract_polynomials(poly1, poly2):
    result = {}

    for exp in poly1:
        result[exp] = poly1[exp]

    for exp in poly2:
        if exp in result:
            result[exp] -= poly2[exp]
        else:
            result[exp] = -poly2[exp]

    return {exp: coeff for exp, coeff in result.items() if coeff != 0}


def divide_polynomials(poly1, poly2):
    quotient = {}
    remainder = dict(poly1)

    while len(remainder) >= len(poly2):
        leading_term_result = {max(remainder.keys()) - max(poly2.keys()): 
                               max(remainder.values()) / max(poly2.values())}

        quotient.update(leading_term_result)
        subtracted_poly = {}

        for exp in poly2:
            subtracted_poly[exp + max(remainder.keys()) - max(poly2.keys())] = poly2[exp] * leading_term_result[max(remainder.keys()) - max(poly2.keys())]

        remainder = subtract_polynomials(remainder, subtracted_poly)

    return quotient, remainder


def remove_term(poly, exp):
    if exp in poly:
        del poly[exp]
    return poly


def term_exists(poly, exp):
    return exp in poly


# Ejemplo de polinomios
polynomial1 = {3: 4, 2: 3, 1: 2, 0: 1}
polynomial2 = {2: 2, 1: 1, 0: 1}

# Restar dos polinomios
result_subtraction = subtract_polynomials(polynomial1, polynomial2)
print("Resta de polinomios:", result_subtraction)

# Dividir dos polinomios
result_division, remainder = divide_polynomials(polynomial1, polynomial2)
print("División de polinomios:")
print("Cociente:", result_division)
print("Residuo:", remainder)

# Eliminar un término de un polinomio
removed_term_poly = remove_term(polynomial1, 2)
print("Polinomio después de eliminar el término:", removed_term_poly)

# Determinar si un término específico existe en un polinomio
term_to_check = 3
exists = term_exists(polynomial1, term_to_check)
print(f"El término de grado {term_to_check} {'sí existe' if exists else 'no existe'} en el polinomio.")
