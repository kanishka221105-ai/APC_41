# Asymmetric Grid Subplots
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 2, 3)
ax3 = fig.add_subplot(2, 2, 4)
ax1.plot([1, 2, 3], [1, 2, 3])
ax2.scatter([1, 2, 3], [3, 2, 1])
ax3.bar(['X', 'Y'], [4, 7])
plt.show()