#horizontal bargraph
import matplotlib.pyplot as plt
categories = ['A', 'B', 'C', 'D']
values = [12, 27, 42, 10]
fig, ax = plt.subplots()
ax.barh(categories, values, color='lavender')
plt.show()