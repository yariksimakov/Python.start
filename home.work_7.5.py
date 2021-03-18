# *(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
#     {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
#
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

import json
import os
import django


def static_Json_dict():
    root_dir = django.__path__[0]
    result_dict = {}
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            exit = file.split('.', maxsplit=1)[-1].lower()
            if size in result_dict:
                result_dict[size][0] += 1
                if exit not in result_dict[size][1]:
                    result_dict[size][1].append(exit)
            else:
                result_dict[size] = [1, [exit]]
    print(result_dict)
    json_dict = {}
    for k, val in sorted(result_dict.items()):
        json_dict[k] = tuple(val)
    print(json_dict)
    with open('folder_name_summary.json', 'w', encoding='utf-8') as f:
        json.dump(json_dict, f)



if __name__ == '__main__':
    static_Json_dict()
