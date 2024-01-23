from timeit import timeit


def option1(name1: str, name2: str) -> None:
    data = {
        'игрок_1': {'побед': 3, 'поражений': 5, 'ничьих': 8},
        'игрок_2': {'побед': 0, 'поражений': 0, 'ничьих': 0},
    }
    data[name1]['побед'] += 1
    data[name2]['поражений'] += 1


def option2(name1: str, name2: str) -> None:
    data = {
        'игрок_1': [3, 5, 8],
        'игрок_2': [0, 0, 0],
    }
    data[name1][0] += 1
    data[name2][1] += 1


if __name__ == '__main__':
    
    N = 1000
    q = 10**6
    
    seconds = timeit(lambda: option1('игрок_1', 'игрок_2'), number=N)
    print(f'тест для словаря: {seconds / N * q:.3f} мкс')
    
    seconds = timeit(lambda: option2('игрок_1', 'игрок_2'), number=N)
    print(f'тест для списка: {seconds / N * q:.3f} мкс')

