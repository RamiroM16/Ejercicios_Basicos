# ### Classes ###

# class MyEmptyPerson:
#     pass


# print(MyEmptyPerson)
# print(MyEmptyPerson())


class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"

    def walk(self):
        print(f"{self.full_name} Esta caminando")


my_person = Person("Ramiro", "Mendoza")
# print(f"{my_person.name} {my_person.surname}")
print(my_person.full_name)

my_person.walk()

my_other_person = Person("Ramiro", "Mendoza", "RamiroMD")

my_other_person.walk()
