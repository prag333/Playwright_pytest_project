from pages.home_page import HomePage
from pages.vaccine_page import VaccinePage


def test_verify_vaccine_page(driver):
    url = "https://www.pfizerforall.com/"
    home_page = HomePage(driver)
    vaccine_page = VaccinePage(driver)

    home_page.go_to_homepage(url)
    assert "Pfizer" in driver.title()
    home_page.click_accept_cookies()
    home_page.scroll_to_element(home_page.SCHEDULE_VACCINES_SECTION)

    # Menopause section
    home_page.scroll_to_element(home_page.SCHEDULE_VACCINES_BUTTON)
    home_page.click_vaccine_options_section()
    home_page.wait_for_timeout(3)
    current_url = home_page.get_url()
    assert current_url == "https://www.pfizerforall.com/vaccine-options", "Url does not match"

    assert vaccine_page.is_visible(VaccinePage.FIND_AND_SCHEDULE_NOW)
    assert vaccine_page.is_visible(VaccinePage.FIND_AND_SCHEDULE_NOW_BUTTON)
    vaccine_page.click_find_and_schedule_now_button()
    assert vaccine_page.is_visible(VaccinePage.CHECK_YOUR_VACCINE_ELIGIBILITY)
    assert vaccine_page.is_visible(vaccine_page.CHECK_YOUR_VACCINE_ELIGIBILITY_BUTTON)
    vaccine_page.click_check_your_vaccine_eligibility_button()
    assert vaccine_page.is_visible(vaccine_page.COVID19)
    assert vaccine_page.is_visible(VaccinePage.FLU)
    assert vaccine_page.is_visible(VaccinePage.FIRST_NAME)
    vaccine_page.click_first_name()
    assert vaccine_page.is_visible(VaccinePage.LAST_NAME)
    vaccine_page.click_last_name()
    assert vaccine_page.is_visible(VaccinePage.EMAIL_ADDRESS)
    vaccine_page.click_email_address()
