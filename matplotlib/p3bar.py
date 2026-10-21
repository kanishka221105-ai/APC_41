#bar chart
import matplotlib.pyplot as plt
categories = ['A', 'B', 'C', 'D']
values = [10, 29, 5, 25]
fig, ax = plt.subplots()
ax.bar(categories, values, color='beige')
plt.show()