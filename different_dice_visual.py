from dice import Dice

import pygal


# Utworzenie dwóch kości typu D6 i D10
dice_1 = Dice()
dice_2 = Dice(10)

# Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście.
results = [(dice_1.roll() + dice_2.roll()) for roll_value in range(50000)]

# Analiza wyników.
# List comprehension odpowiada za iterację poprzez wszystkie możliwe wartości kości, następnie dana wartość znajdująca
# się obecnie w zmiennej value zostaje użyta w metodzie count w celu sprawdzenie ile razy występuje w liście rezultatów.
max_result = dice_1.num_sides + dice_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Wizualizacja wyników.
hist = pygal.Bar()  # Wygenerowanie wykresu tworząc egzemplarz klasy Bar.
hist.force_uri_protocol = 'http'

hist.title = 'Wynik rzutu dwiema kośćmi typu D6 oraz D10.'
hist.x_labels = list(range(2, (dice_1.num_sides + dice_2.num_sides+1)))  # Etykiety osi x
hist.x_title = 'Wynik'  # Tytuł osi x
hist.y_title = 'Częstotliwość występowania wartości'  # Tytuł osi y

hist.add('D6 + D10', frequencies)  # Dodajemy serię wartości do wykresu, etytkieta dla każdego zbioru oraz listę wartości
hist.render_to_file('different_dice_visual.svg')