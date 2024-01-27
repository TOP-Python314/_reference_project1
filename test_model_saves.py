from itertools import zip_longest, chain
from pathlib import Path
from pprint import pprint
from sys import path
from time import perf_counter as pc, sleep


def option1() -> tuple[float, float]:
    results = ()
    # формирование строк для записи в файл
    saves = {
        frozenset(('имя_игрока_1', 'имя_игрока_2')): {
            'X': 'имя_игрока_1', 
            'turns': [4, 2, 8, 0, 1],
            'dim': 3
        },
        frozenset(('имя_игрока_3', 'имя_игрока_1')): {
            'X': 'имя_игрока_3', 
            'turns': [],
            'dim': 7
        },
    }
    start = pc()
    saves_str = []
    for players, save in saves.items():
        players = ','.join((
            save['X'],
            set(players - {save['X']}).pop()
        ))
        turns = ','.join(map(str, save['turns']))
        saves_str.append(f'{players}!{turns}!{save["dim"]}')
    res = '\n'.join(saves_str)
    end = pc()
    # print(res)
    results += (end - start, )
    # интерпретация строки при чтении из файла
    saves_str = 'имя_игрока_1,имя_игрока_2!4,2,8,0,1!3\nимя_игрока_3,имя_игрока_1!!7'
    start = pc()
    saves = {}
    for save in saves_str.split('\n'):
        players, turns, dim = save.split('!')
        players = players.split(',')
        saves[frozenset(players)] = {
            'X': players[0],
            'turns': [int(t) for t in turns.split(',') if t],
            'dim': int(dim)
        }
    end = pc()
    # pprint(saves)
    results += (end - start, )
    return results


def option2() -> tuple[float, float]:
    results = ()
    # формирование строк для записи в файл
    saves = [
        ({'имя_игрока_1': [4, 8, 1], 'имя_игрока_2': [2, 0]}, 3),
        ({'имя_игрока_3': [], 'имя_игрока_1': []}, 7)
    ]
    start = pc()
    saves_str = []
    for save in saves:
        save, dim = save
        players = ','.join(save)
        turns = []
        turns_x, turns_o = save.values()
        for i in range(max(len(turns_x), len(turns_o))):
            try:
                turns.append(str(turns_x[i]))
                turns.append(str(turns_o[i]))
            except IndexError:
                pass
        turns = ','.join(turns)
        saves_str.append(f'{players}!{turns}!{dim}')
    res = '\n'.join(saves_str)
    end = pc()
    # print(res)
    results += (end - start, )
    # интерпретация строки при чтении из файла
    saves_str = 'имя_игрока_1,имя_игрока_2!4,2,8,0,1!3\nимя_игрока_3,имя_игрока_1!!7'
    start = pc()
    saves = []
    for save in saves_str.split('\n'):
        players, turns, dim = save.split('!')
        player_x, player_o = players.split(',')
        turns = [int(t) for t in turns.split(',') if t]
        turns_x, turns_o = turns[::2], turns[1::2]
        saves.append((
            {player_x: turns_x, player_o: turns_o},
            int(dim)
        ))
    end = pc()
    # pprint(saves)
    results += (end - start, )
    return results


N = 1000
coeff = 10**6

for test in (option1, option2):
    intervals = []
    for _ in range(N):
        intervals.append(test())
        sleep(0.002)
    t1 = sum(t[0] for t in intervals) / N * coeff
    t2 = sum(t[1] for t in intervals) / N * coeff
    print(
        f'время для {test.__name__}\n',
        f'  формирование строк: {t1:.2f} мкс\n',
        f'  интерпретация строк: {t2:.2f} мкс\n',
        f'  итого: {t1+t2:.2f} мкс\n'
    )

