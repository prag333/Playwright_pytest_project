from pages.home_page import HomePage
from pages.migraine_page import MigrainePage


def test_verify_migraine_page(driver):
    url = "https://www.pfizerforall.com/"
    home_page = HomePage(driver)
    migraine_page = MigrainePage(driver)

    home_page.go_to_homepage(url)
    assert "Pfizer" in driver.title()
    home_page.click_accept_cookies()
    home_page.scroll_to_element(home_page.TAKE_HEALTH_QUESTIONNAIRES_BUTTON)

    # Migraine section
    home_page.scroll_to_element(home_page.MANAGE_MIGRAINE_BUTTON)
    home_page.click_migraine_section()
    home_page.wait_for_timeout(3)
    current_url = home_page.get_url()
    assert current_url == "https://www.pfizerforall.com/migraine/", "Url does not match"

    exp_learn_about_text = 'Learn about today’s migraine science'
    actual_learn_about_text = migraine_page.get_text(migraine_page.LEARN_ABOUT_TODAY_MIGRAINE_SCEIENCE)
    assert exp_learn_about_text == actual_learn_about_text, "Text does not match"
    assert migraine_page.is_visible(migraine_page.LEARN_ABOUT_TODAY_MIGRAINE_SCEIENCE)
    assert migraine_page.is_visible(migraine_page.EXPLORE_MIGRAINE_TREATMENT_OPTIONS)
    assert migraine_page.is_visible(migraine_page.TALK_TO_A_MIGRAINE_DOCTOR)
    assert migraine_page.is_visible(migraine_page.FIRST_NAME)
    assert migraine_page.is_visible(migraine_page.FREQUENTLY_ASKED_YOUR_QUESTIONS)
    # assert migraine_page.is_visible(migraine_page.TAKE_THE_QUIZ_SECTION)
    # migraine_page.click_take_the_quiz()
