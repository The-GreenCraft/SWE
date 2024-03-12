#pip install numpy
import numpy
import statistics
#pip install matplotlib
import matplotlib.pyplot as plt
#pip install scipy
from scipy import stats

#1)
data = [198, 553, 923, 675, 724, 525, 664, 884, 911, 881, 597, 128, 303, 786, 147, 625, 853, 81, 98, 83, 678, 53, 281, 454, 115, 406, 922, 56, 582, 242, 122, 913, 818, 222, 87, 299, 112, 13, 188, 810, 12, 134, 712, 311, 932, 969, 564, 35, 450, 514, 417, 615, 833, 827, 355, 124, 605, 713, 726, 860, 552, 47, 377, 792, 85, 852, 490, 943, 101, 473, 34, 443, 901, 75, 959, 616, 274, 150, 762, 793, 474, 272, 757, 133, 979, 840, 632, 243, 839, 601, 332, 357, 506, 980, 256, 635, 835, 580, 228, 237]

#2)
mean = numpy.mean(data)
print(mean)

#3)
median = numpy.median(data)

#4)
stdev = numpy.std(data)

#5)
var = numpy.var(data)

#6)
mode = statistics.mode(data)

#7)
