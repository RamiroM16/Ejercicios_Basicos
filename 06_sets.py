### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))   # Inicialmente es un diccionario

my_other_set = {"Ramiro", "Mendoza", 25}
print(type(my_other_set))

print(len(my_other_set))

# print(my_other_set)

my_other_set.add("RamiroMD")

print(my_other_set)         # Un set no es una estructura ordenada

my_other_set.add("RamiroMD")    # Un set no admite repetidos
print(my_other_set)

print("Ramiro" in my_other_set)
print("Ramio" in my_other_set)

my_other_set.remove("Mendoza")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set)
my_set = {"Ramiro", "Mendoza", 25}
my_list = list(my_set)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union({"JavaScript", "Python", "C#"}))

print(my_new_set.difference(my_set))
