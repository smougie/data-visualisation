import pygal

from dice import Dice

# Utworzenie kości typu D6
dice = Dice()

# Wykonanie określonej liczby rzutów i umieszczenie wyników na liście.
results = []
for roll_value in range(1000):
    result = dice.roll()
    results.append(result)

# Analiza wyników.
frequencies = []  # Pusta lista utworzona do przechowywania częstotliwości wystąpień wartości.
for value in range(1, dice.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Wizualizacja wyników.
hist = pygal.Bar()  # Wygenerowanie wykresu tworząc egzemplarz klasy Bar.
hist.force_uri_protocol = 'http'

hist.title = 'Wynik rzucania pojedyńczą kościa D6 tysiąc razy.'
hist.x_labels = ['1', '2', '3', '4', '5', '6']  # Etykiety osi x
hist.x_title = 'Wynik'  # Tytuł osi x
hist.y_title = 'Częstotliwość występowania wartości'  # Tytuł osi y

hist.add('D6', frequencies)  # Dodajemy serię wartości do wykresu, etytkieta dla każdego zbioru oraz listę wartości
hist.render_to_file('dice_visual.svg')
