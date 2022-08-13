import requests


def test_invalid_date(base_url):
    res = requests.get(base_url + "breed/uncorrectbreed/images")
    assert res.status_code == 404
    assert res.json().get("status") == "error"


def test_saxes_date(base_url):
        res = requests.get(base_url + "breed/akita/images")
        assert res.status_code == 200
        assert res.json().get("status") == "success"
