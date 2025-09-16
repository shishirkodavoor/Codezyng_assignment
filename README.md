# E-commerce Automation Framework

A comprehensive Selenium automation framework built with Python and pytest for testing e-commerce web applications. This thing is pretty cool and should work for most e-commerce sites. I made this for testing online shopping websites.

### 1. Install Dependencies
pip install -r requirements.txt

### 2. Test Installation
python simple_demo.py

### 3. Run Tests

# (i) Run smoke tests
python run_tests.py --suite smoke

# (ii) Run with specific browser
python run_tests.py --suite smoke --browser firefox

# (iii) Run in headless mode
python run_tests.py --suite smoke --headless

## Project Structure

ecommerce_automation_framework/
├── config/                     # Configuration files
│   └── config.ini             # Main configuration
├── tests/                      # Test implementation
│   ├── pages/                 # Page Object Model
│   ├── testcases/             # Test cases
│   ├── data/                  # Test data
│   └── reports/               # Test reports
├── utils/                     # Utility classes
│   ├── driver_manager.py
│   ├── config_reader.py
│   └── ...
├── requirements.txt           # Dependencies
├── install.py                 # Installation script
├── run_tests.py              # Test runner
└── README.md                 # This file


## Configuration

Edit `config/config.ini` to configure your test environment. Make sure to set the right URL and browser settings:

```ini
[ENVIRONMENT]
base_url = https://demo.opencart.com/
browser = chrome
headless = false
```

## Available Test Suites

- **Smoke Tests**: Critical functionality (`--suite smoke`) - these are the most important tests
- **Regression Tests**: Complete test suite (`--suite regression`) - runs all the tests
- **Sanity Tests**: Basic functionality (`--suite sanity`) - quick tests to check if everything works

## Reports

- **HTML Report**: `tests/reports/html-report/report.html` - report with screenshots
- **Allure Report**: `allure serve tests/reports/allure-results` - fancy report with steps

## Features

-  Page Object Model (POM) - keeps the code organized
-  Multi-browser support (Chrome, Firefox, Edge) - works with different browsers
-  Parallel test execution - runs tests faster
-  Data-driven testing - uses Excel files for test data
-  Comprehensive reporting - generates nice reports
-  Screenshot capture on failures - takes pictures when tests fail
-  CI/CD integration ready - works with Jenkins and stuff


