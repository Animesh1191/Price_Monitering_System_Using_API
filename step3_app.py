
import streamlit as st
import mysql.connector
import pandas as pd
from step2_fetch_prices import *  # fetch function use karna ho to

# MySQL connection 
def get_conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="WJ28@krhps",
        database="price_monitor"
    )

#  Page 
st.set_page_config(page_title="Price Monitor", page_icon="")
st.title("Price Monitor")
st.caption("MySQL + Fake Store API + Python")

# Fetch button
if st.button(" Naye Prices Fetch Karo", type="primary"):
    with st.spinner("API se data aa raha hai..."):
        import subprocess
        subprocess.run(["python", "step2_fetch_prices.py"])
    st.success("Prices update ho gaye!")
    st.rerun()

st.divider()

#  Data dikhao 
try:
    conn = get_conn()

    # 1. Latest prices
    st.subheader("Sabhi Products ke Latest Prices")
    df = pd.read_sql("SELECT name AS Product, category AS Category, price AS Price, saved_at AS Time FROM products ORDER BY price DESC", conn)
    st.dataframe(df, use_container_width=True)

    st.divider()

    # 2. Alerts
    st.subheader("Price Alerts")
    alerts = pd.read_sql("SELECT product AS Product, old_price AS `Old Price`, new_price AS `New Price`, change_type AS `Change`, alert_time AS Time FROM alerts ORDER BY id DESC LIMIT 20", conn)

    if alerts.empty:
        st.info("Abhi koi alert nahi. Prices fetch karo dobara to changes dikhenge.")
    else:
        for _, row in alerts.iterrows():
            if row["Change"] == "INCREASE":
                st.error(f"🔴 BADHA | {row['Product'][:45]} | ${row['Old Price']} → ${row['New Price']}")
            else:
                st.success(f"🟢 GHATA | {row['Product'][:45]} | ${row['Old Price']} → ${row['New Price']}")

    st.divider()

    # 3. Category wise avg price
    st.subheader("Category wise Average Price")
    cat_df = pd.read_sql("SELECT category AS Category, ROUND(AVG(price),2) AS `Avg Price` FROM products GROUP BY category", conn)
    st.bar_chart(cat_df.set_index("Category"))

    conn.close()

except Exception as e:
    st.error(f"Error: {e}")
    st.info("Pehle step1 aur step2 chalao!")
