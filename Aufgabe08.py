einkaufsliste = ["Äpfel", "Bananen", "Paprika", "Tomaten", "Linsen"]

einkaufsliste[einkaufsliste.index("Paprika")] = "Roter Paprika"

einkaufsliste.extend(["Zwiebel", "Spaghetti", "Oregano"])

if "Bananen" in einkaufsliste:
    print("Die Bananen sind auf der Einkaufsliste.")

zutaten = ["Spaghetti", "Salz", "Tomaten", "Oregano"]

fehlendezutaten = [zutat for zutat in zutaten if zutat not in einkaufsliste]

einkaufsliste.extend(fehlendezutaten)

print("Einkaufsliste: ", einkaufsliste)