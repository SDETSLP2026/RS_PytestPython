import time

from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils


def test_e2e_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # page = playwright.chromium.launch(headless=False).new_context().new_page()

    # Create Order => OrderID
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright)

    # Hitting URL
    page.goto("https://rahulshettyacademy.com/client/")

    # Login
    page.get_by_placeholder("email@example.com").fill("sdetswapnil@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("SDETsp#2025")
    page.get_by_role("button", name="Login").click()

    # Clicking on the 'ORDERS'
    page.get_by_role("button", name="ORDERS").click()

    # Order's History
    row = page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    context.close() # This is optional
    browser.close() # This is optional
