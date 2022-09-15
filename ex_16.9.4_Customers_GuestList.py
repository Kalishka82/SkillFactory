# Команда проекта «Дом питомца» планирует большой корпоратив для своих клиентов. Вам необходимо
# написать программу, которая позволит составить список гостей. В класс «Клиент» добавьте метод,
# который будет возвращать информацию только об имени, фамилии и городе клиента.

# Затем создайте список, в который будут добавлены все клиенты, и выведете его в консоль.

class Customers:
    def __init__(self, name='', surname='', city='', balance=0):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f"{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб.\n"

    def get_guest(self):
        return f"{self.name} {self.surname}, {self.city}"


customer_1 = Customers("Петр", "Иванов", "Москва", 50)
customer_2 = Customers("Иван", "Петров", "Нижний Новгород")
customer_3 = Customers("Анна", "Сидорова", "Краснодар", 280)

guest_list = [customer_1, customer_2, customer_3]

for guest in guest_list:
    print(guest.get_guest())
