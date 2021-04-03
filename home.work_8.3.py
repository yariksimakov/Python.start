# Примечание: если аргументов несколько - выводить данные о каждом
# через запятую; можете ли вы вывести тип значения функции? Сможете
# ли решить задачу для именованных аргументов? Сможете ли вы замаскировать
# работу декоратора? Сможете ли вывести имя функции, например, в виде:

def logger(verbosity=0):
    def _logger(func):
        def wrapper(*args, **kwargs):
            print(f'{*args, *kwargs.values()}')
            type_values = [f'{el:.2f} - {type(el)}' for el in func(*args, *kwargs.values())]
            return f'{func.__name__} {type_values}'
        return wrapper
    return _logger


@logger()
def render_input(*args, **kwargs):
    return [el ** 3 for el in (*args, *kwargs.values()) if isinstance(el, int) or isinstance(el, float)]


if __name__ == '__main__':
    print(render_input(5, 6, 3, sr=5, srt=4.3))
    # print(render_input.__name__)
    # help(render_input)