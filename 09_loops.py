### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else:
    print("Mi condicion es mayor o igual que 10")
print("Saliendo del loop while")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condicion es 15")
        break                   # con esto se detiene subitamente el loop
    print(my_condition)

# For

my_list = [35, 23, 43, 12, 43, 24, 16, 26, 19]
for element in my_list:
    print(element)

my_tuple = (35, 1.78, "Ramiro", "Mendoza", 1.78)
for element in my_tuple:
    print(element)

my_set = {"Ramiro", "Mendoza", 25}
for element in my_set:
    print(element)

my_dict = {
    "Nombre": "Ramiro",
    "Apellido": "Mendoza",
    "Edad": 25,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.78
}
for element in my_dict:
    print(element)
else:
    print("El loop for para el diccionario acaba")
