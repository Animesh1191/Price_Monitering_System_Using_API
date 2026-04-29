# 📊 Price Monitor Project

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Overview

A simple and practical **Price Monitoring System** that tracks product prices, detects changes, and displays everything in an interactive dashboard.

👉 **Core Idea:**
Fetch → Store → Compare → Alert → Visualize

---


## 📸 Screenshots

### 🖥️ Dashboard View

  <img width="849" height="865" alt="image" src="https://github.com/user-attachments/assets/f4a9032f-d1b4-4bba-86f8-3a42c7900431" />


### 🔔 Price Alerts

  <img width="771" height="222" alt="image" src="https://github.com/user-attachments/assets/c765fa04-0687-4920-935f-da7b75b18d8a" />


### 📊 Category Analysis

  <img width="771" height="464" alt="image" src="https://github.com/user-attachments/assets/d687467e-7895-4cba-a35f-3e10bc7addee" />



---

## 🧠 How It Works

```
Fake Store API
       ↓
step2_fetch_prices.py
       ↓
MySQL Database
       ↓
step3_app.py (Streamlit UI)
```

---

## 📁 Project Structure

```
price-monitor/
│
├── step1_database_setup.py
├── step2_fetch_prices.py
├── step3_app.py
├── requirements.txt
├── screenshots/
│   ├── dashboard.png
│   ├── alerts.png
│   └── category.png
└── README.md
```

---

## ⚙️ Tech Stack

* Python
* MySQL
* Streamlit
* Pandas
* Requests

---

## ✨ Features

* ✅ Fetch product data from API
* ✅ Store data in MySQL
* ✅ Detect price changes automatically
* ✅ Generate alerts (increase/decrease)
* ✅ Interactive dashboard
* ✅ Category-wise analytics

---

## ▶️ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/price-monitor.git
cd price-monitor
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Setup Database

```bash
python step1_database_setup.py
```

---

### 4️⃣ Fetch Data

```bash
python step2_fetch_prices.py
```

---

### 5️⃣ Run Dashboard

```bash
streamlit run step3_app.py
```

---

## ⚠️ Configuration

Update MySQL credentials in all files:

```python
host="localhost",
user="root",
password="your_password"
```

---


## 🚧 Future Improvements

* 🔔 Email / WhatsApp alerts
* 🌐 Full cloud deployment
* 🛒 Real e-commerce scraping
* 👤 User authentication
* 📈 Price history graphs

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Make changes
4. Submit a pull request

---

## ⭐ Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 📢 Share it

---

💡 *A real-world beginner project showing complete data flow from API to dashboard.*
