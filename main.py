from conection import *
from create_table import *
from show_type_data import*
from zapros import *


connection = create_connection(
    "postgres", "admin", "root", "127.0.0.1", "5432"
)

def main():
    while True:
        text = input(('Веедіть дію\n1) Створити Бд \n2) Запис у бд\n3) Вивід данних \n4) Вивід данних разом з структурою\nЯкщо бажаєте завершити виконання програми натисніть будь яку чиcло\n'))
        if int(text) == 1:
            execute_query(connection, create_Tariffs)
            execute_query(connection, create_Client)
            execute_query(connection, create_Phone)
            execute_query(connection, create_Calls)
        elif int(text) == 2:
            execute_query(connection, write_Tariffs)
            execute_query(connection, write_Clients)
            execute_query(connection, write_Phones)
            execute_query(connection, write_Calls)

        elif int(text) == 3:
            cur = connection.cursor()
            show_table(cur)

        elif int(text) == 4:
            show_type_bd(connection)
        else:
            print('Допобачення')
            break

if __name__ == "__main__":
    main()