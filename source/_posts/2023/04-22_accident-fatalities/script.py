import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def target_func(x, a, b):
    return a * np.exp(-b * x)


df = pd.read_excel(r'遇难.xlsx', sheet_name='Sheet1')
x = []
x1 = np.zeros(500)
x2 = np.zeros(500)

for num in df["遇难人数"]:
    x.append(int(num))
for data in x[:37]:
    x1[data] += 1
for data in x[37:]:
    x2[data] += 1

popt1, pcov1 = curve_fit(f=target_func, xdata=range(500), ydata=x1)
popt2, pcov2 = curve_fit(f=target_func, xdata=range(500), ydata=x2)

plt.figure(figsize=(12, 5))

a = plt.subplot(121)
a.bar(range(500), x1)
y1 = [target_func(i, popt1[0], popt1[1]) for i in range(500)]
plt.plot(range(500), y1)
plt.xlim([0, 50])
# plt.ylim([0, 0.15])
plt.xticks([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
plt.plot([9.5, 9.5], [5, 0], color='orange')
plt.plot([29.5, 29.5], [5, 0], color='red')

b = plt.subplot(122)
b.bar(range(500), x2)
y2 = [target_func(i, popt2[0], popt2[1]) for i in range(500)]
plt.plot(range(500), y2)
plt.xlim([0, 50])
# plt.ylim([0, 0.15])
plt.xticks([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
plt.plot([9.5, 9.5], [17, 0], color='orange')
plt.plot([29.5, 29.5], [17, 0], color='red')
plt.show()