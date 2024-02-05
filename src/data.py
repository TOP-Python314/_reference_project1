"""
Вспомогательный модуль — глобальные переменные и условные константы.
"""

# стандартная библиотека
from pathlib import Path
from sys import path, argv
from typing import Any


# переменные для аннотаций
Players = dict[str, dict[str, int]]
Saves = dict[frozenset[str, str], dict[str, Any]]
SquareIndex = int
Turns = dict[SquareIndex, str]
WinCombinations = list[set[SquareIndex]]


# корень проекта
ROOT_DIR = Path(path[0]).parent
# каталог данных
DATA_DIR = ROOT_DIR / 'data'
# пути к файлам данных
players_path = DATA_DIR / 'players.ini'
saves_path = DATA_DIR / 'saves.ttt'


# словарь игроков
players_db: Players = {}
# словарь сохранений
saves_db: Saves = {}


# размер поля — все переменные, связанные с размером, вычисляются в utils.change_dimension(), первый вызов со значением по умолчанию осуществляется в main.config()
dim: int = None
# числовая последовательность от 0 до размера поля не включая
dim_range: range = None
# количество ячеек поля
all_cells: int = None
# числовая последовательность от 0 до количества ячеек поля не включая
all_cells_range: range = None
# словарь всех ячеек игрового поля --> номер: ' '
empty: Turns = None
# шаблон игрового поля
field: str = None
# индексы выигрышных последовательностей
wins: WinCombinations = None


# regex шаблон для имени игрока
NAME_PATTERN = compile(r'[A-Za-zА-ЯЁа-яё][A-Za-zА-ЯЁа-яё\d_]+')
# regex шаблон для размера игрового поля
DIM_PATTERN = compile(r'[3-9]|1[0-9]|20')


# текущий авторизованный игрок
authorized: str

