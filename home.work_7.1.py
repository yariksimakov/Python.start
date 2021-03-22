# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
#
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок
# под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить данные о
# вложенных папках и файлах (добавлять детали)?

import os

name_dir = {'new_project': ['my_project',
                            'settings',
                            'mainapp',
                            'adminapp',
                            'authapp']}


def starter(kwargs):
    for key, val in kwargs.items():
        if not os.path.exists(key):
            for el in val:
                os.makedirs(os.path.join(key, el))

        else:
            return 'Such a folder already exists '


if __name__ == '__main__':
    starter(name_dir)
