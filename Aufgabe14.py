#1
def check(number):
    if number % 2 == 0:
        return "gerade Zahl!"
    else:
        return "ungerade Zahl!"

result = check(7)
print(result)

#2
def check_p_n_0(number):
    if number > 0:
        return "Die Zahl ist positiv."
    elif number < 0:
        return "Die Zahl ist negativ."
    else:
        return "Die Zahl ist null."

result = check_p_n_0(-8)
print(result)

#3
print("#3")
for i in range(1, 11):
    print(i)

#4
print("#4")
for i in range(2, 21, 2):
    print(i)

#5
n = int(input("Gib eine Zahl ein: "))
for i in range(1, n + 1):
    print(i)

#6
n = 10
sum_result = sum(range(1, n + 1))
print(f"Die Summe der Zahlen von 1 bis {n} ist: {sum_result}")

#7
liste = ["Apfel", "Banane", "Kirsche"]
for element in liste:
    print(element)

#8
text = "SWE"
for char in text:
    print(char)

#9
i = 1
while i <= 10:
    print(i)
    i += 1

#10
i = 2
while i <= 20:
    print(i)
    i += 2

#11
liste = [1, 3, 5, 7, 9]
zahl = 4

found = False
index = 0
while index < len(liste):
    if liste[index] == zahl:
        found = True
        break
    index += 1

if found:
    print(f"Die Zahl {zahl} ist in der Liste vorhanden.")
else:
    print(f"Die Zahl {zahl} ist nicht in der Liste vorhanden.")
