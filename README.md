# SauceDemo UI Automation Test Suite 🎯

This project contains a functional UI test automation suite for [SauceDemo](https://www.saucedemo.com) using Python and Playwright.

## ✅ Features Tested

1. Product sorting from Z to A
2. Product price sorting from High to Low
3. Checkout flow with multiple items in the cart

## 📋 Prerequisites

- Python 3.10 or later
- Git
- Chrome/Chromium browser
- Internet connection

## 🚀 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/saucedemo-playwright.git
cd saucedemo-playwright
```

2. **create virtual env**
```bash 
python -m venv venv
```
3. **activate virtual env**
```bash 
venv\Scripts\activate      # For Windows
```
4. **install dependencies**

```bash
pip install -r requirements.txt
playwright install
```

5. **execute test suite**
```bash
pytest saucedemo_tests
```

