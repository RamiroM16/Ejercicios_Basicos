### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Ramiro",
                 "Apellido": "Mendoza", "Edad": 25, 1: "Python"}

my_dict = {
    "Nombre": "Ramiro",
    "Apellido": "Mendoza",
    "Edad": 25,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.78
}
print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])
print(my_dict["Lenguajes"])

my_dict["Nombre"] = "Diego"
print(my_dict["Nombre"])

my_dict["Calle"] = "Ramiromd"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Ramiro" in my_dict)
print("Nombre" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())


my_list = ["Nombre", 1]
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, "Ramiro")
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(my_new_dict.values()))
print(list(my_new_dict))
