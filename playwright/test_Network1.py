import pytest
from playwright.sync_api import Page

# Verify the message on the ORDERS page when no orders are shown
# API call from browser > API call contact server > returns response to browser > Browser use response to generate HTML

fakePayloadOrderResponse = {"data": [], "message": "No Orders"}


def intercept_response(route):
    # fulfill() - This method captures the response returned by the route
    route.fulfill(
        json=fakePayloadOrderResponse
    )

@pytest.mark.smoke
def test_Network1(page: Page):
    # Hitting URL
    page.goto("https://rahulshettyacademy.com/client/")

    # Opening a listener to sense orders page URL
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    # * - for any orderID
    # route() will give you all the information of the call

    # Login
    page.get_by_placeholder("email@example.com").fill("sdetswapnil@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("SDETsp#2025")
    page.get_by_role("button", name="Login").click()

    # Clicking on the 'ORDERS'
    page.get_by_role("button", name="ORDERS").click()

    # Fetch the message on the orders page and display in console when no orders available on the orders page.
    order_text = page.locator(".mt-4.ng-star-inserted").text_content()
    print(order_text)
