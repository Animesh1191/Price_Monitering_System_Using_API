
import requests
import mysql.connector
from datetime import datetime

# MySQL se connect karo
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="WJ28@krhps",
    database="price_monitor"
)
cursor = conn.cursor()

print("API se products fetch ho rahe hain...")
products = requests.get("https://fakestoreapi.com/products").json()

now = datetime.now()

for p in products:

    # Pehle purani price dekho
    cursor.execute("SELECT price FROM products WHERE id = %s", (p["id"],))
    row = cursor.fetchone()

    # Naya price save karo
    cursor.execute("""
        INSERT INTO products (id, name, category, price, saved_at)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            price    = VALUES(price),
            saved_at = VALUES(saved_at)
    """, (p["id"], p["title"], p["category"], p["price"], now))

    # Agar purana price tha - compare karo
    if row:
        old_price = float(row[0])
        new_price = p["price"]

        if new_price > old_price:
            change = "INCREASE"
        elif new_price < old_price:
            change = "DECREASE"
        else:
            continue  # same price, koi alert nahi

        cursor.execute("""
            INSERT INTO alerts (product, old_price, new_price, change_type, alert_time)
            VALUES (%s, %s, %s, %s, %s)
        """, (p["title"], old_price, new_price, change, now))

        print(f" {change} | {p['title'][:35]} | ${old_price} → ${new_price}")

conn.commit()
conn.close()

print(f"\n{len(products)} products save ho gaye!")

