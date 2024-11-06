import random

import sympy
import sympy.polys
import sympy.polys.polytools


class FuncGenerator:
    def _generate_roots(self, n: int = 1, min_value: int = -10, max_value: int = 10):
        roots = []
        for _ in range(n):
            root = random.randint(min_value, max_value)
            roots.append(root)
        return roots

    def generate_polynomial_equation(self, degree: int = 2):
        roots = self._generate_roots(degree)
        x = sympy.symbols("x")
        poly = 1

        for root in roots:
            poly *= x - root

        return (set(roots), sympy.latex(sympy.Eq(sympy.expand(poly), 0)))
