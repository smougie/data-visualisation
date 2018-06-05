import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, edgecolors='none', c=y_values, cmap=plt.cm.Wistia, s=40)


plt.title('Sześciany liczb', fontsize=24)
plt.xlabel('Indeks', fontsize=14)
plt.ylabel('Wartość indeksu', fontsize=14)


plt.tick_params(axis='both', which='major', labelsize=14)


plt.show()