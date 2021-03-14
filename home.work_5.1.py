# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield

def generation(param):
    for el in range(1, param + 1, 2):
        yield el


print(*generation(8))
print(*generation(20))