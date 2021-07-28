
def car_rent_cost(nr_km):
    fixed_cost = 100
    cost_per_km = 0.5
    return fixed_cost + nr_km * cost_per_km

def car_rent_cost(nr_km, fixed_cost=100, cost_per_km=0.5):
    return fixed_cost + nr_km * cost_per_km

print(car_rent_cost(500))  # 350.0
print(car_rent_cost(500, 70))  # 280.0
print(car_rent_cost(500, 70, 0.4))  # 230.0
print(car_rent_cost(500, cost_per_km=0.25))  # 225.0

print(car_rent_cost(cost_per_km=0.25, fixed_cost=100, nr_km=500))  # 225.0
print(car_rent_cost(cost_per_km=0.25, nr_km=500))  # 225.0

print(car_rent_cost(cost_per_km=0.25))
# TypeError: car_rent_cost() missing 1 required positional argument: 'nr_km'
