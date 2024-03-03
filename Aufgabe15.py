#1
def f_print(value):
    print(value)
f_print("Testfunktion")

#2
def add(a, b, c):
    result = a + b + c
    print(f"Die Summe von {a}, {b} und {c} ist: {result}")

add(3, 7, 10)

#3
def hallo():
    name = "name"
    print(f"Hallo {name}!")

hallo()

#4
def f_name(vorname, nachname):
    print(f"Vorname: {vorname} {nachname}")

f_name("M", "noname")

#5
def f_add2(x, y):
    result = x + y
    print(f"Die Summe von {x} und {y} ist: {result}")

f_add2(5, 8)

#6
def f_misc(*args):
    for arg in args:
        print(arg)

f_misc(1, "Hallo", True)

#7
def f_noten(noten):
    durchschnitt = sum(noten) / len(noten)
    print(f"Notendurchschnitt: {durchschnitt}")

f_noten([5, 4, 3, 2, 1])

#8
def callfunction():
    print("Aufgabe 15 SWE")

callfunction()