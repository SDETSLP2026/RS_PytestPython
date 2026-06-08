import json
import pytest

from playwright.sync_api import Playwright, expect
from pageObjects.login import LoginPage
from utils.apiBaseFramework import APIUtils

# JSON file for credentials -> util -> access into test
with open('data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']


@pytest.mark.smoke
@pytest.mark.parametrize('user_credentials',
                         user_credentials_list)  # This is used to pull all the datasets from the JSON file
def test_e2e_web_api(playwright: Playwright, browserInstance,
                     user_credentials):  # Here, user_credentials is used as a fixture

    user_email = user_credentials["userEmail"]
    user_password = user_credentials["userPassword"]

    # Create Order => OrderID
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)

    # Login
    loginPage = LoginPage(browserInstance)  # Created an object of a LoginPage constructor
    loginPage.navigate()  # this will load the application URL

    # After login it is landed on dashboard page
    dashboardPage = loginPage.login(user_email, user_password)

    # From Dashboard page - clicking on the 'ORDERS' - it will show orderHistoryPage
    orderHistoryPage = dashboardPage.selectOrdersNavLink()

    # Order's History
    orderDetailsPage = orderHistoryPage.selectOrder(orderId)
    orderDetailsPage.verifyOrderMessage()

# To run test parallel -  pip install pytest-xdist
# pytest -n 3 (No of tests needs to be run in parallel)

# To generate HTML reports - pip install pytest-html
# pytest -n 3 --html=report.html (No of tests needs to be run in parallel)

# For Screenshots & Logs
# Trace viewer - on, off, retain-on-failure
# pytest --tracing on
