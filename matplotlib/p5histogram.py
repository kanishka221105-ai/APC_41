#histogram
import matplotlib.pyplot as plt
data = [12, 15, 12, 18, 22, 25, 22, 28, 30, 35, 40, 22, 18, 25]
fig, ax = plt.subplots()
ax.hist(data, bins=5, edgecolor='black')
plt.show()