# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл
# логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

# from requests import get, utils
# response = get("https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs")
# encoding = utils.get_encoding_from_headers(response.headers)
# content = response.content.decode(encoding=encoding)

with open('nginx_logs.txt', encoding='utf-8') as f:
    content = ((el.split()[0], ', '.join(el.split()[5:7])) for el in f)
    for el in content:
        print(el)