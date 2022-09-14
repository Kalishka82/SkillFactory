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
