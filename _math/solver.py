from sympy import Eq, latex, solve, symbols


def do_math():
    x = symbols("x")
    equation = latex(Eq(x**2 - 4, 0))
    rs = solve(Eq(x**2 - 4, 0))
    return equation, rs
