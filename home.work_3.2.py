# *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать
# корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
# Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

def num_translate_adv(el):
    dict_translate = {'zero': 'ноль',
                      'one': 'один',
                      'two': 'два',
                      'three': 'три',
                      'four': 'четыре',
                      'five': 'пять',
                      'six': 'шесть',
                      'seven': 'семь',
                      'eight': 'восемь',
                      'nine': 'девять',
                      'ten': 'десять'}
    if el.lower() not in dict_translate:
        return 'you enter mistake number'
    return dict_translate.setdefault(el.lower()).capitalize()  # Если ключа нету вернет None


print(num_translate_adv('One'))
print(num_translate_adv('fifty'))
