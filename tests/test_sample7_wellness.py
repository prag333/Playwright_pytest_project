from pages.home_page import HomePage
from pages.wellness_page import WellnessPage


def test_verify_wellness_page(driver):
    url = "https://www.pfizerforall.com/"
    home_page = HomePage(driver)
    wellness_page = WellnessPage(driver)

    home_page.go_to_homepage(url)
    assert "Pfizer" in driver.title()
    home_page.click_accept_cookies()
    home_page.scroll_to_element(home_page.HEALTH_AND_WELLNESS_MEDICATIONS_SECTION)

    # Menopause section
    home_page.scroll_to_element(home_page.GET_ANSWERS_TO_HEALTH_AND_WELLNESS_QUESTIONS_BUTTON)
    home_page.click_health_wellness_section()
    home_page.wait_for_timeout(3)
    current_url = home_page.get_url()
    assert current_url == "https://www.pfizerforall.com/#health-wellness", "Url does not match"

    assert wellness_page.is_visible(wellness_page.CANCER_BUTTON)
    wellness_page.click_cancer_button()
    assert wellness_page.is_visible(wellness_page.MAIN_MENU)
    wellness_page.click_main_menu_button()
    assert wellness_page.is_visible(wellness_page.COVID19_GET_STARTED)
    assert wellness_page.is_visible(wellness_page.LEARN_MORE_ABOUT_SYMPTOMS)
    assert wellness_page.is_visible(wellness_page.HEALTH_QUESTIONNAIRES_BUTTON)
    wellness_page.click_health_questionnaries_button()
    # assert wellness_page.is_visible(wellness_page.NAVIGATE_MENOPAUSE_BUTTON)
    # wellness_page.click_navigate_menopause_button()

