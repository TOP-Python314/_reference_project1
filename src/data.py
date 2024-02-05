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

