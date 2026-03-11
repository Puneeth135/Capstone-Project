# 🧪 BStackDemo - Selenium Test Automation Framework

An end-to-end test automation framework built with **Selenium** and **Python**, using the **Page Object Model (POM)** design pattern. This project automates key user workflows on [BStackDemo](https://bstackdemo.com/), a sample e-commerce web application.

---

## 📌 Features Tested

| # | Test Case | Description |
|---|-----------|-------------|
| 1 | **Login** | Validates login with multiple credentials from Excel (data-driven) |
| 2 | **Product Search** | Searches and filters products on the catalog |
| 3 | **Add to Cart** | Adds a product to the shopping cart |
| 4 | **Checkout** | Initiates the checkout process from the cart |
| 5 | **Shipping Details** | Fills in shipping information during checkout |
| 6 | **Download Receipt** | Completes the order and validates receipt download |

---

## 🏗️ Project Structure

```
CapstoneProject/
├── conftest.py              # Pytest fixtures & hooks (driver setup, screenshot on failure)
├── pytest.ini               # Pytest configuration
├── requirements.txt         # Python dependencies
│
├── pages/                   # Page Object Model classes
│   ├── base_page.py         # Base page with reusable actions (click, type, wait)
│   ├── login_page.py        # Login page interactions
│   ├── product_page.py      # Product search & add to cart
│   ├── cart_page.py         # Cart & checkout trigger
│   └── checkout_page.py     # Shipping details & receipt download
│
├── tests/                   # Test cases
│   └── test_bstackdemo.py   # All e2e test scenarios
│
├── data/                    # Test data
│   └── test_data.xlsx       # Data-driven test inputs (credentials, products, addresses)
│
└── utils/                   # Utility modules
    ├── excel_reader.py      # Reads test data from Excel files
    ├── logger.py            # Custom logger (file-based logging)
    └── file_validator.py    # File validation utilities
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Programming language |
| **Selenium WebDriver** | Browser automation |
| **Pytest** | Test framework & runner |
| **Pytest-HTML** | HTML test report generation |
| **Pytest-Xdist** | Parallel test execution |
| **Pandas + Openpyxl** | Data-driven testing via Excel |
| **WebDriver Manager** | Automatic browser driver management |

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.8+
- Google Chrome browser

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/CapstoneProject.git
   cd CapstoneProject
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate    # macOS/Linux
   .venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Running Tests

### Run all tests
```bash
pytest
```

### Run with verbose output
```bash
pytest -v
```

### Run a specific test
```bash
pytest tests/test_bstackdemo.py::test_login
```

### Run tests in parallel
```bash
pytest -n auto
```

### Generated Outputs
After each test run, the following are generated:
- **HTML Report** → `tests/reports/report.html`
- **Logs** → `tests/logs/test_log_<timestamp>.log`
- **Screenshots** (on failure) → `tests/screenshots/`

---

## 🔑 Key Design Highlights

- **Page Object Model (POM)** — Clean separation between test logic and page interactions
- **Base Page Class** — Reusable methods for waits, clicks, scrolling, and text input with built-in exception handling
- **Data-Driven Testing** — Test data loaded from Excel, enabling easy parameterization without code changes
- **Automatic Screenshot Capture** — Screenshots taken automatically on test failure via `conftest.py` hook
- **Custom Logging** — Timestamped log files for each test session for easy debugging

---

## 📄 License

This project is for educational purposes as part of a capstone project.
