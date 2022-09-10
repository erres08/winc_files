# Do not modify these lines
__winc_id__ = "49bce82ef9cc475ca3146ee15b0259d0"
__human_name__ = "functions"

# Add your code after this line

# Greet Bob
def greet(name):
    return f"Hello, {name}!"


message = greet("Bob")
print(message)

# Add numbers
def add(a, b, c):
    return a + b + c


sum_total = add(5, 3, 2)
print(sum_total)

# Positive
def positive(number):
    return number > 0


boolean = positive(1)
print(boolean)

# Negative
def negative(number2):
    return number2 < 0


boolean2 = negative(0)
print(boolean2)
