#6

distance = float(input("Write the distance you plan to travel (km): "))

fuel_consumption = float(input("Write the average fuel consumption (L/100 km): "))

fuel_price = 6.5

fuel_needed = (distance * fuel_consumption) / 100

cost = fuel_needed * fuel_price


print(f"\nExpected fuel consumption: {fuel_needed:.2f} liters")
print(f"Estimated trip cost: {cost:.2f} PLN")