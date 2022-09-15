# Откройте сайт «Дом питомца» и на основе имеющихся в нем данныхсоздайте конструктор класса Cat со
# следующими параметрами: имя, пол, возраст.
# В отдельный файл импортируйте и создайте объект Cat, который выводит имеющихся на сайте котов,
# с одинаковыми параметрами, но с разными значениями.

class Pet:
# Cat заменила на Pet для практики, тк на сайте PetFriend кот только один
    def __init__(self, species='', name='', gender='', age=0):
        self.species = species
        self.name = name
        self.gender = gender
        self.age = age

    def getSpecies(self):
        return self.species

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getAge(self):
        return self.age
