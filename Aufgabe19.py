#Aufgabe 19
import csv
with open("Day-ahead Prices_202201010000-202301010000.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=" ")
    for row in reader:
        print(f", ".join(row)) 