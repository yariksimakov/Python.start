import re

re_email = re.compile(r'(?P<username>([\w]+))@(?P<domin>[^&]+\.\w+)')


# re_email = re.compile(r'\b(\w)@\w\b')

def email_parse(name):
    if not re_email.match(name):
        raise ValueError
    print(re_email.match(name).groupdict())


if __name__ == '__main__':
    try:
        email_parse('someone@geekbrains.ru')
    except (AttributeError, ValueError) as err:
        print(err)
