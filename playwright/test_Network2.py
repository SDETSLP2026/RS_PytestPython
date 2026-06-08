from playwright.sync_api import Page, Playwright, expect

from utils.apiBase import APIUtils

# Verify the message on the ORDERS page when someone try to access someone else's order details
# API call from the browser > Mock the request before API call contact server

fakePayloadOrderResponse = {"data": [], "message": "No Orders"}

def interceptRequest(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6711e249ae2afd4c0b9f6fb0")


def test_Network2(page: Page):
    # Hitting URL
    page.goto("https://rahulshettyacademy.com/client/")

    # Opening a listener to sense orders page URL
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", interceptRequest)
    # * - for any orderID
    # route() will give you all the information of the call

    # Login
    page.get_by_placeholder("email@example.com").fill("sdetswapnil@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("SDETsp#2025")
    page.get_by_role("button", name="Login").click()

    # Clicking on the 'ORDERS'
    page.get_by_role("button", name="ORDERS").click()

    # Selecting & clicking View button of the first order
    page.get_by_role("button", name="View").first.click()

    # Fetch the message on the orders page and display in console when no orders available on the orders page.
    message = page.locator(".blink_me").text_content()
    print(message)


def test_session_storage(playwright: Playwright):
    api_utils = APIUtils()
    getToken = api_utils.getToken(playwright)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #script to inject token in session local storage
    page.add_init_script(f"""localStorage.setItem('token', '{getToken}')""") # Setting token in session storage
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text('Your Orders')).to_be_visible()