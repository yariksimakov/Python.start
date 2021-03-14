from itertools import zip_longest

with open('users.csv', encoding='utf-8') as user:
    with open('hobby.csv', encoding='utf-8') as hob:
        result_list = zip_longest((' '.join(el.replace('\n', '').split(',')) for el in user), hob)
        result_dict = {index[0]: index[1] for index in result_list if index[0] != None}
        with open('result_dict.txt', 'w', encoding='utf-8') as f:
            for el in result_dict.items():
                f.writelines(f'{el[0]}: {el[1]}')
