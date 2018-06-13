import pygal

from dice import Dice

# Utworzenie kości typu D6
dice = Dice()

# Wykonanie określonej liczby rzutów i umieszczenie wyników na liście.
results = [dice.roll() for roll_value in range(1000)]

# Analiza wyników.
# List comprehension odpowiada za iterację poprzez wszystkie możliwe wartości kości, następnie dana wartość znajdująca
# się obecnie w zmiennej value zostaje użyta w metodzie count w celu sprawdzenie ile razy występuje w liście rezultatów.
frequencies = [results.count(value) for value in range(1, dice.num_sides+1)]

# Wizualizacja wyników.
hist = pygal.Bar()  # Wygenerowanie wykresu tworząc egzemplarz klasy Bar.
hist.force_uri_protocol = 'http'

hist.title = 'Wynik rzucania pojedyńczą kościa D6 tysiąc razy.'
hist.x_labels = list(range(1, dice.num_sides+1))  # Etykiety osi x
hist.x_title = 'Wynik'  # Tytuł osi x
hist.y_title = 'Częstotliwość występowania wartości'  # Tytuł osi y

hist.add('D6', frequencies)  # Dodajemy serię wartości do wykresu, etytkieta dla każdego zbioru oraz listę wartości
hist.render_to_file('dice_visual.svg')
