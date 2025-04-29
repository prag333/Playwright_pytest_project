from pages.home_page import HomePage
from pages.pfizermedications import PfizermedicationsPage


def test_verify_pfizermedications_page(driver):
    url = "https://www.pfizerforall.com/"
    home_page = HomePage(driver)
    pfizermedications_page = PfizermedicationsPage(driver)

    home_page.go_to_homepage(url)
    assert "Pfizer" in driver.title()
    home_page.click_accept_cookies()
    home_page.scroll_to_element(home_page.SAVE_ON_PFIZER_MEDICATIONS_BUTTON)

    # Menopause section
    home_page.scroll_to_element(home_page.SAVE_ON_PFIZER_MEDICATIONS_BUTTON)
    home_page.click_prescription_assistance_section()
    home_page.wait_for_timeout(3)
    current_url = home_page.get_url()
    assert current_url == "https://www.pfizerforall.com/prescription-assistance", "Url does not match"

    assert pfizermedications_page.is_visible(pfizermedications_page.SUBMISSION)
    assert pfizermedications_page.is_visible(pfizermedications_page.REVIEW)
    assert pfizermedications_page.is_visible(pfizermedications_page.DECISION)
    assert pfizermedications_page.is_visible(pfizermedications_page.PRESCRIPTION)
    assert pfizermedications_page.is_visible(pfizermedications_page.PRIVATE_HEALTH_INSURANCE)
    pfizermedications_page.click_private_health_insurance_section()
    assert pfizermedications_page.is_visible(pfizermedications_page.PUBLIC_HEALTH_INSURANCE)
    pfizermedications_page.click_public_health_insurance_section()
    assert pfizermedications_page.is_visible(pfizermedications_page.UNDERSTAND_INSURANCE_REQUIREMENTS)
    pfizermedications_page.click_understand_insurance_requirements_button()
    assert pfizermedications_page.is_visible(pfizermedications_page.SAVINGS_AND_SUPPORT_FOR_ELIGIBLE_PATIENTS)
    assert pfizermedications_page.is_visible(pfizermedications_page.SAVINGS_AND_SUPPORT_FOR_ELIGIBLE_PATIENTS_BUTTON)
    pfizermedications_page.click_savings_and_support_for_eligible_patients_button()

