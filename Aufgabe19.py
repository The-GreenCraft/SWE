import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def read_csv(filename):
    with open(filename) as csvfile:
        return list(csv.reader(csvfile))

day_ahead_prices = read_csv("Day-ahead Prices_202201010000-202301010000.csv")
total_load = read_csv("Total Load - Day Ahead _ Actual_202201010000-202301010000.csv")


def create_histogram(data, title):
    plt.hist([float(row[0]) for row in data[1:]], bins=20)
    plt.title(title)
    plt.xlabel('Wert')
    plt.ylabel('Häufigkeit')
    plt.show()

create_histogram(day_ahead_prices, 'Day Ahead Preise')
create_histogram(total_load, 'Gesamtladung')


def create_scatterplot(data1, data2, title):
    x = [float(row[0]) for row in data1[1:]]
    y = [float(row[0]) for row in data2[1:]]
    plt.scatter(x, y)
    plt.title(title)
    plt.xlabel('Day Ahead Preise')
    plt.ylabel('Gesamtladung')
    plt.show()

create_scatterplot(day_ahead_prices, total_load, 'Scatterplot: Day Ahead Preise vs. Gesamtladung')


x = np.array([float(row[0]) for row in day_ahead_prices[1:]])
y = np.array([float(row[0]) for row in total_load[1:]])
slope, intercept, _, _, _ = stats.linregress(x, y)

plt.scatter(x, y)
plt.plot(x, slope * x + intercept, color='red')
plt.title('Regressionslinie und Scatterplot')
plt.xlabel('Day Ahead Preise')
plt.ylabel('Gesamtladung')
plt.show()


print("Steigung:", slope)
print("Achsenabschnitt:", intercept)

# NICHT FERTIG !