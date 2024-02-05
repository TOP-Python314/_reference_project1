"""
Точка входа. Управляющий код верхнего уровня
"""

# текущий проект
import data
import files
import help
import players
import utils


def config():
    """Чтение файлов, инициализация структур данных, авторизация."""
    data.players_db = files.read_players()
    data.saves_db = files.read_saves()
    
    if not data.players_db:
        help.print_full_help()
    
    utils.change_dimension(3)
    
    data.authorized = players.get_player_name()


def main_menu():
    """Главное меню: обработка команд."""
    command = input(data.MESSAGES['ввод команды'])
    
    if command in data.COMMANDS['...']:
        ...
    
    # elif command in data.COMMANDS['...']:
    
    ...
    
    else:
        data.MESSAGES['некорректная команда']


def end():
    """Перед завершением работы."""
    ...



if __name__ == '__main__':
    config()
    main_menu()
    end()

