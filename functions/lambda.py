#  Lambda fucntions are anonymous functions defined with the keyword lambda
# Lambda are one liners and can only contain one expression

# Regular function
def square(x):
    return x ** 2

# same function in lambda
square = lambda x: x ** 2

print(square(6))

# Lambda with multiple arguments

add = lambda x, y, z: x + y + z
print(add(1,2,3))

# When to use lambda
# Lambda functions are often used in combination with:

# Higher-Order Functions: Functions that take another function as an argument (e.g., map, filter, sorted).
# Temporary, Inline Operations: Operations where you don't want to define a separate named function.