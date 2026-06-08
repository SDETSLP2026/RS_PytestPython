from tkinter.filedialog import dialogstates

from playwright.sync_api import Page, expect


# https://rahulshettyacademy.com/AutomationPractice/

def test_UIChecks(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    # hide/display and placeholder locator
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    # ----------------------------------------------------------------

    # AlertBoxes
    # functions without names are called Anonymous functions and to handle such functions lambda is used in Python

    page.on("dialog", lambda dialog: dialog.accept())  # To click on Okay button on the alert popup box
    page.get_by_role("button", name="Confirm").click()

    # ----------------------------------------------------------------

    # FrameHandling
    # Frames - An HTML page which is embedded in another HTML page (which is not a part of base page)
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")

    # ----------------------------------------------------------------

    # MouseHover & selecting from the dropdown
    page.locator("#mousehover").hover()
    page.get_by_role("link",name="Top").click()


    page.locator("#mousehover").hover()
    page.get_by_role("link",name="Reload").click()

    # ----------------------------------------------------------------

    # WebTables - Check the price of Rice = 37
    # The main challenge is the elements can be moved anywhere, need to handle smartly
    # Identify the Price column
    # Identify the Rice row
    # Extract the price of the rice

    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    # Identify the Price column
    # countOfColumns = page.locator("th").count()
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            priceColValue = index
            print(f"Price column value is:- {priceColValue}")
            break

    # Identify the Rice row
    riceRow = page.locator("tr").filter(has_text="Rice")

    # Extract the price of the rice
    # page.locator("td") - This will give almost 15 elements
    # riceRow.locator("td") - This will return only 3 elements
    expect(riceRow.locator("td").nth(priceColValue)).to_have_text("37") # This will return 3 elements
