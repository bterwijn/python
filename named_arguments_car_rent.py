
def car_rent_cost(nr_km):
    fixed_cost = 100
    cost_per_km = 0.5
    return fixed_cost + nr_km * cost_per_km

def car_rent_cost(nr_km, fixed_cost = 100, cost_per_km = 0.5):
    return fixed_cost + nr_km * cost_per_km

print(car_rent_cost(500))  # 350.0
print(car_rent_cost(500, 70))  # 320.0
print(car_rent_cost(500, 70, 0.4))  # 270.0
print(car_rent_cost(500, cost_per_km=0.4))  # 300.0

print(car_rent_cost(cost_per_km=0.4, fixed_cost=100, nr_km=500))  # 300.0
print(car_rent_cost(cost_per_km=0.4, nr_km=500))  # 300.0

# print(car_rent_cost(cost_per_km=0.4)) # TypeError: car_rent_cost() missing 1 required positional argument: 'nr_km'
