def add(a, b):
    print("Adding: %d + %d" %(a, b))
    return a + b

def subtract(a, b):
    print("Subtraction: %d - %d" %(a, b))
    return a - b

def multiply(a, b):
    print("Multiply: %d * %d" %(a, b))
    return a * b

def divide(a, b):
    print("Division: %d / %d" %(a, b))
    return a/b


age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq))

print("Here is a puzzle.")

puzzle = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes", puzzle, "Can you do it by hand?")
