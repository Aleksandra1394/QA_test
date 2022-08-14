from LoginPages import LoginHelper


def test_valid_login(browser):
    swag_labs_page = LoginHelper(browser)
    swag_labs_page.go_to_site()
    swag_labs_page.enter_login("standard_user")
    swag_labs_page.enter_password("secret_sauce")
    swag_labs_page.enter_button()
    #assert "Картинки" and "Видео" in elements



def test_wrong_login(browser):
    swag_labs_page = LoginHelper(browser)
    swag_labs_page.go_to_site()
    swag_labs_page.enter_login("qwertt_dgdr")
    swag_labs_page.enter_password("awrfcreee")
    swag_labs_page.enter_button()