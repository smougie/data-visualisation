import matplotlib.pyplot as plt

from random_walk import RandomWalk


# Utworzenie pętli która będzie tworzyć kolejne błądzenia losowe dopóki użytkownik nie przerwie pętli wpisując 'n'
while True:
    # Przygotowanie danych błądzenia losowego i wyświetlenie punktów
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Określenie wielkości okna wykresu.
    plt.figure(figsize=(20, 12))

    # Zmienna w której przechowuje listę punktów, które przekażemy do mapowania kolorów.
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, s=1, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none')

    # Podkreślenie pierwszego i ostatniego punktu bładzenia losowego.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Ukrycie osi.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Utworzyć kolejne błądzenie losowe? (t/n): ')
    if keep_running == 'n':
        break