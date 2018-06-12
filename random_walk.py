from random import choice

class RandomWalk():
    """Klasa przeznaczona do wygenerowania błądzenia losowego."""

    def __init__(self, num_points=5000):
        """Inicjalizacja atrybutów błądzenia."""
        self.num_points = num_points

        # Punkt początkowy ma współrzędne (0, 0)
        self.y_values = [0]
        self.x_values = [0]

    def get_step(self):
        """Funkcja odpowiedzialna za wygenerowanie losowej wartości kroku"""
        value_direction = choice([1, -1])
        value_distance = choice([0, 1, 2, 3, 4])
        return value_direction * value_distance

    def fill_walk(self):
        """Wygenerowanie wszystkich punktów dla błądzenia losowego."""

        # Wykonywanie kroków aż do chwili osiągnięcia oczekiwanej liczby punktów.
        while len(self.x_values) < self.num_points:
            # Ustalenie kierunku oraz odległości do pokonania w tym kierunku przy pomocy funkcji get_step()
            x_step = self.get_step()
            y_step = self.get_step()

            # Odrzucenie ruchów, które prowadzą donikąd.
            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)