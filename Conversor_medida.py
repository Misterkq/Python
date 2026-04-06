distancia = float(input("Uma distancia em metros:"))
print(f"a media de {distancia}m corresponde a:")

km = distancia / 1000 
hectometros = distancia / 100
decametros = distancia / 10
decimetros = distancia * 10
centimetros = distancia * 100
milimetros = distancia * 1000

print(f"{km}km")
print(f"{hectometros}hm")
print(f"{decametros}dam")
print(f"{decimetros}dm")
print(f"{centimetros}cm")
print(f"{milimetros}mm")