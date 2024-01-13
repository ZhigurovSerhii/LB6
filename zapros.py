from psycopg2 import sql
from tabulate import tabulate

def show_table(cur):
    # Запит 1
    query1 = """
        SELECT * FROM Clients WHERE client_type = 'фізична особа' ORDER BY last_name;
    """
    cur.execute(query1)
    results1 = cur.fetchall()
    print("\nРезультат запиту 1:")
    print(tabulate(results1, headers=["client_code", "client_type", "address", "last_name", "first_name", "middle_name"]))

    # Запит 2
    query2 = """
        SELECT client_type, COUNT(*) FROM Clients GROUP BY client_type;
    """
    cur.execute(query2)
    results2 = cur.fetchall()
    print("\nРезультат запиту 2:")
    print(tabulate(results2, headers=["client_type", "count"]))

    # Запит 3
    query3 = """
        SELECT c.*, t.cost_per_minute * c.call_duration AS call_cost
        FROM Calls c
        JOIN Tariffs t ON c.tariff_code = t.tariff_code;
    """
    cur.execute(query3)
    results3 = cur.fetchall()
    print("\nРезультат запиту 3:")
    print(tabulate(results3, headers=["call_code", "call_date", "phone_number", "call_duration", "tariff_code", "call_cost"]))

    # Запит 4
    call_type_param = 'внутрішній'
    query4 = sql.SQL("""
        SELECT * FROM Calls c
        JOIN Tariffs t ON c.tariff_code = t.tariff_code
        WHERE t.call_type = {};
    """).format(sql.Literal(call_type_param))
    cur.execute(query4)
    results4 = cur.fetchall()
    print("\nРезультат запиту 4:")
    print(tabulate(results4, headers=["call_code", "call_date", "phone_number", "call_duration", "tariff_code"]))

    # Запит 5
    query5 = """
        SELECT p.client_code, SUM(t.cost_per_minute * c.call_duration) AS total_cost
        FROM Calls c
        JOIN Tariffs t ON c.tariff_code = t.tariff_code
        JOIN Phones p ON c.phone_number = p.phone_number
        GROUP BY p.client_code;
    """
    cur.execute(query5)
    results5 = cur.fetchall()
    print("\nРезультат запиту 5:")
    print(tabulate(results5, headers=["client_code", "total_cost"]))

    # Запит 6
    query6 = """
        SELECT p.client_code, t.call_type, SUM(c.call_duration) AS total_minutes
        FROM Calls c
        JOIN Tariffs t ON c.tariff_code = t.tariff_code
        JOIN Phones p ON c.phone_number = p.phone_number
        GROUP BY p.client_code, t.call_type;
    """