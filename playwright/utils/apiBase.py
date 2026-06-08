from playwright.sync_api import Playwright
ordersPayload = {"orders": [{"country": "India", "productOrderedId": "67a8dde5c0d3e6622a297cc8"}]}

class APIUtils:

    def getToken(self, playwright: Playwright ):

        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")

        response = api_request_context.post(
            "/api/ecom/auth/login",
            data={"userEmail": "sdetswapnil@gmail.com", "userPassword": "SDETsp#2025"})

        assert response.ok  # To ensure the test is pass (200 OK)
        print(response.json())  # To print response
        responseBody = response.json() # This is stored like a Dictionary i.e. Key:Value pair
        return responseBody["token"]


    def createOrder(self, playwright: Playwright):
        token = self.getToken(playwright) #This is to get token value
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")

        # request is a property which helps you to use with APIs
        response = api_request_context.post(
            "/api/ecom/order/create-order",
            data=ordersPayload,
            headers={"Authorization": token,
                     "Content-Type": "application/json"
                     })

        print(response.json()) # To print response
        responseBody = response.json()  # This is stored like a Dictionary i.e. Key:Value pair
        # {'orders': ['682f63925d3fd9ffa0ff9d65'], 'productOrderId': ['67a8dde5c0d3e6622a297cc8'], 'message': 'Order Placed Successfully'}
        orderId = responseBody["orders"][0] # Storing the first orderId from the list
        return orderId