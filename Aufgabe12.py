faecher = {"MT", "MTSP", "FG_SWE", "INSY"}
faecher.add("UNF")
faecher.add("BETP")

faecherneu = {"ENG", "DEU", "AMAT"}

faecher.update(faecherneu)

faecher.remove("MTSP")

print(len(faecher))

overlaps = faecher.intersection(faecherneu)


print("faecherneu:")
for subject in faecherneu:
    print(subject)

mt_in_faecher = "MT" in faecher

faecher_2 = faecher.copy()


