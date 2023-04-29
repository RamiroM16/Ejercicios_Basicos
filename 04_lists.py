### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [15, 24, 65, 23, 14, 40, 28]

print(my_list)
print(len(my_list))

my_other_list = [24, 1.78, "Ramiro", "Mendoza"]
print(my_other_list)

print(type(my_list))
print(type(my_other_list))
print(my_other_list[1])
# cuenta cuantos elementos tiene la lista del valor introducido
print(my_other_list.count("Ramiro"))
print(my_other_list.count("ramiro"))

age, height, name, surname = my_other_list
print(name)

print(my_list + my_other_list)

my_other_list.append("Ramiromd")
print(my_other_list)

my_other_list.insert(1, "rojo")
print(my_other_list)

my_other_list.remove("rojo")
print(my_other_list)

# el pop sirve para desapilar, y returna el elemento desapilado
print(my_list.pop())
print(my_list)

my_list.clear()
print(my_list)

my_list = "Hola python"
print(my_list)
print(type(my_list))
