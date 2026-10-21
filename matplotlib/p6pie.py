#piechart
import matplotlib.pyplot as plt
labels = ['Kolhapur', 'Ichalkaranji', 'Sangli', 'Miraj']
sizes = [40, 30, 20, 10]
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.show()