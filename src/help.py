"""
Исполнительный модуль — раздел помощи.
"""

# текущий проект
import data


def print_full_help() -> None:
    """Отправляет в stdout полную справку."""
    print(
        render_game_info(),
        render_interface_help(),
        render_commands(),
        sep='\n\n'
    )


def render_game_info() -> str:
    """Возвращает строку с информацией об игре."""
    ...


def render_interface_help() -> str:
    """Возвращает строку с описанием интерфейса командной строки."""
    ...


def render_numerated_filed(center: bool = True) -> str:
    """Возвращает строку игрового поля с номерами клеток.
    
    :param center: выравнивание: True - по центру, False - влево
    """


def render_commands() -> str:
    """Возвращает строку со списком команд и вариантов ввода."""
    ...

