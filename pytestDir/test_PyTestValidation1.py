# To check pytest configurations with playwright
# Fixtures - reusable code across multiple test cases
import pytest


# @pytest.fixture
# @pytest.fixture(scope="module") # This will run only once for all the TCs
# @pytest.fixture(scope="class") # This will run only once for the classes
# @pytest.fixture(scope="session") # This will run only once for a session

@pytest.fixture(scope="module")  # This will run for all the TCs/functions
def preWork():
    print("Inside preWork - I setup preWork instance")
    return "pass"

@pytest.mark.smoke #Tagging to run specific tests across multiple test files
@pytest.fixture(scope="function")  # This will run for all the TCs/functions
def secondWork():
    print("Inside preWork - I setup secondWork instance")  # SetUp
    yield  # pause
    print("Inside preWork - I setup tearDown instance")  # TearDown


def test_InitialCheck(preWork, secondWork):  # Need to mention 'test' at the start or end
    print("This is the first test")
    assert preWork == "pass"


@pytest.mark.skip # To skip a single test
def test_SecondCheck(preSetupWork, secondWork):  # Need to mention 'test' at the start or end
    print("This is the Second test")
