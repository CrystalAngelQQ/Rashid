#!/usr/bin/python3
import psycopg2cffi as psycopg2
from config import config


# Создать таблицу данных "phonebook" с полями
# ник (name) и номер телефона (number)
# в базе данных "cur
def create_table(cur):
    command = """
        CREATE TABLE IF NOT EXISTS phonebook (
            name VARCHAR(255) NOT NULL,
            number INTEGER NOT NULL);
        """
    cur.execute(command)


# 1
# Загрузить из файла "phonebook.csv"
# в таблицу данных "phonebook".
def load_from_file(cur):
    command = """
        COPY phonebook(name, number)
        FROM 'phonebook.csv'
        DELIMITER ','
        CSV HEADER;
        """
    cur.execute(command)


# 2
# Добавить нового пользователя в таблицу данных "phonebook"
# с ником "name" и номером телефона "number".
def enter_name_number(cur, name, number):
    new_name = str(name)
    new_number = int(
        number
    )  # Сконвертировать их в строку и число, если не получится - питон даст полезную ошибку
    command = f"""
        INSERT INTO phonebook(name, number)
        VALUES ('{new_name}', {new_number});
        """
    cur.execute(command)


# 3
# Обновить у пользователя (по нику) его номер.
def update_number_for_nick(cur, filter_name, new_number):
    filter_name = str(filter_name)
    new_number = int(
        new_number
    )  # Сконвертировать их в строку и число, если не получится - питон даст полезную ошибку
    command = f"""
        UPDATE phonebook
        SET number={new_number}
        WHERE name='{filter_name}';
        """
    cur.execute(command)


# 4
# Обновить у пользователя (по номеру) его ник.
def update_nick_for_number(cur, new_name, filter_number):
    new_name = str(new_name)
    filter_number = int(
        filter_number
    )  # Сконвертировать их в строку и число, если не получится - питон даст полезную ошибку
    command = f"""
        UPDATE phonebook
        SET name='{new_name}'
        WHERE number={filter_number};
        """
    cur.execute(command)


# 5
# Вывести список всех пользователей с таким номером
def get_by_number(cur, filter_number):
    filter_number = int(filter_number)
    command = f"""
        SELECT * FROM phonebook
        WHERE number={filter_number}
        """
    cur.execute(command)
    printed_lines = cur.fetchall()
    for printed_line in printed_lines:
        print(f"{printed_line}")


# 6
# Вывести список всех пользователей с таким ником
def get_by_nick(cur, filter_nick):
    filter_nick = str(filter_nick)
    command = f"""
        SELECT * FROM phonebook
        WHERE name='{filter_nick}'
        """
    cur.execute(command)
    printed_lines = cur.fetchall()
    for printed_line in printed_lines:
        print(f"{printed_line}")


# 7
# Удалить всех пользователей с таким номером
def delete_by_number(cur, filter_number):
    filter_number = int(filter_number)
    command = f"""
        DELETE FROM phonebook
        WHERE number={filter_number}
        """
    cur.execute(command)


# 8
# Удалить всех пользователей с таким ником
def delete_by_nick(cur, filter_nick):
    filter_nick = str(filter_nick)
    command = f"""
        DELETE FROM phonebook
        WHERE name='{filter_nick}'
        """
    cur.execute(command)


def connect():
    params = config()
    conn = psycopg2.connect(**params)  # подключение
    cur = conn.cursor()  # доступ

    # Создать таблицу
    create_table(cur)

    print("Какой режим вы хотите выбрать? Введите число...")
    print("1) Загрузить из файла CSV")
    print("2) Добавить нового пользователя")
    print("3) Обновить у пользователя (по нику) его номер.")
    print("4) Обновить у пользователя (по номеру) его ник.")
    print("5) Вывести список всех пользователей с таким номером")
    print("6) Вывести список всех пользователей с таким ником")
    print("7) Удалить всех пользователей с таким номером")
    print("8) Удалить всех пользователей с таким ником")
    mode = int(input("Введите число... "))
    # Это как switch в C++
    match mode:
        case 1:
            load_from_file(cur)
        case 2:
            name = input("Введите имя нового пользователя: ")
            number = input("Введите его номре: ")
            enter_name_number(cur, name, number)
        case 3:
            filter_name = input("Введите ник нужного пользователя: ")
            new_number = input("Введите новый номер: ")
            update_number_for_nick(cur, filter_name, new_number)
        case 4:
            filter_number = input("Введите номер нужного пользователя: ")
            new_nick = input("Введите новый ник: ")
            update_nick_for_number(cur, new_nick, filter_number)
        case 5:
            filter_number = input("Введите номер: ")
            get_by_number(cur, filter_number)
        case 6:
            filter_nick = input("Введите ник: ")
            get_by_nick(cur, filter_nick)
        case 7:
            filter_number = input("Введите номер: ")
            delete_by_number(cur, filter_number)
        case 8:
            filter_nick = input("Введите ник: ")
            delete_by_nick(cur, filter_nick)
        case _:  # если другие условия не подходят
            print("Неизвестное действие!")

    conn.commit()  # Сохранить в базу данных
    cur.close()  # Закрыть доступ
    # Если conn (подключение) ещё существует
    if conn is not None:
        conn.close()  # Закрыть подключение
        print("Подключение к базе данных закрыто.")


# Главная функция (как main в C++) это curect
if __name__ == "__main__":
    connect()
