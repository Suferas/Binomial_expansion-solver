import sympy as sp

def pascal_triangle(row):
    set_of_start = [1, 0]
    if row == 0:
        return set_of_start
    else:
        for n in range(row):
            set_of_elements = [1]
            for i in range(len(set_of_start)):
                if i == len(set_of_start)-1:
                    set_of_elements.append(set_of_start[i])
                else:
                    set_of_elements.append(set_of_start[i]+set_of_start[i+1])

            set_of_start = [j for j in set_of_elements]
 
        return set_of_elements

def binomial_solver(degree, a, b):

    variables = [a, b]

    for i in variables:
        try:
            j = float(i)
        except:
            j = sp.symbols(i)
        variables[variables.index(i)] = j
    
    a, b = variables[0], variables[1]

    operations = pascal_triangle(degree)
    values_of_a = []   
    values_of_b = []
  
    for n in range(degree, -1, -1):
        values_of_a.append(a**n)
    for n in range(degree+1):
        values_of_b.append(b**n)
    
    set_of_values = []

    for i in values_of_a:
        set_of_values.append(i)
        for j in values_of_b:
            if values_of_b.index(j) == values_of_a.index(i):
                set_of_values.append(j)

    set_of_products = []

    for i in range(0, len(set_of_values), 2):
        if i < len(set_of_values)-1:
            product = set_of_values[i]*set_of_values[i+1]
            set_of_products.append(product)

    polynomial_set  = list(map(lambda x, y: x*y, set_of_products, operations))

    return polynomial_set