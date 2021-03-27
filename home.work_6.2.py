# Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.

with open('nginx_logs.txt', encoding='utf-8') as f:
    content = (el.split()[0] for el in f)
    list_ip = list(content)

spam_dict = {}
for el in list_ip:
    if el in spam_dict:
        spam_dict[el] += 1
    else:
        spam_dict[el] = 1

spammer = max(spam_dict.values())
for el in spam_dict:
    if spam_dict[el] == spammer:
        print(el)