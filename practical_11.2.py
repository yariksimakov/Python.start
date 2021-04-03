class ZeroOwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    try:
        dividend = int(input('Enter dividend: '))
        divider = int(input('Enter divider: '))
        if divider == 0:
            raise ZeroOwnError('You divide by zero, you get infinity')
    except ZeroOwnError as err:
        print(err)
    else:
        value_private = dividend / divider
        print(f'result {value_private}')
        break
