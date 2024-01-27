from typing import Literal


def get_human_turn() -> int:
    ...

def easy_bot_turn() -> int:
    ...

def hard_bot_turn() -> int:
    ...

def if_win(pointer: Literal[0, 1]) -> bool:
    ...


dim = 3
all_cells = dim**2

tokens = ('X', 'O')

players_names = ['лёгкий_бот', 'имя_игрока_1']
players_funcs = [easy_bot_turn, get_human_turn]

turns = {}

for t in range(all_cells):
    p = t % 2
    
    turn = players_funcs[p]()
    turns[turn] = tokens[p]

    if if_win(p):
        print(f'победил {players_names[p]}')
        break

