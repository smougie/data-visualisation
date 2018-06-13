from dice import Dice

import pygal


# Utworzenie dwóch kości typu D6 i D10
dice = Dice(8)


# Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście.
results = [(dice.roll() + dice.roll()) for roll_value in range(2000000)]

# Analiza wyników.
# List comprehension odpowiada za iterację poprzez wszystkie możliwe wartości kości, następnie dana wartość znajdująca
# się obecnie w zmiennej value zostaje użyta w metodzie count w celu sprawdzenie ile razy występuje w liście rezultatów.
max_result = dice.num_sides + dice.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Wizualizacja wyników.
hist = pygal.Bar()  # Wygenerowanie wykresu tworząc egzemplarz klasy Bar.
hist.force_uri_protocol = 'http'

hist.title = 'Wynik rzutu dwiema kośćmi typu D8 dwa miliony razy.'
hist.x_labels = list(range(2, (max_result+1)))  # Etykiety osi x
hist.x_title = 'Wynik'  # Tytuł osi x
hist.y_title = 'Częstotliwość występowania wartości'  # Tytuł osi y

hist.add('D8', frequencies)  # Dodajemy serię wartości do wykresu, etytkieta dla każdego zbioru oraz listę wartości
hist.render_to_file('d8_visual.svg')