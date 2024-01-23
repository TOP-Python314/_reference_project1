from itertools import islice
from re import compile
from time import perf_counter as pc, sleep
from typing import Callable


dim = 3
all_cells = dim**2

tokens = ('X', 'O')
field_template = ' {} | {} | {} \n———————————\n {} | {} | {} \n———————————\n {} | {} | {} '
wins = [
    {0, 1, 2},
    {3, 4, 5},
    {6, 7, 8},
    {0, 3, 6},
    {1, 4, 7},
    {2, 5, 8},
    {0, 4, 8},
    {2, 4, 6}
]

ActionsIntervals = tuple[float, float, float]


def option1() -> ActionsIntervals:
    turns = {
        'имя_игрока_1': [4, 8], 
        'имя_игрока_2': [2, 0] 
    }
    results = ()
    # индекс-указатель
    p = 0
    # добавление хода
    start = pc()
    player_turns = tuple(turns.values())[p]
    player_turns.append(1)
    end = pc()
    results += (end - start, )
    # вывод поля
    start = pc()
    board = [' '] * all_cells
    for i, player_turns in enumerate(turns.values()):
        for t in player_turns:
            board[t] = tokens[i]
    field_template.format(*board)
    end = pc()
    results += (end - start, )
    # проверку на победу
    start = pc()
    player_turns = set(tuple(turns.values())[p])
    for win_comb in wins:
        if win_comb <= player_turns:
            break
    end = pc()
    results += (end - start, )
    return results


def option2() -> ActionsIntervals:
    turns = {
        'имя_игрока_1': {'X': [4, 8]}, 
        'имя_игрока_2': {'O': [2, 0]}
    }
    results = ()
    # индекс-указатель
    p = 0
    # добавление хода
    start = pc()
    player_turns = tuple(turns.values())[p][tokens[p]]
    player_turns.append(1)
    end = pc()
    results += (end - start, )
    # вывод поля
    start = pc()
    board = [' '] * all_cells
    for i, player_turns in enumerate(turns.values()):
        player_turns = player_turns[tokens[i]]
        for t in player_turns:
            board[t] = tokens[i]
    field_template.format(*board)
    end = pc()
    results += (end - start, )
    # проверку на победу
    start = pc()
    player_turns = set(tuple(turns.values())[p][tokens[p]])
    for win_comb in wins:
        if win_comb <= player_turns:
            break
    end = pc()
    results += (end - start, )
    return results


def option3() -> ActionsIntervals:
    turns = {'1': 4, '2': 2, '3': 8, '4': 0}
    results = ()
    # индекс-указатель
    p = 0
    # добавление хода
    start = pc()
    t = 5
    turns[str(t)] = 1
    end = pc()
    results += (end - start, )
    # вывод поля
    start = pc()
    board = [' '] * all_cells
    for i, t in enumerate(turns.values()):
        board[t] = tokens[i%2]
    field_template.format(*board)
    end = pc()
    results += (end - start, )
    # проверку на победу
    start = pc()
    player_turns = set(islice(turns.values(), p, None, 2))
    for win_comb in wins:
        if win_comb <= player_turns:
            break
    end = pc()
    results += (end - start, )
    return results


def option4() -> ActionsIntervals:
    turns = [['имя_игрока_1', 'имя_игрока_2'], [4, 2, 8, 0]]
    results = ()
    # индекс-указатель
    p = 0
    # добавление хода
    start = pc()
    turns[1].append(1)
    end = pc()
    results += (end - start, )
    # вывод поля
    start = pc()
    board = [' '] * all_cells
    for i, t in enumerate(turns[1]):
        board[t] = tokens[i%2]
    field_template.format(*board)
    end = pc()
    results += (end - start, )
    # проверку на победу
    start = pc()
    player_turns = set(turns[1][p::2])
    for win_comb in wins:
        if win_comb <= player_turns:
            break
    end = pc()
    results += (end - start, )
    return results


def option5() -> ActionsIntervals:
    turns = [4, 2, 8, 0]
    results = ()
    # индекс-указатель
    p = 0
    # добавление хода
    start = pc()
    turns.append(1)
    end = pc()
    results += (end - start, )
    # вывод поля
    start = pc()
    board = [' '] * all_cells
    for i, t in enumerate(turns):
        board[t] = tokens[i%2]
    field_template.format(*board)
    end = pc()
    results += (end - start, )
    # проверку на победу
    start = pc()
    player_turns = set(turns[p::2])
    for win_comb in wins:
        if win_comb <= player_turns:
            break
    end = pc()
    results += (end - start, )
    return results


def option6() -> ActionsIntervals:
    turns = {4: 'X', 2: 'O', 8: 'X', 0: 'O'}
    results = ()
    # индекс-указатель
    p = 0
    # добавление хода
    start = pc()
    turns[1] = tokens[p]
    end = pc()
    results += (end - start, )
    # вывод поля
    board = dict.fromkeys(range(all_cells), ' ')
    start = pc()
    field_template.format(*(board | turns).values())
    end = pc()
    results += (end - start, )
    # проверку на победу
    start = pc()
    player_turns = set(islice(turns, p, None, 2))
    for win_comb in wins:
        if win_comb <= player_turns:
            break
    end = pc()
    results += (end - start, )
    return results


# tests = (option1, option2, option3, option4, option5, option6)
# автоматический сбор всех объектов функций с тестами:
pat_test_func_name = compile(r'option(\d+)')
tests = tuple(
    obj
    for key, obj in globals().items()
    if pat_test_func_name.fullmatch(key) 
    and isinstance(obj, Callable)
)

N = 1000
coeff = 10**6
for i, test in enumerate(tests, 1):
    intervals = []
    for _ in range(N):
        intervals.append(test())
        sleep(0.002)
    t1 = sum(t[0] for t in intervals) / N * coeff
    t2 = sum(t[1] for t in intervals) / N * coeff
    t3 = sum(t[2] for t in intervals) / N * coeff
    print(
        f'структура {i}',
        f'  добавление хода: {t1:.2f} мкс',
        f'  вывод поля: {t2:.2f} мкс',
        f'  проверку на победу: {t3:.2f} мкс',
        f'  итого: {t1+t2+t3:.1f} мкс',
        sep='\n',
        end='\n\n'
    )


# {'имя_игрока_1': [4, 8], 
#  'имя_игрока_2': [2, 0]}
# 
# структура 1
#   добавление хода: 9.08 мкс
#   вывод поля: 25.23 мкс
#   проверку на победу: 9.29 мкс
#   итого: 43.6 мкс


# {'имя_игрока_1': {'X': [4, 8]}, 
#  'имя_игрока_2': {'O': [2, 0]}}
# 
# структура 2
#   добавление хода: 10.65 мкс
#   вывод поля: 24.18 мкс
#   проверку на победу: 9.54 мкс
#   итого: 44.4 мкс


# {'1': 4, '2': 2, '3': 8, '4': 0}
# структура 3
#   добавление хода: 3.74 мкс
#   вывод поля: 23.47 мкс
#   проверку на победу: 13.00 мкс
#   итого: 40.2 мкс


# [['имя_игрока_1', 'имя_игрока_2'], [4, 2, 8, 0]]
# структура 4
#   добавление хода: 4.78 мкс
#   вывод поля: 21.76 мкс
#   проверку на победу: 9.83 мкс
#   итого: 36.4 мкс


# [4, 2, 8, 0]
# структура 5
#   добавление хода: 3.12 мкс
#   вывод поля: 24.48 мкс
#   проверку на победу: 10.30 мкс
#   итого: 37.9 мксс


# {4: 'X', 2: 'O', 8: 'X', 0: 'O'}
# структура 6
#   добавление хода: 1.85 мкс
#   вывод поля: 19.46 мкс
#   проверку на победу: 11.38 мкс
#   итого: 32.7 мкс



# >>> board_empty = dict.fromkeys(range(9), ' ')
# >>> board_empty
# {0: ' ', 1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' '}
# >>>
# >>> turns = {4: 'X', 2: 'O', 8: 'X', 0: 'O'}
# >>> turns
# {4: 'X', 2: 'O', 8: 'X', 0: 'O'}
# >>>
# >>> board_empty | turns
# {0: 'O', 1: ' ', 2: 'O', 3: ' ', 4: 'X', 5: ' ', 6: ' ', 7: ' ', 8: 'X'}
# >>>
# >>> (board_empty | turns).values()
# dict_values(['O', ' ', 'O', ' ', 'X', ' ', ' ', ' ', 'X'])
# >>>
# >>> field_template.format(*(board_empty | turns).values())
# ' O |   | O \n———————————\n   | X |   \n———————————\n   |   | X '
# >>>
# >>> print(field_template.format(*(board_empty | turns).values()))
#  O |   | O
# ———————————
#    | X |
# ———————————
#    |   | X
