import os
import configparser 


def install_requirements():
    print('Требование к установке ...')
    os.system('python -m pip install -r requirements.txt')

def setup_config():
    cpass = configparser.RawConfigParser()
    cpass.add_section('account')

    apixid = input("Введите идентификатор API: ")
    cpass.set('account', 'api_id', apixid)

    apixhash = input("Введите xеш API: ")
    cpass.set('account', 'api_hash', apixhash)

    username = input("Введите username: ")
    cpass.set('account', 'username', username)

    xphone = input('Введите телефон номер: ')
    cpass.set('account', 'phone', xphone)

    password = input("Введите пароль (Если нету нажми ENTER): ")
    cpass.set('account', 'password', password)

    channel_id = input("Введите идентификатор канала: ")
    cpass.set('account', 'channel_id', channel_id)

    channel_2_id = input("Введите идентификатор второго канала: ")
    cpass.set('account', 'channel_2_id', channel_2_id)

    with open('config.ini', 'w') as setup_file:
        cpass.write(setup_file)

    print("Настройка завершена!")


def main():
    # Установка необходимых зависимостей.
    install_requirements()
    # Настройка конфигурационнного файла.
    setup_config()


if __name__ == "__main__":
    main()