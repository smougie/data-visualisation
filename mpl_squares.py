import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
input_values = list(range(1,6))
plt.plot(input_values, squares, linewidth=5)

# Zdefiniowanie tytułu wykresu i etykiet osi.
plt.title('Kwadraty liczb', fontsize=24)
plt.xlabel('Indeks', fontsize=14)
plt.ylabel('Wartość indeksu', fontsize=14)

# Zdefiniowanie wielkości etykiet.
plt.tick_params(axis='both', labelsize=14)

plt.show()
