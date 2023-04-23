# Variables

my_variable = "My string variable"
print(my_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Concatenacion
print(my_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Funciones del sistema
print(len("la funcion len arroja la longitud de una cadena"))

# Variables en una sola linea
# se pueden crear variables en una sola linea, aunque no es una buena practica
name, surname, alias, age = "Ramiro", "Mend", "rmd", 25
print("Me llamo:", name, surname, "Mi edad es:", age, "y mi alias es:", alias)

"""
# Funcion para ingresar datos desde la terminal
name = input('Cual es tu nombre?: ')
age = input('Cuantos Años tienes? ') # se puede sobreescribir en las variables, tal como se esperaria de una variable

print(name)
print(age)
"""

# se puede cambiar el tipo de variable
name = 25
age = "Ramiro"
print(name)
print(age)

address: str = "Mi direccion"
address = 32
print(address)
print(type(address))
