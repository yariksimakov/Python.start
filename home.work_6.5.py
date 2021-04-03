# **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки,
# чтобы можно было задать имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта.
from sys import argv
from itertools import zip_longest


def save_data(us, ho, res):
    with open(us, encoding='utf-8') as user:
        with open(ho, encoding='utf-8') as hob:
            result_list = zip_longest((el.replace('\n', '').replace(',', ' ') for el in user), hob)
            with open(res, 'w', encoding='utf-8') as f:
                for el in result_list:
                    if el[0] == None:
                        break
                    f.write(f'{str(el[0])}: {str(el[1])}')


if __name__ == '__main__':
    save_data(argv[1], argv[2], argv[3])
