from binomial_solver import binomial_solver
import sympy as sp    

print("----------\n    Enter 1 for Addition (+) -----> (a + b)\u207f \n    Enter 2 for Subtraction (-) -----> (a - b)\u207f\n----------")
operation = input("Select the operation:\n")
value_of_a = input("\nInput the numeric value of each variable of the binomial in the form of (a"+u"\u00B1"+"b)\u207f. \nIf you don't have the numeric value, just input the name of the variable.\n\nValue of a: "  )
value_of_b = input("Value of b: ")
exponet = int(input("\nInput the degree of the binomial:\n"))

polynomial_set = binomial_solver(exponet, value_of_a, value_of_b) 

if operation == "1":
        polynomial = sum(polynomial_set)
if operation == "2":
    polynomial =[]
    for i in range(0, len(polynomial_set), 2):
        if i == len(polynomial_set)-1:
            polynomial.append(polynomial_set[i])
            break
        if i%2 == 0:
            operation = polynomial_set[i]-polynomial_set[i+1]
        else:
            operation = polynomial_set[i]+polynomial_set[i+1]
        polynomial.append(operation)
    polynomial = sum(polynomial)

if isinstance(polynomial, sp.core.add.Add) == True:
    print("\nPolynomial: ")
else:
    print("\nResult: ")

print(polynomial)
