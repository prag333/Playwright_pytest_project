from pages.home_page import HomePage
from pages.menopause_page import MenopausePage


def test_verify_menopause_page(driver):
    url = "https://www.pfizerforall.com/"
    home_page = HomePage(driver)
    menopause_page = MenopausePage(driver)

    home_page.go_to_homepage(url)
    assert "Pfizer" in driver.title()
    home_page.click_accept_cookies()
    home_page.scroll_to_element(home_page.NAVIGATE_MENOPAUSE_SECTION)

    # Menopause section
    home_page.scroll_to_element(home_page.NAVIGATE_MENOPAUSE_BUTTON)
    home_page.click_menopause_section()
    home_page.wait_for_timeout(3)
    current_url = home_page.get_url()
    assert current_url == "https://www.pfizerforall.com/menopause", "Url does not match"

    assert menopause_page.is_visible(menopause_page.VASOMOR_SYMPTOMS_VMS)
    assert menopause_page.is_visible(menopause_page.SLEEP_DISTURBANCES)
    assert menopause_page.is_visible(menopause_page.GENITOURINARY_SYNDROME_OF_MENOPAUSE)
    assert menopause_page.is_visible(menopause_page.MOOD_AND_COGNITIVE_DISTURBANCES)
    assert menopause_page.is_visible(menopause_page.KEEP_UP_WITH_VACCINATIONS)
    assert menopause_page.is_visible(menopause_page.KEEP_UP_WITH_VACCINATIONS_BUTTON)
    # menopause_page.click_keep_up_with_vaccinations_button()
    assert menopause_page.is_visible(menopause_page.TALK_TO_A_DOCTOR)
    assert menopause_page.is_visible(menopause_page.TALK_TO_A_DOCTOR_BUTTON)
    menopause_page.click_talk_to_a_doctor_section()
