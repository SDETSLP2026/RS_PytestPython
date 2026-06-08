# To invoke & hit any URL in the browser
# Use 'playwright' fixture
import time

from playwright.sync_api import Playwright, Page, expect


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    # Invoking chromium engine
    # Browsers depends on Chromium Engine - MSEdge, Chrome, Brave
    # By setting headless=False, the browser will run with the UI visible, allowing you to see the browser's actions.

    context = browser.new_context()
    # This is to open a browser in incognito window/maintain a session

    page = context.new_page()
    # To open a new tab

    page.goto("https://rahulshettyacademy.com/")
    # Hitting URL in the browser


# ----------------------------------------------------------------

def test_playwrightShortCut(page: Page):
    # This can be implemented only in case of running test in chromium headless mode on 1 single context
    # If we need to run this test in Firefox this won't work
    # page fixture has default implementation with headless=True
    # To run in the headed mode, make these settings > Goto - Modify Run Configuration - Additional Arguments as - '--headed'

    page.goto("https://rahulshettyacademy.com/")


# ----------------------------------------------------------------

def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning123")
    # The tag should be starting with <label></label>
    # The <input> should be wrapped in the label tags OR both should be linked with a reference 'for'

    page.get_by_role("radio", name="admin").click()  # Radio button selection
    page.get_by_role("combobox").select_option("teach")  # Dropdown selection
    page.locator("#terms").check()  # To check checkbox/Here, we used CSS locators #id or.className
    page.get_by_role("link", name="terms and conditions").click()  # Clicking on the link
    time.sleep(5)
    page.get_by_role("button", name="Sign In").click()  # Clicking on the button

    # In case of wrong creds are entered need to catch the error message -
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()  # Assertion


# ----------------------------------------------------------------

def test_firefoxBrowser(playwright: Playwright):
    # firefoxBrowser = playwright.firefox
    # browser = firefoxBrowser.launch(headless=False)
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning123")
    # The tag should be starting with <label></label>
    # The <input> should be wrapped in the label tags OR both should be linked with a reference 'for'

    page.get_by_role("radio", name="admin").click()  # Radio button selection
    page.get_by_role("combobox").select_option("teach")  # Dropdown selection
    page.locator("#terms").check()  # To check checkbox/Here, we used CSS locators #id or.className
    page.get_by_role("link", name="terms and conditions").click()  # Clicking on the link
    time.sleep(5)
    page.get_by_role("button", name="Sign In").click()  # Clicking on the button

    # In case of wrong creds are entered need to catch the error message -
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()  # Assertion
