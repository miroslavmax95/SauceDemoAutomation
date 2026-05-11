# This is an automation testing suite for SauceDemo test app, built
# using Python, Playwright and pytest. 

# The main goal is to create a simple
# regression testing suite that will cover all main sections of the
# application.

Tech stack:
- Python 3.12
- Playwright
- pytest / pytest/playwright


Project structure:
- pages/ - Page object model classes
- tests/ - Test suites
- conftest.py - Shared fixtures

How to run:
- pip install -r requirements.txt
- playwright install
- pytest -v

Suite coverage (still in progress):
- Login (happy path + some negative cases);
- Inventory / product management
- Shopping cart flow
- Checkout