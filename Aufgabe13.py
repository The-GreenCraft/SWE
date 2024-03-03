mydict = {"Größe": 180, "Gewicht": 70, "Beruf": "Angestellter"}
print("Dictionary mydict:", mydict)

groesse = mydict["Größe"]
gewicht = mydict["Gewicht"]

bmi = gewicht / ((groesse / 100) ** 2)
print("BMI:", bmi)

dict_laenge = len(mydict)
print("Länge des Dictionaries:", dict_laenge)

mydict["Gewicht"] = 80
neuer_bmi = mydict["Gewicht"] / ((groesse / 100) ** 2)
print("Neuer BMI nach Änderung des Gewichts:", neuer_bmi)

mydict["Name"] = "Borat"
print("Dictionary nach Hinzufügen des Namens:", mydict)

new_dict = {"Größe": 170, "Gewicht": 60, "Beruf": "Taxifahrerin", "Name": "Melissa"}
print("Neues Dictionary neues_dict:", new_dict)

Team = {"mydict": mydict, "neues_dict": new_dict}
print("Dictionary Team:", Team)

print("Dictionary Team:")
for key, value in Team.items():
    print(f"{key}: {value}")
