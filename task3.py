from random import randint

def unique_numbers() -> list[int]:
    get_numbers = [randint(-10, 10) for _ in range(15)] # 15 случайных чисел

    unique = set(get_numbers)

    while len(unique) < 15:
        unique = list(unique)
        unique.append(randint(-10, 10))
        unique = set(unique)
    return list(unique)


print(unique_numbers())

