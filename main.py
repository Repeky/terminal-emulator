import os
import sys
import time
import random

# Глобальные переменные
word = "TERMINAL"  # Слово для анимации
delay = 0.2  # Задержка между обновлениями анимации в секундах

# Словарь с командами и их описанием
COMMANDS = {
    "--help": "Список доступных команд.",
    "sudo su": "Переход в режим суперпользователя (не реализовано).",
    "sudo -i": "Получение интерактивной оболочки суперпользователя (не реализовано).",
    "sudo apt update": "Обновление списка пакетов.",
    "poweroff": "Выключение терминала.",
    "clear": "Очистка экрана.",
    "history": "Просмотр истории команд.",
}


def animate(word):
    """
    Анимация вывода слова `word` в терминале.
    Постепенно выделяет и "стирает" буквы в слове.
    """
    clear_screen()  # Очищаем экран перед началом анимации
    try:
        _, columns = os.get_terminal_size()  # Получаем ширину терминала
    except OSError:
        columns = 80  # Используем стандартную ширину в случае ошибки

    sys.stdout.write("\033[1m\033[31m")  # Включаем жирный красный текст
    for i in range(len(word) + 1):
        sys.stdout.write("\r" + " " * ((columns - len(word)) // 2) + word[:i].lower() + word[i:].upper())
        sys.stdout.flush()
        time.sleep(delay)
    for i in range(len(word) - 1, -1, -1):
        sys.stdout.write("\r" + " " * ((columns - len(word)) // 2) + word[:i].lower() + word[i:].upper())
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m\n")  # Сбрасываем стиль текста
    # Возвращаем курсор на новую строку после анимации для последующего вывода


def write_command():
    """
    Обработка команд, введенных пользователем.
    Считывает команду, обрабатывает ее и выполняет соответствующие действия.
    """
    while True:
        command = input("Write command: ").strip()

        try:
            with open("comander.txt", "a", encoding="utf-8") as file:
                file.write(command + '\n')
        except FileNotFoundError:
            print("Файл не найден")

        if command in COMMANDS:
            if command == "clear":
                clear_screen()
            elif command == "sudo apt update":
                main_update_sequence()
            elif command == "poweroff":
                print("Выключение...")
                break
            elif command == "history":
                history()
            elif command == "--help":
                help()
            else:
                print(COMMANDS[command])
        else:
            print("Команда не распознана. Введите --help для списка команд.")


def print_progress_bar(iteration, total, prefix='', suffix='', length=50, decimals=1, fill='█', print_end="\r"):
    """
    Выводит прогресс-бар.
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()


def print_download_links(iteration, total_links):
    """
    Имитирует вывод ссылок.
    """
    link = f"http://example.com/update{iteration}"
    sys.stdout.write(f'\nСкачивание: {link} [{iteration}/{total_links}]')
    sys.stdout.flush()


def main_update_sequence():
    """
    Запускает процесс имитации обновления системы.
    """
    clear_screen()
    components_to_update = [("Ядро системы", 5), ("Драйвера устройств", 3), ("Приложения", 8)]
    for component, updates in components_to_update:
        update_component(component, updates)
    print("Все компоненты успешно обновлены!\n")


def update_component(component_name, num_updates):
    """
    Обновляет компонент с имитацией ссылок.
    """
    print(f"\033[1;33mОбновление {component_name}...\033[0m")
    for i in range(1, num_updates + 1):
        time.sleep(random.uniform(0.1, 0.3))  # Рандомная пауза для реализма
        print_progress_bar(i, num_updates, prefix='Прогресс:', suffix='Завершено', length=40)
        print_download_links(i, num_updates)
    print(f"\033[1;32m{component_name} обновлён.\033[0m\n")


def clear_screen():
    """
    Очищает экран терминала.
    Использует системные вызовы в зависимости от операционной системы.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def history():
    """
    Выводит историю команд, введенных пользователем.
    Считывает команды из файла 'comander.txt'.
    """
    try:
        with open("comander.txt", "r", encoding="utf-8") as file:
            for counter, line in enumerate(file, 1):
                print(f"{counter}. {line}", end='')
    except FileNotFoundError:
        print("Файл не найден!")


def help():
    """
    Выводит список доступных команд и их описание.
    """
    print("Доступные команды:")
    counter = 1
    for command, description in COMMANDS.items():
        print(f"{counter}. {command}: {description}")
        counter += 1


def history():
    # чтение файла по команде
    try:
        with open("comander.txt", "r", encoding="utf-8") as file:
            for counter, line in enumerate(file):
                print(f"{counter}. {line}")
    except FileNotFoundError:
        print("Фаил не найден!")


def main():
    animate(word)  # Запуск анимации с выводом "TERMINAL"
    write_command()  # Обработка команд пользователя после анимации


if __name__ == '__main__':
    main()
