import time
import webbrowser

print('Hallo!')
time.sleep(1)
x = input("Wie heißt du? : ")
print("Hallo, " + x + "!")
time.sleep(1)
y = input("Wie kann ich dir heute helfen? : ")
if 'GTA' in y.lower() or 'GTA 6' in y.lower() or 'GTA VI' in y.lower():
    print("Natürlich, hier ist der neuste Trailer zu GTA 6:")
    time.sleep(1)
    webbrowser.open('https://youtu.be/QdBZY2fkU-0?si=fw1pePWz2YNIx-Fg')
elif 'temperatur' in y.lower():

    def fahrenheit_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    def celsius_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    print("Okay, der Temperatur-Umwandler wurde gestartet!")
    t = input("In welcher Einheit ist deine Temperatur? Antworte mit 'C' für Celsius und 'F' für Fahrenheit!")
    if t == "C":
        c = float(input("Okay, gib hier die Temperatur ein:"))
        umgerechnete_temperatur = celsius_fahrenheit(c)
        print("Hier ist deine Temperatur in Fahrenheit: ", umgerechnete_temperatur)
    elif t == "F":
        f = float(input("Okay, gib hier deine Temperatur ein:"))
        umgerechnete_temperatur = fahrenheit_celsius(f)
        print("Hier ist deine Temperatur in Celsius: ", umgerechnete_temperatur)

    else:
        print("Das ist keine gültige Temperatureinheit!")
else:
    print('Entschuldigung, das verstehe ich noch nicht!')

