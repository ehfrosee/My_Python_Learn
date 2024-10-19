# Импортируем библиотеку subprocess
import subprocess

# Определяем функцию git_config_list, которая будет выполнять команду Git 
# (нужно в консоль вывести результат работы команды git: git config --global --list)
def git_config_list():
    result = subprocess.run(['git', 'config', '--global', '--list'])
    result.stdout
    # Удаляем заглушку, создаем переменную result:
    # Используем subprocess.run для выполнения команды в переменной result
    # Выводим результат выполнения команды result.stdout
    

# вызываем git_config_list()
git_config_list()