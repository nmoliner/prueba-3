class Polynomial:
    def __init__(self, terms):
        self.terms = terms

    def subtract(self, other):
        result = {}

        for exp in self.terms:
            result[exp] = self.terms[exp]

        for exp in other.terms:
            if exp in result:
                result[exp] -= other.terms[exp]
            else:
                result[exp] = -other.terms[exp]

        return Polynomial({exp: coeff for exp, coeff in result.items() if coeff != 0})

    def divide(self, other):
        quotient = {}
        remainder = dict(self.terms)

        while len(remainder) >= len(other.terms):
            leading_term_result = {max(remainder.keys()) - max(other.terms.keys()): 
                                   max(remainder.values()) / max(other.terms.values())}

            quotient.update(leading_term_result)
            subtracted_poly = {}

            for exp in other.terms:
                subtracted_poly[exp + max(remainder.keys()) - max(other.terms.keys())] = other.terms[exp] * leading_term_result[max(remainder.keys()) - max(other.terms.keys())]

            remainder = Polynomial(remainder).subtract(Polynomial(subtracted_poly)).terms

        return Polynomial(quotient), Polynomial(remainder)

    def remove_term(self, exp):
        if exp in self.terms:
            del self.terms[exp]
        return self.terms

    def term_exists(self, exp):
        return exp in self.terms


# Ejemplo de polinomios
polynomial1 = Polynomial({3: 4, 2: 3, 1: 2, 0: 1})
polynomial2 = Polynomial({2: 2, 1: 1, 0: 1})

# Restar dos polinomios
result_subtraction = polynomial1.subtract(polynomial2)
print("Resta de polinomios:", result_subtraction.terms)

# Dividir dos polinomios
result_division, remainder = polynomial1.divide(polynomial2)
print("División de polinomios:")
print("Cociente:", result_division.terms)
print("Residuo:", remainder.terms)

# Eliminar un término de un polinomio
removed_term_poly = Polynomial(polynomial1.remove_term(2))
print("Polinomio después de eliminar el término:", removed_term_poly.terms)

# Determinar si un término específico existe en un polinomio
term_to_check = 3
exists = polynomial1.term_exists(term_to_check)
print(f"El término de grado {term_to_check} {'sí existe' if exists else 'no existe'} en el polinomio.")

if __name__ == "__main__":
    # Your code here
    pass

