import pytest


@pytest.fixture(scope="session") # This will run for all the TCs/functions
def preSetupWork():
    print("Inside preSetupWork - I setup browser instance")