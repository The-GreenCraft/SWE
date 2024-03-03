#1
einkaufsliste = ["Äpfel", "Bananen", "Paprika", "Tomaten", "Linsen"]
print("2. Element der Einkaufsliste:", einkaufsliste[1])
#2
einkaufsliste[0] = "Kiwis"
#3
einkaufsliste.append("Orangen")
#4
einkaufsliste.insert(3, "Zitronen")
#5
einkaufsliste.remove("Tomaten")
#6
print("Negativer Index:", einkaufsliste[-2])
#7
print("Element 2 und 3:", einkaufsliste[1:3])