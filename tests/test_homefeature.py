import pytest
from pages.homefeature_page import HomeFeaturePage
from pages.home_page import HomePage
from tests.conftest import driver
import logging

logger = logging.getLogger(__name__)


class TestHomeFeaturePage:

    @pytest.fixture(autouse=True)
    def setup(self, driver, BASE_URL):
        self.base_url = BASE_URL
        self.homefeature_page = HomeFeaturePage(driver)
        self.home_page = HomePage(driver)

        logger.info("Common steps for HomeFeaturePage")
        self.home_page.go_to_homepage(self.base_url)
        assert "Pfizer" in driver.title()
        logger.info("Verifying the Accept all displayed")
        assert self.homefeature_page.is_visible(self.homefeature_page.ACCEPT_ALL, timeout=30)
        logger.info("Click the Accept all")
        self.home_page.click_accept_cookies()
        logger.info("Scroll to the pfizer for all logo")
        self.homefeature_page.scroll_to_element(self.homefeature_page.PFIZER_FOR_ALL_LOGO)
        logger.info("Scroll to the MENU")
        self.homefeature_page.scroll_to_element(self.homefeature_page.MENU)

    def test_verify_the_display_of_pfizerforall_logo_and_menu_section(self):

        logger.info("Test verify_the_display_of_pfizerforall_logo_and_menu_section")
        logger.info("Click the Menu button")
        self.homefeature_page.click_menu()
        logger.info("Verify the Get help")
        assert "Get Help With" in self.homefeature_page.get_text(self.homefeature_page.GET_HELP_WITH_TEXT_IS), \
            "GET_HELP_WITH_TEXT_IS is not displayed"
        logger.info(f"Checking the covid19 flu text is: {self.homefeature_page.get_text(self.homefeature_page.COVID19_FLU_TEXT_IS)}")
        assert "COVID-19 & flu" in self.homefeature_page.get_text(self.homefeature_page.COVID19_FLU_TEXT_IS), \
            "COVID-19 & flu text is not displayed"
        logger.info(f"Verifying the migraine text is: {self.homefeature_page.get_text(self.homefeature_page.MIGRAINE_TEXT_IS)}")
        assert "Migraine" in self.homefeature_page.get_text(self.homefeature_page.MIGRAINE_TEXT_IS), \
            "Migraine is not displayed"
        logger.info(f"Verifying Vaccines text is: {self.homefeature_page.get_text(self.homefeature_page.VACCINES_TEXT_IS)}")
        assert "Vaccines" in self.homefeature_page.get_text(self.homefeature_page.VACCINES_TEXT_IS), \
            "Vaccines is not displayed"
        logger.info(f"Verifying Menopause text is: {self.homefeature_page.get_text(self.homefeature_page.MENOPAUSE_TEXT_IS)}")
        assert  "Menopause" in self.homefeature_page.get_text(self.homefeature_page.MENOPAUSE_TEXT_IS), \
            "Menopause is not displayed"
        logger.info(f"Verifying the Health Questionnaires text is: {self.homefeature_page.get_text(self.homefeature_page.HEALTH_QUESTIONNAIRES_TEXT_IS)}")
        assert "Health questionnaires" in self.homefeature_page.get_text(self.homefeature_page.HEALTH_QUESTIONNAIRES_TEXT_IS), \
            "Health questionnaires is not displayed"
        logger.info(f"Verifying the Save on pfizer med text is: {self.homefeature_page.get_text(self.homefeature_page.SAVE_ON_PFIZER_MED_TEXT)}")
        assert "Save on Pfizer medications" in self.homefeature_page.get_text(self.homefeature_page.SAVE_ON_PFIZER_MED_TEXT), \
            "Save on Pfizer medications is not displayed"
        logger.info(f"Verifying the Additional resources text is: {self.homefeature_page.get_text(self.homefeature_page.ADDITIONAL_RESOURCES_TEXT_IS)}")
        assert "Additional Resources" in self.homefeature_page.get_text(self.homefeature_page.ADDITIONAL_RESOURCES_TEXT_IS), \
            "Additional Resources is not displayed"
        logger.info(f"Verifying the Support text is: {self.homefeature_page.get_text(self.homefeature_page.SUPPORT_TEXT_IS)}")
        assert "Support" in self.homefeature_page.get_text(self.homefeature_page.SUPPORT_TEXT_IS), \
            "Support is not displayed"
        self.home_page.wait_for_timeout(15)
        logger.info("Verify the Close Button is visible")
        assert self.homefeature_page.is_visible(self.homefeature_page.CLOSE_BTN), "Close is not displayed"

    def test_verify_the_welcome_to_pfizerforalltm_section(self):
        logger.info("Test verify the welcome to pfizerforalltm section")
        logger.info("Click the menu button")
        self.homefeature_page.click_menu()
        logger.info("Verify the Home is displayed")
        assert self.homefeature_page.is_visible(self.homefeature_page.HOME), "Home is not displayed"
        logger.info("Click the Home button")
        self.homefeature_page.click_home()
        self.home_page.wait_for_timeout(1)
        logger.info(f"Verifying the Checking Support text is: {self.homefeature_page.get_text(self.homefeature_page.NAVIGATE_MENOPAUSE_TEXT_IS)}")
        assert "Navigate menopause" in self.homefeature_page.get_text(self.homefeature_page.NAVIGATE_MENOPAUSE_TEXT_IS), \
            "Navigate menopause is not displayed"
        logger.info("Click the Navigate menopause button")
        self.homefeature_page.click_navigate_menopause()
        logger.info("Verify the Menopause text in the title")
        assert 'Menopause' in self.homefeature_page.get_title(), "Menopause is not displayed"
        logger.info("Go back to the previous page")
        self.home_page.go_back_to_previous_page()
        self.home_page.wait_for_timeout(1)
        logger.info(f"Verifying the Manage migraine text is: {self.homefeature_page.get_text(self.homefeature_page.MANAGE_MIGRAINE_TEXT_IS)}")
        assert "Manage migraine" in self.homefeature_page.get_text(self.homefeature_page.MANAGE_MIGRAINE_TEXT_IS), \
             "Manage migraine text is not displayed"
        logger.info("Click the Manage migraine button")
        self.homefeature_page.click_manage_migraine()
        logger.info("PfizerForAll text in the title")
        assert "PfizerForAll" in self.homefeature_page.get_title(), "PfizerForAll text is not displayed"
        logger.info("Go back to the previous page")
        self.home_page.go_back_to_previous_page()
        self.home_page.wait_for_timeout(1)
        logger.info(f"Verifying the Schedule vaccines text is: {self.homefeature_page.get_text(self.homefeature_page.SCHEDULE_VACCINES_TEXT_IS)}")
        assert "Schedule vaccines" in self.homefeature_page.get_text(self.homefeature_page.SCHEDULE_VACCINES_TEXT_IS), \
            "Schedule vaccines is not displayed"
        logger.info("Click the Schedule Vaccines button")
        self.homefeature_page.click_schedule_vaccines()
        logger.info("Respiratory Vaccine Finder & Options | PfizerForAll™ text in the title")
        assert "Respiratory Vaccine Finder & Options | PfizerForAll™" in self.homefeature_page.get_title(), "Respiratory Vaccines is not displayed"
        logger.info("Go back to the previous page")
        self.home_page.go_back_to_previous_page()
        self.home_page.wait_for_timeout(1)
        logger.info("Verify the save on pfizer med is displayed")
        assert self.homefeature_page.is_visible(self.homefeature_page.SAVE_ON_PFIZER_MED), \
            "Manage migraine text is not displayed"
        logger.info(f"Verifying the Save on pfizer med text is: {self.homefeature_page.get_text(self.homefeature_page.SAVE_ON_PFIZER_MED_TEXT_IS)}")
        assert "Save on Pfizer medications" in self.homefeature_page.get_text(self.homefeature_page.SAVE_ON_PFIZER_MED_TEXT_IS), \
            "Save on Pfizer medications is not displayed"
        logger.info("Click the save on pfizer med button")
        self.homefeature_page.click_save_on_pfizer_med()
        logger.info("Prescription Assistance | PfizerForAll™ text in the title")
        assert "Prescription Assistance | PfizerForAll™" in self.homefeature_page.get_title(), "Prescription Assistance is not displayed"
        self.home_page.go_back_to_previous_page()
        logger.info("Go back to the previous page")
        self.home_page.wait_for_timeout(1)
        logger.info(f"Verifying the Take health question text is: {self.homefeature_page.get_text(self.homefeature_page.TAKE_HEALTH_QUESTION_TEXT_IS)}")
        assert "Take health questionnaires" in self.homefeature_page.get_text(self.homefeature_page.TAKE_HEALTH_QUESTION_TEXT_IS), \
            "Take health questionnaires is not displayed"
        logger.info("Click take health Question button")
        self.homefeature_page.click_take_health_question()
        logger.info("Be Your Own Champion | PfizerForAll™ text in the title")
        assert "Be Your Own Champion | PfizerForAll™" in self.homefeature_page.get_title(), "Be Your Own Champion is not displayed"
        logger.info("Go back to the previous page")
        self.home_page.go_back_to_previous_page()
        self.home_page.wait_for_timeout(1)
        logger.info(f"Verifying the Get answers to health and wellness questions text is: {self.homefeature_page.get_text(self.homefeature_page.GET_ANSWERS_TO_HEALTH_AND_WELLNESS_QUESTIONS_TEXT_IS)}")
        self.homefeature_page.get_text(self.homefeature_page.GET_ANSWERS_TO_HEALTH_AND_WELLNESS_QUESTIONS_TEXT_IS), \
            "Get answers to health and wellness questions is not displayed"

    def test_verify_two_cards_section(self):
        logger.info("Test Verify two cards section")
        logger.info("Click menu section")
        self.homefeature_page.click_menu()
        logger.info("Verify the Home is displayed")
        assert self.homefeature_page.is_visible(self.homefeature_page.HOME), "Home is not displayed"
        logger.info("Click the Home button")
        self.homefeature_page.click_home()
        self.homefeature_page.wait_for_timeout(1)
        logger.info("Verify Flu title is displayed")
        assert self.homefeature_page.is_visible(self.homefeature_page.FLU_TITLE), "Flu title is not displayed"
        logger.info(f"Verifying the Flu title text is: {self.homefeature_page.get_text(self.homefeature_page.FLU_TITLE_TEXT_IS)}")
        assert "COVID‑19, flu, or just a cold? Let’s find out." in self.homefeature_page.get_text(self.homefeature_page.FLU_TITLE_TEXT_IS), "Flu title is not displayed"
        logger.info(f"Verifying the Flu text text is: {self.homefeature_page.get_text(self.homefeature_page.FLU_TEXT_TEXT_IS)}")
        assert "Take a step towards feeling better with quick access to doctors, tests, and treatments." in self.homefeature_page.get_text(self.homefeature_page.FLU_TEXT_TEXT_IS), \
            "Flu text is not displayed"
        logger.info("Verify flu get started button is displayed")
        assert self.homefeature_page.is_visible(self.homefeature_page.FLU_GET_STARTED_BUTTON), \
            "Flu get started button is not displayed"
        logger.info("Scroll to the flu get started button")
        self.homefeature_page.scroll_to_element(self.homefeature_page.FLU_GET_STARTED_BUTTON)
        self.homefeature_page.wait_for_timeout(2)
        logger.info("Click to the flu get started button")
        self.homefeature_page.click_ful_get_started_button()
        self.homefeature_page.wait_for_timeout(1)
        logger.info("Get the url")
        assert f"{self.base_url}/respiratory/" in self.homefeature_page.get_url()
        logger.info("Go back to the previous page")
        self.home_page.go_back_to_previous_page()
        self.home_page.wait_for_timeout(3)
        logger.info("Scroll to the Migraine Title")
        self.homefeature_page.scroll_to_element(self.homefeature_page.MIGRAINE_TITLE)
        logger.info(f"Verifying the Migraine Title text is: {self.homefeature_page.get_text(self.homefeature_page.MIGRAINE_TITLE_TEXT_IS)}")
        assert "A newer way to manage migraine is here." in self.homefeature_page.get_text(self.homefeature_page.MIGRAINE_TITLE_TEXT_IS), \
            "Migrate title text is not displayed"
        logger.info(f"Verifying the Migraine Text text is: {self.homefeature_page.get_text(self.homefeature_page.MIGRAINE_TEXT_TEXT_IS)}")
        assert "Talk to a doctor about options that may be right for you." in self.homefeature_page.get_text(self.homefeature_page.MIGRAINE_TEXT_TEXT_IS), \
            "Migraine text text is not displayed"
        self.homefeature_page.wait_for_timeout(1)
        logger.info("Scroll to the migraine get started button")
        self.homefeature_page.scroll_to_element(self.homefeature_page.MIGRAINE_GET_STARTED_BUTTON)
        logger.info("Click the migraine get started button")
        self.homefeature_page.click_migraine_get_started_button()
        self.homefeature_page.wait_for_timeout(1)
        logger.info("Get the url")
        assert f"{self.base_url}/migraine/" in self.homefeature_page.get_url()

    def test_verify_prevention_card(self):
        logger.info("Test verify prevention card")
        logger.info("Click menu section")
        self.homefeature_page.click_menu()
        logger.info("Verify Home is displayed ")
        assert self.homefeature_page.is_visible(self.homefeature_page.HOME), "Home is not displayed"
        logger.info("click home button")
        self.homefeature_page.click_home()
        logger.info("Scroll to the prevention title")
        self.homefeature_page.scroll_to_element(self.homefeature_page.PREVENTION_TITLE)
        logger.info("Verify Prevention title is displayed")
        assert self.homefeature_page.is_visible(self.homefeature_page.PREVENTION_TITLE), "Prevention title is not displayed"
        logger.info(f"Verifying the Prevention title text is: {self.homefeature_page.get_text(self.homefeature_page.PREVENTION_TITLE_TEXT_IS)}")
        assert "Find and schedule vaccines you and your family may be eligible for." in self.homefeature_page.get_text(self.homefeature_page.PREVENTION_TITLE_TEXT_IS), \
            "Prevention title is not displayed"
        logger.info("Verify prevention get started is displayed")
        assert self.homefeature_page.is_visible(self.homefeature_page.PREVENTION_GET_STARTED), "Prevention get started button is not displayed"
        logger.info("Click the prevention get started button")
        self.homefeature_page.click_prevention_get_started()
        logger.info("Get the url")
        assert f"{self.base_url}/vaccine-options" in self.homefeature_page.get_url()

    def test_verify_prevention_card_afford_your_pfizer_medications(self):
        logger.info("Test verify prevention card afford your pfizer medications")
        logger.info("Click menu section")
        self.homefeature_page.click_menu()
        logger.info("Verify Home is visible ")
        assert self.homefeature_page.is_visible(self.homefeature_page.HOME), "Home is not displayed"
        logger.info("click home button")
        self.homefeature_page.click_home()
        self.home_page.wait_for_timeout(3)
        logger.info("Scroll to the header")
        self.homefeature_page.scroll_to_element(self.homefeature_page.HEADER)
        logger.info("Verify Header is displayed")
        assert self.homefeature_page.is_visible(self.homefeature_page.HEADER), "Home is not displayed"
        logger.info(f"Verifying the Header text is: {self.homefeature_page.get_text(self.homefeature_page.HEADER_TEXT)}")
        assert "We’re committed to helping you afford your Pfizer medications." in self.homefeature_page.get_text(self.homefeature_page.HEADER_TEXT), \
            "Header text is not displayed"
        logger.info("Verify Describe is displayed")
        assert self.homefeature_page.is_visible(self.homefeature_page.DESCRIBE), "Describe is not displayed"
        logger.info(f"Verifying the Describe text is: {self.homefeature_page.get_text(self.homefeature_page.DESCRIBE_TEXT)}")
        assert (("From co-pay cards to assistance with information on the prior authorization process, "
                "we’re here to help with your prescribed Pfizer medications. And if you’re eligible for our programs, "
                "we can also help you get access to your prescribed medications regardless of income.")
                in self.homefeature_page.get_text(self.homefeature_page.DESCRIBE_TEXT)), "Header text is not displayed"
        logger.info("Click get Started button")
        self.homefeature_page.click_get_started()
        logger.info("Get the url")
        assert f"{self.base_url}/prescription-assistance" in self.homefeature_page.get_url()

    def test_verify_disclaimer_text_on_home_page(self):
        logger.info("Test verify disclaimer text on home page")
        logger.info("Click menu section")
        self.homefeature_page.click_menu()
        logger.info("Verify the Home is displayed")
        assert self.homefeature_page.is_visible(self.homefeature_page.HOME), "Home is not displayed"
        logger.info("Click home button")
        self.homefeature_page.click_home()
        logger.info(f"Verifying the Disclaimer text is: {self.homefeature_page.get_text(self.homefeature_page.DISCLAIMER_TEXT)}")
        assert ("FOR U.S. RESIDENTS ONLY. The information provided is for educational purposes only and is not intended "
                "to replace discussions with a healthcare professional.© 2025 Pfizer Inc. All rights reserved. "
                "PP-UNP-USA-6048") in self.homefeature_page.get_text(self.homefeature_page.DISCLAIMER_TEXT), \
            "DISCLAIMER is not displayed"
