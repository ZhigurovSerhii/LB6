import psycopg2
from tabulate import tabulate  


def execute_query(connection, query):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(f"Помилка виконання запиту: {e}")
        return None

def show_type_bd(connection):
    if connection:
        show_tables_query = """
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
        """

        tables = execute_query(connection, show_tables_query)

        if tables:
            for table in tables:
                table_name = table[0]
                print(f"\nТаблиця: {table_name}")

                describe_table_query = f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}'"
                table_structure = execute_query(connection, describe_table_query)

                if table_structure:
                    headers = [column[0] for column in table_structure]
                    print(tabulate(table_structure, headers, tablefmt="grid"))

                    select_data_query = f"SELECT * FROM {table_name}"
                    table_data = execute_query(connection, select_data_query)

                    if table_data:
                        print("\nДані таблиці:")
                        print(tabulate(table_data, headers, tablefmt="grid"))

        connection.close()

