"""
Точка входа. Управляющий код верхнего уровня
"""

# текущий проект
import data
import files
import help
import utils


def config():
    """Чтение файлов, инициализация структур данных."""
    data.players_db = files.read_players()
    data.saves_db = files.read_saves()
    
    if not data.players_db:
        help.print_full_help()
    
    utils.change_dimension(3)
    
    ...


def main_menu():
    """Главное меню."""
    ...


def end():
    """Перед завершением работы."""
    ...



if __name__ == '__main__':
    config()
    main_menu()
    end()

