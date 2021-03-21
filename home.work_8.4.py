# Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные
# значения функции и выбрасывать исключение ValueError, если что-то не так, например:

def val_checker(val_func):
    def callback(func):
        def wrapper(*num):
            resul_list = list()
            for el in num:
                if val_func(el) > 0:
                    resul_list.append(func(el))
                else:
                    raise ValueError(f'problem {el} в списе {num}')
            return resul_list
        return wrapper

    return callback


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    try:
        print(*calc_cube(8, 7, 5, 4))
    except ValueError as err:
        print(err)
    else:
        print('all right')
    finally:
        print('good')
