# Реализовать склонение слова «процент» для чисел до 20. Например,
# задаем число 5 — получаем «5 процентов», задаем число 2 — получаем
# «2 процента». Вывести все склонения для проверки.

my_list = ("процент", "процента", "процентов")
result = []
for el in range(1, 21):
    if el == 1:
        result.append(f"{el} - {my_list[0]}")
    elif el >= 2 and el < 5:
        result.append(f"{el} - {my_list[1]}")
    else:
        result.append(f"{el} - {my_list[2]}")
print(result)