import pygal

from dice import Dice

# Utworzenie kości typu D6
dice_1 = Dice()
dice_2 = Dice()

# Wykonanie określonej liczby rzutów i umieszczenie wyników na liście.
results = []
for roll_value in range(100000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

# Analiza wyników.
frequencies = []  # Pusta lista utworzona do przechowywania częstotliwości wystąpień wartości.
max_result = dice_1.num_sides + dice_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)


# Wizualizacja wyników.
hist = pygal.Bar()  # Wygenerowanie wykresu tworząc egzemplarz klasy Bar.
hist.force_uri_protocol = 'http'

hist.title = 'Wynik rzutu dwiema kośćmi D6 tysiąc razy.'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']  # Etykiety osi x
hist.x_title = 'Wynik'  # Tytuł osi x
hist.y_title = 'Częstotliwość występowania wartości'  # Tytuł osi y

hist.add('D6 + D6', frequencies)  # Dodajemy serię wartości do wykresu, etytkieta dla każdego zbioru oraz listę wartości
hist.render_to_file('multi_dice_visual.svg')
