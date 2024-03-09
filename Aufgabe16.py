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

# Aufgabe 6 (nur zum Ansehen)
def f():
    print(a)

a = 1
f()

# Aufgabe 7 (nur zum Ansehen)
def f():
    a = 1

f()
print(a)

# Aufgabe 8
def f():
    a = 1
    print(a)

a = 0
print(a)
f()
print(a)

#Aufgabe 9
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

for i in range(1, 6):
    print(factorial(i), ' = ', i, '!', sep='')
    
#Aufgabe 10
def f():
    print(a)
    if False:
        a = 0

a = 1
f()

#Aufgabe 11
def f():
    global a
    a = 1
    print(a)

a = 0
print(a)
f()
print(a)

#Aufgabe 12
def factorial(n):
    global f
    res = 1
    for i in range(2, n + 1):
        res *= i
    f = res

n = int(input())
factorial(n)
print(f)

#Aufgabe 13
# the chunk of code that can be copied from program to program
def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res
# end of the chunk

n = int(input())
f = factorial(n)
print(f)

#Aufgabe 14
a = input()
b = input()

def f(a,b):
    return [a + "th", b + "th"]

n, m = f(a, b)
print(n)
print(m)

#Aufgabe 15
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

#Aufgabe 16 (Gelöst)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def double_factorial(n):
    if n <= 0:
        return 1
    else:
        return n * double_factorial(n - 2)

print(double_factorial(5))

