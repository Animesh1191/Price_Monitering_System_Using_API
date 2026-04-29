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

## 🎥 Live Demo

### 🌐 Deployed Version (Vercel / Cloud)

👉 Add your deployed link here:

```bash
https://your-project-name.vercel.app
```

> ⚠️ Note: Streamlit apps are usually deployed on **Streamlit Cloud / Render**, not Vercel.
> If you still use Vercel, host frontend separately or show demo screenshots.

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

## 📊 Example Output

### 🔴 Price Increase

```
INCREASE | Product Name | $20 → $25
```

### 🟢 Price Decrease

```
DECREASE | Product Name | $50 → $45
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

## 🚀 Deployment Guide

### 🟣 Option 1: Streamlit Cloud (Recommended)

1. Push code to GitHub
2. Go to Streamlit Cloud
3. Connect your repo
4. Select `step3_app.py`
5. Deploy

---

### 🟡 Option 2: Render

1. Create a new Web Service
2. Add build command:

```
pip install -r requirements.txt
```

3. Start command:

```
streamlit run step3_app.py --server.port=10000 --server.address=0.0.0.0
```

---

### 🔵 Option 3: Vercel (Alternative Showcase)

Vercel does NOT support Python backend directly for Streamlit.

👉 You can:

* Deploy screenshots (portfolio showcase)
* Or create a simple frontend + API separately

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

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 📢 Share it

---

💡 *A real-world beginner project showing complete data flow from API to dashboard.*
