import csv
import matplotlib.pyplot as plt

with open('Day-ahead Prices_202201010000-202301010000.csv', 'r') as file:
    reader = csv.reader(file)

with open('Total Load - Day Ahead _ Actual_202201010000-202301010000.csv', 'r') as file:
    reader = csv.reader(file)