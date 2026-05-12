# 💱 Currency Converter

A simple command-line currency converter built with Python. Fetches **live exchange rates** using the [ExchangeRate API](https://www.exchangerate-api.com/) and converts between 160+ currencies instantly.

---

## ✨ Features

- 🔄 Convert any amount between 160+ currencies
- 📊 View popular exchange rates at a glance (USD, EUR, INR, GBP, JPY, and more)
- 🌐 Live rates fetched in real-time from the API
- ✅ Input validation and friendly error messages
- 💡 Simple menu-driven interface — no coding knowledge needed to use it

---

## 📸 Demo

```
=============================================
        💱  Currency Converter  💱
    Powered by exchangerate-api.com
=============================================

Options:
  [1] Convert currency
  [2] View popular exchange rates
  [3] Exit

Enter choice (1/2/3): 1

  From currency (e.g. USD): USD
  To currency   (e.g. INR): INR
  Amount: 100

  Fetching rates for USD...

  ✅  100.00 USD  =  8,312.45 INR
```

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Library:** `requests` — for making HTTP API calls
- **API:** [ExchangeRate-API](https://www.exchangerate-api.com/) (free tier, no key required)

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/currency-converter.git
cd currency-converter
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python currency_converter.py
```

---

## 📁 Project Structure

```
currency-converter/
│
├── currency_converter.py   # Main application file
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 📚 What I Learned

- How to make HTTP GET requests using the `requests` library
- How to parse JSON responses from a REST API
- Building a user-friendly CLI (command-line interface)
- Handling errors like invalid input and network failures

---

## 🔮 Future Improvements

- [ ] Add a graphical interface (GUI) using Tkinter
- [ ] Show historical exchange rate trends
- [ ] Add support for cryptocurrency conversion
- [ ] Save conversion history to a file

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
