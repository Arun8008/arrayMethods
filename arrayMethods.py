bikes=["royal","yamaha","honda","hero"]
cars=["bmw","audi","benz","hundai"]

bikes.append("R15")
print(bikes)

bikes.remove("honda")
print(bikes)

bikes.extend(cars)
print(bikes)

count=bikes.count("hero")
print(count)

bikes.reverse()
print(bikes)

bikes.sort()
print(bikes)

cars.sort()
print(cars)

cars.pop(2)
print(cars)

bikes.index(2)
print(bikes)

cars.insert("kia")
print(cars)