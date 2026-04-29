import mysql.connector

# MySQL se connect karo
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="WJ28@krhps"
)

cursor = conn.cursor()

# Database banao
cursor.execute("CREATE DATABASE IF NOT EXISTS price_monitor")
cursor.execute("USE price_monitor")

# Products table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id       INT PRIMARY KEY,
        name     VARCHAR(200),
        category VARCHAR(100),
        price    DECIMAL(10,2),
        saved_at DATETIME
    )
""")

# Alerts table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS alerts (
        id        INT AUTO_INCREMENT PRIMARY KEY,
        product   VARCHAR(200),
        old_price DECIMAL(10,2),
        new_price DECIMAL(10,2),
        change_type VARCHAR(20),
        alert_time  DATETIME
    )
""")

conn.commit()
conn.close()

print("Database 'price_monitor' ban gaya!")
print("Table 'products' ban gayi!")
print("Table 'alerts' ban gayi!")

