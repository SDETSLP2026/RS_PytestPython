# To check pytest configurations with playwright
#Fixtures - reusable code across multiple test cases
import pytest


# @pytest.fixture
# @pytest.fixture(scope="module") # This will run only once for all the TCs
# @pytest.fixture(scope="class") # This will run only once for the classes

@pytest.mark.smoke #Tagging to run specific tests across multiple test files
def test_ThirdCheck(preSetupWork): #Need to mention 'test' at the start or end
    print("This is the Third test")

