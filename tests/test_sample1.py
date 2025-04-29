from pages.home_page import HomePage


def test_verify_sections(driver):
    url = "https://www.pfizerforall.com/"
    home_page = HomePage(driver)
    home_page.go_to_homepage(url)
    assert "Pfizer" in driver.title()
    home_page.click_accept_cookies()
    home_page.scroll_to_element(home_page.TAKE_HEALTH_QUESTIONNAIRES_BUTTON)

    assert home_page.is_visible(home_page.TAKE_HEALTH_QUESTIONNAIRES), "Take health questionnaires button is not visible"
    assert home_page.is_visible(home_page.TAKE_HEALTH_QUESTIONNAIRES_BUTTON), "Take health questionnaires button is not visible"
    assert home_page.is_visible(home_page.MANAGE_MIGRAINE), "Manage health questionnaires button is not visible"
    assert home_page.is_visible(home_page.MANAGE_MIGRAINE_BUTTON), "Manage health questionnaires button is not visible"
    assert home_page.is_visible(home_page.NAVIGATE_MENOPAUSE), "Navigate icon button is not visible"
    assert home_page.is_visible(home_page.NAVIGATE_MENOPAUSE_BUTTON), "Navigate icon button is not visible"
    assert home_page.is_visible(home_page.SCHEDULE_VACCINES), "Schedule vaccines button is not visible"
    assert home_page.is_visible(home_page.SCHEDULE_VACCINES_BUTTON), "Schedule vaccines button is not visible"
    assert home_page.is_visible(home_page.SAVE_ON_PFIZER_MEDICATIONS), "Save on pfizer medications button is not visible"
    assert home_page.is_visible(home_page.SAVE_ON_PFIZER_MEDICATIONS_BUTTON), "Save on pfizer medications button is not visible"
    assert home_page.is_visible(home_page.GET_ANSWERS_TO_HEALTH_AND_WELLNESS_QUESTIONS), "Get answers to health questionnaires button is not visible"
    assert home_page.is_visible(home_page.GET_ANSWERS_TO_HEALTH_AND_WELLNESS_QUESTIONS_BUTTON), "Get answers to health questionnaires button is not visible"
    assert home_page.is_visible(home_page.COVID19_GET_STARTED_BUTTON)
