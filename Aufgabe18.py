import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 1.
salary = [1562, 2554, 2199, 4764, 4455, 2588, 4206, 1906, 2797, 3699, 1706, 3267, 3471, 3121, 3565, 2706, 2430, 1717, 4581, 1572]

# 2.
education = [9, 14, 12, 20, 19, 15, 21, 10, 17, 18, 16, 18, 16, 17, 15, 13, 10, 9, 22, 9]

# 3.
plt.figure()
plt.hist(education, bins=10, color='skyblue', edgecolor='black')
plt.title('Histogramm')
plt.grid(True)
plt.show()

# 4.
plt.figure()
plt.scatter(education, salary, color='red')
plt.title('Scatterplot')
plt.grid(True)

# 5.
slope, intercept, r, p, std_err = stats.linregress(education, salary)
print("slope:", slope)
print("intercept:", intercept)
print("r:", r)
print("p:", p)
print("std_err:", std_err)

# 6.
def regression_line(x):
    return slope * x + intercept

# 7.
plt.plot(education, regression_line(education), color='blue')

# 8.
plt.show()