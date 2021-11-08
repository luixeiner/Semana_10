sueldos = (4567, 5555, 1000, 8888, 1177)

sueldos = sorted(sueldos, reverse=True)

mayor = sueldos[0]
menor = sueldos[len(sueldos)-1]
print(mayor)
print(menor)