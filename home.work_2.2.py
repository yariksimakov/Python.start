# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить
# нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать
# это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться
# к его реализации позже. Главное: дополнить числа до двух разрядов нулём!

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

result_list = []
for index, el in enumerate(my_list):
    el_2 = ''.join(el)
    if el.isdigit():
        result_list.append('"'), result_list.append(f"{int(el) :02}"), result_list.append('"')
    elif el_2.find("+") == 0 or el_2.find("-") == 0:
        result_list.append('"'), result_list.append(f"+{int(my_list[index]) :02}"), result_list.append('"')
    else:
        result_list.append(el)

print(result_list)

my_str = str()
for index, el in enumerate(result_list):
    el_2 = ''.join(el)
    if el.isdigit():
        my_str += result_list[index - 1] + el + result_list[index + 1] + ' '
    elif el_2[0] == '+' or el_2[0] == '-':
        my_str += result_list[index - 1] + el + result_list[index + 1] + ' '
    elif el != '"':
        my_str += el + ' '
print(my_str)
