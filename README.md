# OrangeHRM Test Automation Framework

This is a Page Object Model (POM) based test automation framework for OrangeHRM using Selenium and Python. Done as a Final year assignment for QA Test Automation module - ICT Dept, FOT, University of Colombo.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Project Structure

```
orange_hrm_automation/
│
├── PageObjects/             # Page object classes
├── TestCases/               # Test case files
├── Utilities/               # Utility functions and classes
├── Configuration/           # Configuration files
├── Logs/                    # Log files
├── Screenshots/             # Screenshots taken during test execution
├── Reports/                 # Test execution reports
│
├── requirements.txt         # Required Python packages
├── conftest.py              # Pytest configurations
└── README.md                # Project documentation
```

## Setup Instructions

1. Clone the repository:

   ```
   git clone <repository-url>
   cd orange_hrm_automation
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running Tests

To run all tests:

```
pytest -v TestCases/test_orange_hrm.py
```

To run tests and generate HTML report:

```
pytest -v TestCases/test_orange_hrm.py --html=Reports/report.html
```

To run tests with Allure reports:

```
pytest -v TestCases/test_orange_hrm.py --alluredir=Reports/allure-results
allure serve Reports/allure-results
```

## Key Features

- Page Object Model implementation
- Configurable settings via config.ini
- Parallel test execution capability
- HTML reporting
- Allure reporting
- Automatic screenshot capture on test failure
- Support for multiple browsers (Chrome, Firefox)

## Test Cases

1. `test_login_page_title`: Verify the title of the login page
2. `test_login_functionality`: Verify login functionality
3. `test_leave_functionality`: Verify leave functionality
4. `test_logout_functionality`: Verify logout functionality
