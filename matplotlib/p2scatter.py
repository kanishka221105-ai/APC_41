#scatter plot
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [2, 3, 5, 7, 11, 13, 17, 19]
fig, ax = plt.subplots()
ax.scatter(x, y, color='red', marker='o')
plt.show()