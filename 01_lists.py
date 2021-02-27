lista = [
    99,
    29,
    44,
    8,
    12,
    10,
    30,
    45,
    50,
    60
]

# Ordenar
lista.sort()

for elemento in lista:
    print(elemento)

print(f'La longitud de la lista es de {len(lista)} elementos')

# REmover una lista
print(lista)
lista.pop()
print(lista)

# Agregar un elemento
lista.append(56)
lista.append(20)
lista.append(2)

print(lista)
