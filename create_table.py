create_Tariffs = ("""
    CREATE TABLE IF NOT EXISTS Tariffs (
        tariff_code SERIAL PRIMARY KEY,
        call_type VARCHAR(20),
        cost_per_minute DECIMAL(10, 2)
    )
""")

create_Client =("""
    CREATE TABLE IF NOT EXISTS Clients (
        client_code SERIAL PRIMARY KEY,
        client_type VARCHAR(255),
        address VARCHAR(255),
        last_name VARCHAR(255),
        first_name VARCHAR(255),
        middle_name VARCHAR(255)
    )
""")

create_Phone =("""
    CREATE TABLE IF NOT EXISTS Phones (
        phone_number VARCHAR(30) PRIMARY KEY,
        client_code INTEGER REFERENCES Clients(client_code)
    )
""")

create_Calls= ("""
    CREATE TABLE IF NOT EXISTS Calls (
        call_code SERIAL PRIMARY KEY,
        call_date DATE,
        phone_number VARCHAR(20) REFERENCES Phones(phone_number),
        call_duration INTEGER,
        tariff_code INTEGER REFERENCES Tariffs(tariff_code)
    )
""")

write_Clients= ("""
    INSERT INTO Clients (client_type, address, last_name, first_name, middle_name)
    VALUES
        ('відомство', 'Київ, вул. Примерна, буд. 1', 'Іванов', 'Олександр', 'Петрович'),
        ('фізична особа', 'Львів, вул. Тестова, буд. 2', 'Петров', 'Ірина', 'Андріївна'),
        ('фізична особа', 'Одеса, вул. Зразкова, буд. 3', 'Сидоренко', 'Максим', 'Ігорович'),
        ('відомство', 'Харків, вул. Макетна, буд. 4', 'Коваленко', 'Анна', 'Олегівна'),
        ('фізична особа', 'Дніпро, вул. Прикладна, буд. 5', 'Ткаченко', 'Ігор', 'Сергійович')
""")



# Додавання телефонів
write_Phones= ("""
    INSERT INTO Phones (phone_number, client_code)
    VALUES
        ('+380501234567', 1),
        ('+380502345678', 2),
        ('+380503456789', 3),
        ('+380504567890', 4),
        ('+380505678901', 5),
        ('+380506789012', 1),
        ('+380507890123', 2)
""")

# Додавання розмов
write_Calls= ("""
    INSERT INTO Calls (call_date, phone_number, call_duration, tariff_code)
    VALUES
        ('2024-01-01', '+380501234567', 10, 1),
        ('2024-01-02', '+380502345678', 15, 2),
        ('2024-01-03', '+380503456789', 20, 3),
        ('2024-01-04', '+380504567890', 25, 1),
        ('2024-01-05', '+380505678901', 30, 2),
        ('2024-01-06', '+380501234567', 35, 3),
        ('2024-01-07', '+380507890123', 40, 1),
        ('2024-01-08', '+380506789012', 45, 2),
        ('2024-01-09', '+380503456789', 50, 3),
        ('2024-01-10', '+380504567890', 55, 1),
        ('2024-01-11', '+380505678901', 60, 2),
        ('2024-01-12', '+380501234567', 65, 3),
        ('2024-01-13', '+380507890123', 70, 1),
        ('2024-01-14', '+380506789012', 75, 2),
        ('2024-01-15', '+380503456789', 80, 3),
        ('2024-01-16', '+380504567890', 85, 1),
        ('2024-01-17', '+380505678901', 90, 2),
        ('2024-01-18', '+380501234567', 95, 3),
        ('2024-01-19', '+380507890123', 100, 1),
        ('2024-01-20', '+380506789012', 105, 2)
""")

# Додавання тарифів
write_Tariffs= ("""
    INSERT INTO Tariffs (call_type, cost_per_minute)
    VALUES
        ('внутрішній', 0.5),
        ('міжміський', 1),
        ('мобільний', 1.5)
""")


