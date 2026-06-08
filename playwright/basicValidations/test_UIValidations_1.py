from playwright.sync_api import Page, expect


def test_UIValidationDynamicScript(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("radio", name="admin").click()  # Radio button selection
    page.get_by_role("combobox").select_option("teach")  # Dropdown selection
    page.locator("#terms").check()  # To check checkbox/Here, we used CSS locators #id or.className
    page.get_by_role("link", name="terms and conditions").click()  # Clicking on the link
    page.get_by_role("button", name="Sign In").click()  # Clicking on the button

    # iphone X, Nokia edge -> Verify 2 items are showing in the cart
    # Get all the item_cards & then get iphone X, Nokia edge

    # Adding 2 elements in the Cart
    prod_iphoneX = page.locator("app-card").filter(has_text="iphone X")
    prod_iphoneX.get_by_role("button").click()
    prod_nokiaEdge = page.locator("app-card").filter(has_text="Nokia Edge")
    prod_nokiaEdge.get_by_role("button").click()

    # Clicking on the checkout button
    page.get_by_text("Checkout").click()

    # Assertions
    expect(page.locator(".media-body")).to_have_count(2)  # To check if 2 elements added into the cart
    expect(page.get_by_text("iphone X")).to_be_visible()
    expect(page.get_by_text("Nokia Edge")).to_be_visible()


# ----------------------------------------------------------------

def test_childWindowHandle(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newPage_info:  # Creating object as a new page/PageClosure
        page.locator(".blinkingText[href='https://rahulshettyacademy.com/documents-request']").click()  # New page
        childPage = newPage_info.value  # Accessing child page
        text = childPage.locator(".red").text_content()
        print(text)

        # mentor@rahulshettyacademy.com - check text contains this
        # Please email us at mentor@rahulshettyacademy.com with below template to receive response
        # We need to split this
        words_0 = text.split(
            "at")  # 0 = 'Please email us at' & 1 = 'mentor@rahulshettyacademy.com with below template to receive response'
        email = words_0[1].strip().split(" ")[
            0]  # 0 - 'mentor@rahulshettyacademy.com' & 1 - 'with below template to receive response'
        assert email == "mentor@rahulshettyacademy.com"
