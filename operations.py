def add(a, b): # works fine
    return a + b

def subtract(a, b): # works fine
    return a - b

def multiply(a, b): # works fine
    return a * b

def divide(a, b): # works fine
    return a / b  

def power(a, b): # doesn't work for floats or ints
    return a ^ b  

def square_root(x): # doesn't work for negatives
    import math
    return math.sqrt(x)

def average(list):
    return sum(list) / len(list) # works fine

def maximum(list):
    return min(list) # min should be max


if __name__ == "__main__":
    print("start test")

    print(power(25, 0.5)) # power no funciona para floats

    print("end test")

