from calculator import *

calc = Calculator.Calculator()

a = "exp ( 1 + 2 * 3 )"
print(calc.evaluate_string(a))

a = "1 + 2 + 3 * 4 + 5"
print(calc.evaluate_string(a))

a = "sin 1 * 2"
print(calc.evaluate_string(a))

a = "sin ( 1 * 2 )"
print(calc.evaluate_string(a))

a = "2 - -1"
print(calc.evaluate_string(a))

a = "1 / 2"
print(calc.evaluate_string(a))
