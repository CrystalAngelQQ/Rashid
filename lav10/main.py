#!/usr/bin/python3
import psycopg2cffi as psycopg2
from config import config

def connect():
    print("Какой режим вы хотите выбрать? Введите число...")
    print("1) Загрузить из файла CSV")
    print("2) Добавить нового пользователя")
    mode = int(input("Введите число... "))
    commands = (
        """
        CREATE TABLE phonebook (
            name VARCHAR(255) NOT NULL,
            number INTEGER NOT NULL
        )
        """,
    )
    if mode == 1:
        commands += """
        COPY phonebook(name, number)
        FROM 'phonebook.csv'
        DELIMITER ','
        CSV HEADER;
        """,
    elif mode == 2:
        new_name = input("Введите имя: ")
        new_number = input("Введите номер (без знака плюс): ")
        commands += f"""
        INSERT INTO phonebook(name, number)
        VALUES ('{new_name}', '{new_number}');
        """,

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        for command in commands:
            cur.execute(command)

        cur.fetchone()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")


if __name__ == "__main__":
    connect()
