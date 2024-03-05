import time
print('Hallo!')
time.sleep(1)
x = input("Wie heißt du? : ")
print("Hallo, " + x + "!")
time.sleep(1)
y = input("Wie kann ich dir heute helfen? : ")
print("Leider kann ich diese Frage nicht beantworten :(")
print("Ich kann dir aber die Fläche deines Wohnzimmers ausrechnen ^^")
print("Wie breit ist dein Wohnzimmer?")
a = float(input())
print("Wie lang ist dein Wohnzimmer?")
b = float(input())
z = a*b
txt = "Dein Wohnzimmer hat eine Fläche von {}"
print(txt.format(z))
time.sleep(1)
print("Ich bin jetzt müde und gehe offline. Bis später!")