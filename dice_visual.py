from dice import Dice

dice = Dice()

results = []
for roll_value in range(100):
    result = dice.roll()
    results.append(result)

print(results)