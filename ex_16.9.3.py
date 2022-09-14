class Customers:
    def __init__(self, name='', surname='', city='', balance=0):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f"{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб."

customer_1 = Customers("Петр", "Иванов", "Москва", 50)
customer_2 = Customers("Иван", "Петров", "Нижний Новгород")
customer_3 = Customers("Николай", "Сидоров", "Краснодар", 280)

customer_list = [customer_1, customer_2, customer_3]

for customer in customer_list:
    print(customer.__str__())
