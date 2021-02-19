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

new_list = []
for el, i in enumerate(my_list):
    my_sum = []
    while True:
        num = i % 10
        i //= 10
        my_sum.append(num)
        if i == 0:
            break
    if sum(my_sum) % 7 == 0:
        new_list.append(my_list[el])
print("{} - summa ".format(sum(new_list)))


for i, number in enumerate(my_list):
    number += 17
    my_list[i] = number
print(my_list)


new_list = []
for el, i in enumerate(my_list):
    my_sum = []
    while True:
        num = i % 10
        i //= 10
        my_sum.append(num)
        if i == 0:
            break
    if sum(my_sum) % 7 == 0:
        new_list.append(my_list[el])
print(f"{sum(new_list)} - summa")
