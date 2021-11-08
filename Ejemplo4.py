lista = []
while True:
    n = int(input("Ingresa un numero"))
    if n <= 0:
        break
    lista.append(n)
print(sorted(lista))


