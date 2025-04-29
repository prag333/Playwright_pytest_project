from pages import covid19_page
from pages.vaccines_overview_page import  VaccinesOverviewPage
from pages.home_page import HomePage

def test_verify_covid19_overview_page(driver):
    url = "https://www.pfizerforall.com/"
    vaccines_page = VaccinesOverviewPage(driver)
    home_page = HomePage(driver)

    home_page.go_to_homepage(url)
    assert "Pfizer" in driver.title()
    assert home_page.is_visible(covid19_page.ACCEPT_ALL)
    home_page.click_accept_cookies()

    vaccines_page.click_menu()
    vaccines_page.click_vaccines()
    vaccines_page.click_vaccines_overview()
    assert vaccines_page.is_visible(vaccines_page.VACCINES_OVERVIEW_HEADER)
    assert vaccines_page.is_visible(vaccines_page.VACCINES_OVERVIEW_HEADER_TEXT)
    assert vaccines_page.is_visible(vaccines_page.VACCINES_OVERVIEW_P_TEXT)
    assert vaccines_page.is_visible(vaccines_page.CHECK_YOUR_VACCINE_ELIGIBILITY_BUTTON)
    assert vaccines_page.is_visible(vaccines_page.FIND_AND_SCHEDULE_NOW_BUTTON)
    vaccines_page.click_check_your_vaccine_eligibility_button()
    vaccines_page.click_find_and_schedule_now_button()