import pytest
from pytest_bdd import given, when, then, parsers, scenarios

from pageObjects.login import LoginPage
from utils.apiBaseFramework import APIUtils

scenarios('features/orderTransaction.feature')


@pytest.fixture
def shared_data():
    return {}  # returning empty dictionary


@given(parsers.parse('place the item order with {username} and {password}'))
def place_item_order(playwright, username, password, shared_data):
    user_credentials = {}
    user_credentials["userEmail"] = username
    user_credentials["userPassword"] = password

    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)
    shared_data['order_Id'] = orderId


@given('the user is on the landing page')
def user_on_landing_page(browserInstance, shared_data):
    loginPage = LoginPage(browserInstance)  # Created an object of a LoginPage constructor
    loginPage.navigate()  # this will load the application URL
    shared_data['login_Page'] = loginPage


@when(parsers.parse('I login to portal with {username} and {password}'))
def login_to_portal(username, password, shared_data):
    loginPage = shared_data['login_Page']
    dashboardPage = loginPage.login(username, password)
    shared_data['dashboard_Page'] = dashboardPage


@when('navigate to orders page')
def navigate_to_orders_page(shared_data):
    dashboardPage = shared_data['dashboard_Page']
    orderHistoryPage = dashboardPage.selectOrdersNavLink()
    shared_data['orderHistory_Page'] = orderHistoryPage


@when('select the orderId')
def select_order_id(shared_data):
    orderId = shared_data['order_Id']
    orderHistoryPage = shared_data['orderHistory_Page']
    orderDetailsPage = orderHistoryPage.selectOrder(orderId)
    shared_data['orderDetails_Page'] = orderDetailsPage


@then('order message is successfully displayed')
def order_message_successfully_displayed(shared_data):
    orderDetailsPage = shared_data['orderDetails_Page']
    orderDetailsPage.verifyOrderMessage()
