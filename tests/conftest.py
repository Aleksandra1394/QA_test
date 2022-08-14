import pytest
import requests
import csv


def pytest_addoption(parser):
    parser.addoption("--url", default="https://restful-booker.herokuapp.com/", help="This is request url")



@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")