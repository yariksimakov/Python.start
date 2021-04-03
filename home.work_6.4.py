# *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах
# превышает объём ОЗУ (разумеется, не нужно реально создавать такие большие
# файлы, это просто задел на будущее проекта). Только теперь не нужно создавать
# словарь с данными. Вместо этого нужно сохранить объединенные данные в новый файл
# (users_hobby.txt). Хобби пишем через двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи

from itertools import zip_longest

with open('users.csv', encoding='utf-8') as user:
    with open('hobby.csv', encoding='utf-8') as hob:
        result_list = zip_longest((' '.join(el.replace('\n', '').split(',')) for el in user), hob)
        with open('result_dict.txt', 'w', encoding='utf-8') as f:
            for el in result_list:
                if el[0] == None:
                    break
                f.write(f'{str(el[0])}: {str(el[1])}')
