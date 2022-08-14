import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome("C:\\Users\\serge\\PycharmProjects\\pythonProject2\\qa_test\\tests\\ui_tests\\chromedriver.exe")
    yield driver
    driver.quit()