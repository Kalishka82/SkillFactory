n = int(input('Input amount of tickets you need: '))
price = [0, 990, 1390]
discount = 0.1
subtotal = 0

for i in range(1, n + 1):
    age = int(input(f"Input age of visitor {i}: "))
    if age < 18:
        # print('Ticket price = ', price[0])
        subtotal = subtotal + price[0]
    elif 18 <= age <= 25:
        # print('Ticket price = ', price[1])
        subtotal = subtotal + price[1]
    elif age > 25:
        # print('Ticket price = ', price[2])
        subtotal = subtotal + price[2]

if n > 3:
    subtotal = subtotal - subtotal * discount
print(f'Subtotal ({n} tickets):', round(subtotal, 2), 'rub.')
