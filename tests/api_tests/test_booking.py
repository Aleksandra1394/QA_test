import pytest
import requests


@pytest.mark.smoke
def test_create_booking(base_url):
    info = {"firstname": "Jim", "lastname": "Brown", "totalprice": 111, "depositpaid": True,
            "bookingdates": {"checkin": "2023-01-01", "checkout": "2023-01-01"}, "additionalneeds": "Breakfast"}
    header = {"Content-Type": "application/json"}
    res = requests.post(base_url + "booking", json=info, headers=header)
    assert res.status_code == 200
    assert res.json().get("booking") == info


@pytest.mark.smoke
def test_get_valid_token(base_url):
    info = {"username": "admin", "password": "password123"}
    header = {"Content-Type": "application/json"}
    res = requests.post(base_url + "auth", json=info, headers=header)
    assert res.status_code == 200


@pytest.mark.regress
def test_delete_booking(base_url):
    info = {"username": "admin", "password": "password123"}
    header = {"Content-Type": "application/json"}
    res = requests.post(base_url + "auth", json=info, headers=header)
    token = res.json().get("token")
    info = {"firstname": "Jim", "lastname": "Brown", "totalprice": 111, "depositpaid": True,
            "bookingdates": {"checkin": "2023-01-01", "checkout": "2023-01-01"}, "additionalneeds": "Breakfast"}
    header = {"Content-Type": "application/json"}
    res = requests.post(base_url + "booking", json=info, headers=header)
    id1 = res.json().get("bookingid")
    cookie = "token=" + str(token)
    header = {"Content-Type": "application/json", "Cookie": cookie}
    res = requests.delete(base_url + "booking/" + str(id1), headers=header)
    assert res.status_code == 201


@pytest.mark.regress
def test_wrong_username(base_url):
    info = {"username": "error", "password": "password123"}
    header = {"Content-Type": "application/json"}
    res = requests.post(base_url + "auth", json=info, headers=header)
    assert res.status_code == 200


@pytest.mark.regress
def test_wrong_password(base_url):
    info = {"username": "admin", "password": "retyugfhr"}
    header = {"Content-Type": "application/json"}
    res = requests.post(base_url + "auth", json=info, headers=header)
    assert res.status_code == 200


@pytest.mark.regress
def test_empty_user(base_url):
    info = {"username": "", "password": "password123"}
    header = {"Content-Type": "application/json"}
    res = requests.post(base_url + "auth", json=info, headers=header)
    assert res.status_code == 200


@pytest.mark.regress
def test_empty_pass(base_url):
    info = {"username": "admin", "password": ""}
    header = {"Content-Type": "application/json"}
    res = requests.post(base_url + "auth", json=info, headers=header)
    assert res.status_code == 200


@pytest.mark.regress
def test_empty_user_empty_pass(base_url):
    info = {"username": "", "password": ""}
    header = {"Content-Type": "application/json"}
    res = requests.post(base_url + "auth", json=info, headers=header)
    assert res.status_code == 200


@pytest.mark.regress
def test_create_booking_without_name(base_url):
    info = {"firstname": "", "lastname": "", "totalprice": 111, "depositpaid": True,
            "bookingdates": {"checkin": "2023-01-01", "checkout": "2023-01-01"}, "additionalneeds": "Breakfast"}
    header = {"Content-Type": "application/json"}
    res = requests.post(base_url + "booking", json=info, headers=header)
    assert res.status_code == 200
    assert res.json().get("booking") == info


@pytest.mark.regress
def test_create_booking_without_date(base_url):
    info = {"firstname": "Jim", "lastname": "Brown", "totalprice": 111, "depositpaid": True,
            "bookingdates": {"checkin": "", "checkout": ""}, "additionalneeds": "Breakfast"}
    header = {"Content-Type": "application/json"}

    expected_info = {"firstname": "Jim", "lastname": "Brown", "totalprice": 111, "depositpaid": True,
            "bookingdates": {"checkin": "2022-08-14", "checkout": "2022-08-14"}, "additionalneeds": "Breakfast"}
    res = requests.post(base_url + "booking", json=info, headers=header)
    assert res.status_code == 200
    assert res.json().get("booking") == expected_info
