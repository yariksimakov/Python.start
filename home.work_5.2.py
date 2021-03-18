# *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
# не используя ключевое слово yield.

def generation(param):
    return (el for el in range(1, param + 1, 2))


print(*generation(9))