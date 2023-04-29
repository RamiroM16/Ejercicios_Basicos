### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.78, "Ramiro", "Mendoza", 1.78)
my_other_tuple = (15, 23, 40, 32)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4])
# print(my_tuple[-6])

print(my_tuple.count(1.78))
print(my_tuple.index("Ramiro"))
print(my_tuple.index("Mendoza"))

my_sum_tuple = my_tuple+my_other_tuple
print(my_sum_tuple)
# my_tuple[1] = 1.90        A las tuplas no se les puede cambiar el valor de los elementos
# print(my_tuple)

my_tuple = list(my_tuple)

print(type(my_tuple))

my_tuple[4] = "Ramiromd"
my_tuple.insert(1, "Rojo")
print(my_tuple)

# del my_tuple            # Elimina la variable de la tupla
# print(my_tuple)
