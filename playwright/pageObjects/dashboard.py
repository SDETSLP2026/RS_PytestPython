from .ordersHistory import OrdersHistoryPage


class Dashboard:

    def __init__(self, page):
        self.page = page

    def selectOrdersNavLink(self):
        self.page.get_by_role("button", name="ORDERS").click()

        # As we know after clicking on ORDERS - we are landing on to the orderHistoryPage page, we are creating object here itself
        ordersHistoryPage = OrdersHistoryPage(self.page)
        return ordersHistoryPage
