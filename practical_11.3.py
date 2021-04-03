class ListOwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt


my_bool = True
result_list = []
while my_bool:
    try:
        user = input('Enter number: ')
        for el in user.split():
            if el == 'st':
                print(result_list)
                my_bool = False
                break
            if el[0] == '-':
                if el[1:].isdigit():
                    result_list.append(float(el))
                else:
                    raise ListOwnErr('You entered not a number')
            else:
                if el.isdigit():
                    result_list.append(float(el))
                else:
                    raise ListOwnErr('You entered not a number')
    except ListOwnErr as err:
        print(err)
