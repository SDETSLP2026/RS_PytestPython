import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    ) # pytest test_framework_web_api.py --browser_name firefox
    parser.addoption(
        "--url_name", action="store", default="https://rahulshettyacademy.com/client/", help="server selection"
    ) # pytest test_framework_web_api.py --browser_name firefox --url_name https://rahulshettyacademy.com/client/


@pytest.fixture(scope="session")
def user_credentials(request):  # request is a global parameter
    return request.param

@pytest.fixture
def browserInstance(playwright, request):
    # pytest test_framework_web_api.py --browser_name firefox
    # By using this command we can run the test in the desired browsers
    # For this we are using global fixture - request

    browser_name = request.config.getoption("--browser_name")
    url_name = request.config.getoption("--url_name")
    if browser_name =="chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name =="firefox":
        browser = playwright.firefox.launch(headless=False)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=False)
    else:
        raise ValueError(f"Unsupported or missing browser name: '{browser_name}'")

    context = browser.new_context()
    page = context.new_page()
    page.goto(url_name)

    yield page

    context.close()
    browser.close()