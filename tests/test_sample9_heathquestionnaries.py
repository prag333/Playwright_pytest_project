from pages.home_page import HomePage
from pages.healthquestionnaires_page import HealthquestionnairesPage


def test_verify_healthquestionnaires_page(driver):
    url = "https://www.pfizerforall.com/"
    home_page = HomePage(driver)
    healthquestionnaires_page = HealthquestionnairesPage(driver)

    home_page.go_to_homepage(url)
    assert "Pfizer" in driver.title()
    home_page.click_accept_cookies()

    home_page.scroll_to_element(home_page.TAKE_HEALTH_QUESTIONNAIRES_BUTTON)
    home_page.click_questionaries_section()
    home_page.wait_for_timeout(3)
    current_url = home_page.get_url()
    assert current_url == "https://www.pfizerforall.com/healthquestionnaires", "Url does not match"

    assert healthquestionnaires_page.is_visible(healthquestionnaires_page.CANCER_BUTTON)
    healthquestionnaires_page.click_cancer_button()
    assert healthquestionnaires_page.is_visible(healthquestionnaires_page.HEART_HEALTH_BUTTON)
    healthquestionnaires_page.click_heart_health_button()
    assert healthquestionnaires_page.is_visible(healthquestionnaires_page.MIGRAINE_BUTTON)
    healthquestionnaires_page.click_migraine_button()
    assert healthquestionnaires_page.is_visible(healthquestionnaires_page.VACCINS_BUTTON)
    healthquestionnaires_page.click_vaccins_button()
    assert healthquestionnaires_page.is_visible(healthquestionnaires_page.FIRST_NAME)
    healthquestionnaires_page.click_first_name()
    assert healthquestionnaires_page.is_visible(healthquestionnaires_page.ASK_A_QUESTION)
    healthquestionnaires_page.click_ask_a_question()
