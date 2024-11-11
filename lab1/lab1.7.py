import random

fuel_consumption = float(input("Enter the car's average fuel consumption (L/100 km): "))


fuel_price_per_liter = 6.5


distance = random.randint(50, 500)


expected_fuel_needed = (distance * fuel_consumption) / 100


trip_cost = expected_fuel_needed * fuel_price_per_liter


print(f"\nDistance: {distance} km")
print(f"Expected fuel consumption: {expected_fuel_needed:.2f} liters")
print(f"Estimated trip cost: {trip_cost:.2f} PLN")
