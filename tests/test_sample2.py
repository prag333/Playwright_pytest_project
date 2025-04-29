from pages.home_page import HomePage


def test_verify_url_extensions(driver):
    url = "https://www.pfizerforall.com/"
    home_page = HomePage(driver)
    home_page.go_to_homepage(url)
    assert "Pfizer" in driver.title()
    home_page.click_accept_cookies()
    home_page.scroll_to_element(home_page.TAKE_HEALTH_QUESTIONNAIRES_BUTTON)

    # Questionaries section
    home_page.click_questionaries_section()
    home_page.wait_for_timeout(3)
    current_url = home_page.get_url()
    assert current_url == "https://www.pfizerforall.com/healthquestionnaires", "Url does not match"
    home_page.go_back_to_previous_page()

    # Migraine section
    home_page.scroll_to_element(home_page.MANAGE_MIGRAINE_BUTTON)
    home_page.click_migraine_section()
    home_page.wait_for_timeout(3)
    current_url = home_page.get_url()
    assert current_url == "https://www.pfizerforall.com/migraine/", "Url does not match"
    home_page.go_back_to_previous_page()

    # Menopause section
    home_page.scroll_to_element(home_page.MANAGE_MIGRAINE_BUTTON)
    home_page.click_menopause_section()
    home_page.wait_for_timeout(3)
    current_url = home_page.get_url()
    assert current_url == "https://www.pfizerforall.com/menopause", "Url does not match"
    home_page.go_back_to_previous_page()

    # vaccine-options section
    home_page.scroll_to_element(home_page.MANAGE_MIGRAINE_BUTTON)
    home_page.click_vaccine_options_section()
    home_page.wait_for_timeout(3)
    current_url = home_page.get_url()
    assert current_url == "https://www.pfizerforall.com/vaccine-options", "Url does not match"
    home_page.go_back_to_previous_page()

    # prescription-assistance section
    home_page.scroll_to_element(home_page.MANAGE_MIGRAINE_BUTTON)
    home_page.click_prescription_assistance_section()
    home_page.wait_for_timeout(3)
    current_url = home_page.get_url()
    assert current_url == "https://www.pfizerforall.com/prescription-assistance", "Url does not match"
    home_page.go_back_to_previous_page()

    # health-wellness section
    home_page.scroll_to_element(home_page.MANAGE_MIGRAINE_BUTTON)
    home_page.click_health_wellness_section()
    home_page.wait_for_timeout(3)
    current_url = home_page.get_url()
    assert current_url == "https://www.pfizerforall.com/#health-wellness", "Url does not match"
    home_page.go_back_to_previous_page()
