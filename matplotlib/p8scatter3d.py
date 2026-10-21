#3D scatter plot
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
z = [2, 3, 4, 3, 2]
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z, color='red')
plt.show()