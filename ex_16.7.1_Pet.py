from ex_16_7_1 import Pet

pet_1 = Pet("собака", "Феликс", "мальчик", 2)
pet_2 = Pet("собака", "Мухтар", "мальчик")
pet_3 = Pet("кот", "Сэм", "мальчик", 2)
pet_4 = Pet("попугай", "Гоша", "мальчик", 1)

print("Питомец 1: ", pet_1.getSpecies(), pet_1.getName(), pet_1.getGender(), pet_1.getAge())
print("Питомец 2: ", pet_2.getSpecies(), pet_2.getName(), pet_2.getGender(), pet_2.getAge())
print("Питомец 3: ", pet_3.getSpecies(), pet_3.getName(), pet_3.getGender(), pet_3.getAge())
print("Питомец 4: ", pet_4.getSpecies(), pet_4.getName(), pet_4.getGender(), pet_4.getAge())

# Питомец 1:  собака Феликс мальчик 2
# Питомец 2:  собака Мухтар мальчик 0
# Питомец 3:  кот Сэм мальчик 2
# Питомец 4:  попугай Гоша мальчик 1