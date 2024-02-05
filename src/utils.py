"""
Вспомогательный модуль — дополнительные функции.
"""

# текущий проект
import bot
import data


def change_dimension(new_dimension: int) -> None:
    """Переопределяет все глобальные переменные, связанные с размером игрового поля."""
    data.dim = new_dimension
    data.all_cells = new_dimension**2
    data.dim_range = range(new_dimension)
    data.all_cells_range = range(data.all_cells)
    data.empty = dict.fromkeys(data.all_cells_range, ' ')
    data.field = generate_field_template(new_dimension)
    data.wins = generate_win_combinations(new_dimension)
    data.start_matrices = (
        bot.calc_sm_cross(),
        bot.calc_sm_zero()
    )
    data.MESSAGES['ход не в диапазоне'].format(data.all_cells-1)


def get_new_dimension() -> int:
    """Получает от пользователя новый размер игрового поля."""
    ...


def generate_field_template(dimension: int) -> str:
    """Возвращает строковый шаблон игрового поля требуемого размера."""
    ...


def generate_win_combinations(dimension: int) -> data.WinCombinations:
    """Возвращает список победных комбинаций номеров клеток игрового поля требуемого размера."""
    ...


def clear(delete_save: bool = False) -> None:
    """Перезаписывает начальными значениями глобальные переменные, связанные с игровым процессом."""
    ...

