from requests import get, utils

response = get("http://www.cbr.ru/scripts/XML_daily.asp")
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)


def currency_rates(code):
    result = content.split('Valute')
    for el in result:
        if code.isdigit():
            return None
        if code.upper() in el:
            return float(el.split('Value>')[1].replace('</', '').replace(',', '.'))


if __name__ == '__main__':
    print(currency_rates('usd'))
    print(currency_rates('036'))
