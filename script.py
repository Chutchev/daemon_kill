import os


def commands_list(commands):
    print("\n")
    for key in commands.keys():
        print(key)
    print("!завершить")


def daemons_list(commands):
    os.system(f"service --status-all")


def reload_daemon(daemon_name):
    os.system(f"sudo /etc/init.d/{daemon_name} reload")
    print(f"Демон {daemon_name} был перезапущен.")


def on_daemon(daemon_name):
    os.system(f"sudo /etc/init.d/{daemon_name} start")
    print(f"Демон {daemon_name} был запущен.")


def off_daemon(daemon_name):
    os.system(f"sudo /etc/init.d/{daemon_name} stop")
    print(f"Демон {daemon_name} был завершен.")

#TODO убрать индексирование и изменить методы
def main():
    commands = {"!убить": off_daemon,
                "!запустить": on_daemon,
                "!перезапустить": reload_daemon,
                "!список": daemons_list,
                "!команды": commands_list}
    command = input("Введите команду: ").split(" ")
    while command[0] != "!завершить":
        command = input("Введите команду: ").split(" ")
        if command[0] in commands:
            try:
                commands[command[0]](command[1])
            except (TypeError, IndexError):
                commands[command[0]](commands)
    print("Скрипт выключен.")


if __name__ == "__main__":
    main()
