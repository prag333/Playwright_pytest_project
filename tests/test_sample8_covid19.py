from pages.home_page import HomePage
from pages.covid19_page import Covid19Page


def test_verify_covid19_page(driver):
    url = "https://www.pfizerforall.com/"
    home_page = HomePage(driver)
    covid19_page = Covid19Page(driver)

    home_page.go_to_homepage(url)
    assert "Pfizer" in driver.title()
    home_page.click_accept_cookies()

    home_page.scroll_to_element(home_page.COVID19_GET_STARTED_BUTTON)
    home_page.click_covid19_get_started()
    home_page.wait_for_timeout(3)
    current_url = home_page.get_url()
    assert current_url == "https://www.pfizerforall.com/respiratory/", "Url does not match"

    assert covid19_page.is_visible(covid19_page.PNEUMONIA)
    assert covid19_page.is_visible(covid19_page.FLU)
    assert covid19_page.is_visible(covid19_page.RSV)
    assert covid19_page.is_visible(covid19_page.TALK_TO_A_DOCTOR_BUTTON)
    assert covid19_page.is_visible(covid19_page.FREQUENTLY_ASKED_QUETIONS_1ST_QUESTION)
    covid19_page.click_frequently_asked_quetions_1st_question()
    assert covid19_page.is_visible(covid19_page.FREQUENTLY_ASKED_QUETIONS_2ND_QUESTION)
    covid19_page.click_frequently_asked_quetions_2nd_question()
    assert covid19_page.is_visible(covid19_page.KEEP_UP_WITH_VACCINATIONS_CARD)
    # covid19_page.click_keep_up_with_vaccinations_card()
    assert covid19_page.is_visible(covid19_page.GO_T0_THE_GUIDE_BUTTON)
    # covid19_page.click_go_to_the_guide_button()
    assert covid19_page.is_visible(covid19_page.MAKE_AN_APPOINTMENT_BUTTON)
    covid19_page.click_make_an_appointment_button()
