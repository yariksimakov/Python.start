# Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
# a Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 –
# делится нацело на 7. Внимание: использовать только арифметические операции!
# b К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

my_list = []

for i in range(1, 1001, 2):
    my_list.append(i ** 3)
print(my_list)

my_sum = []
for index in my_list:
    if index % 7 == 0:
        my_sum.append(index)
print(f"{sum(my_sum)} - summa")

for i, number in enumerate(my_list):
    number += 17
    my_list[i] = number
print(my_list)

new_sum = 0
for number in my_list:
    if number % 7 == 0:
        new_sum += number
print(f"{new_sum} - summa")
