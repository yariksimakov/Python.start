# *(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# для получения информации вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>,
#                                 <response_code>, <response_size>),
import re
from requests import get, utils

response = get("https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs")
encoding = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encoding)

RE_GET_PARSER = re.compile(r'([\w\.\+\:\/]+)')  # я понял регулярку пока только для чисел, для всего списка пока слабоват


def parc_http(lin):
    res_list = RE_GET_PARSER.findall(lin)
    return res_list[0], res_list[1], res_list[3], res_list[4], res_list[5], res_list[6] + res_list[7]


# print(RE_GET_PARSER.findall(content), sep=', ')

for line in content.split('\n'):
    if line: # в конце будет пустая - [], чтоб её не было
        print(parc_http(line))



# RE_DATE = re.compile(r'(?:\d{2}[./-]){2}\d{4}')
# txt = 'Погода 23.01.2021 была отличная! Зато за день до этого (22/01/2021) - очень холодно. ' \
#      'Надеемся, что 24-01-2021 будет без ветра.'
#
# RE_PRODUCTS = re.compile(r'"([^"]+)"\s*\((\d+(?:[,.]\d+)*).*\)')
# txt = '''
# Иван сегодня сделал заказ: "iPhone 12"  (158900,6 руб),
# "Galaxy S21"(98653.7 р).
# Позже он добавил в корзину "iPad"\t(32451)
# '''
# RE_EQ_LETTERS = re.compile(r'\b(\w)\w*\1\b', re.IGNORECASE)
# txt = 'Однако, хорошо у вас получилось. А как еще могло быть?'
