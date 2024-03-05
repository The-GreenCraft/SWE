# Aufgabe 1 (nur zum Ansehen)
# compute 3!
res = 1
for i in range(1, 4):
    res *= i
print(res)

# compute 5!
res = 1
for i in range(1, 6):
    res *= i
print(res)

# Aufgabe 2 (nur zum Ansehen)
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

# Aufgabe 3 (nur zum Ansehen)
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

print(factorial(3))
print(factorial(5))

# Aufgabe 4 (nur zum Ansehen)
def max(a, b):
    if a > b:
        return a
    else:
        return b

print(max(3, 5))
print(max(5, 3))
print(max(int(input()), int(input())))

# Aufgabe 5 (korrigiert)
def max3(a, b, c):
    return max(max(a, b), c)

print(max3(3, 6, 5))

# Aufgabe 6 