import pytest
from pages.covid19_inperson_appointment_page import Covid19InPersonAppointmentPage
from pages.home_page import HomePage
from tests.conftest import driver
import logging

logger = logging.getLogger(__name__)

class TestCovid19InPersonPage:

    @pytest.fixture(autouse=True)
    def setup(self, driver, BASE_URL):
        self.base_url = BASE_URL
        self.covid19_inperson_page = Covid19InPersonAppointmentPage(driver)
        self.home_page = HomePage(driver)

        logger.info("Common steps for Covid19TalkDoctorPage")
        self.home_page.go_to_homepage(self.base_url)
        assert "Pfizer" in driver.title()
        logger.info("Verify the accept all displayed")
        assert self.covid19_inperson_page.is_visible(self.covid19_inperson_page.ACCEPT_ALL, timeout=30)
        logger.info("Click the accept cookies")
        self.home_page.click_accept_cookies()
        logger.info("Scroll to the menu button")
        self.covid19_inperson_page.scroll_to_element(self.covid19_inperson_page.MENU_BUTTON)
        logger.info("Click the menu button")
        self.covid19_inperson_page.click_menu_button()
        logger.info(f"Checking the covid19 flu text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.COVID19_FLU_TEXT_IS)}")
        assert self.covid19_inperson_page.is_visible(self.covid19_inperson_page.COVID19_FLU_TEXT_IS), "Covid19 flu text is not displayed"
        logger.info("Click the covid19 flu button")
        self.covid19_inperson_page.click_covid19_flu_button()
        logger.info(f"Checking the covid19 flu text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.COVID19_FLU_OVERVIEW_TEXT_IS)}")
        assert "COVID-19 & flu overview" in self.covid19_inperson_page.get_text(self.covid19_inperson_page.COVID19_FLU_OVERVIEW_TEXT_IS), "COVID-19 & flu overview text is not displayed"
        logger.info("Click the covid19 flu overview button")
        self.covid19_inperson_page.click_covid19_flu_overview_button()
        assert f"{self.base_url}/respiratory/" in self.covid19_inperson_page.get_url()
        self.covid19_inperson_page.wait_for_timeout(2)
        logger.info("Scroll to the make an appointment")
        self.covid19_inperson_page.scroll_to_element(self.covid19_inperson_page.MAKE_AN_APPOINTMENT)
        logger.info("Verify make an appointment is displayed")
        self.covid19_inperson_page.is_visible(self.covid19_inperson_page.MAKE_AN_APPOINTMENT), "Make an appointment is not displayed"
        logger.info("Click make an appointment arrow button")
        self.covid19_inperson_page.click_make_an_appointment_arrow_button()
        self.covid19_inperson_page.wait_for_timeout(2)
        assert f"{self.base_url}/respiratory/in-person-appointment" in self.covid19_inperson_page.get_url()
        assert "Book an In-Person Respiratory Appointment | PfizerForAll™" in self.covid19_inperson_page.get_title()
        logger.info(f"Checking the title text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.TITLE_TEXT_IS)}")
        assert "See a doctor in person near you." in self.covid19_inperson_page.get_text(self.covid19_inperson_page.TITLE_TEXT_IS), "See a doctor in person near you. is not displayed"
        logger.info(f"Checking the Subtext text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.SUBTEXT_TEXT_IS)}")
        assert "We’ve made it simple to find one. Make an appointment to talk to a doctor near you, on your schedule." in self.covid19_inperson_page.get_text(self.covid19_inperson_page.SUBTEXT_TEXT_IS), "We’ve made it simple to find one. Make an appointment to talk to a doctor near you, on your schedule. os not displayed"
        logger.info(f"Checking the Book appointment button text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.BOOK_APPOINTMENT_BUTTON)}")
        assert "Book an appointment on Zocdoc" in self.covid19_inperson_page.get_text(
            self.covid19_inperson_page.BOOK_APPOINTMENT_BUTTON), "Book an appointment on Zocdoc is not displayed"

        # Scenario:1 Verify the Zocdoc Pop-up on "Covid-19 In-person Appointment" page

    def test_verify_the_zocdoc_popup_covid19_inperson_appointment(self):
        logger.info("Test verify the zocdoc popup covid19 inperson appointment")
        logger.info("Click book appointment button")
        self.covid19_inperson_page.click_book_appointment_button()
        self.covid19_inperson_page.wait_for_timeout(2)
        logger.info(f"Checking the Zocdoc title text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.ZOCDOC_TITLE_TEXT_IS)}")
        assert "You are leaving PfizerForAll™ to go to Zocdoc.com" in self.covid19_inperson_page.get_text(self.covid19_inperson_page.ZOCDOC_TITLE_TEXT_IS), "You are leaving PfizerForAll™ to go to Zocdoc.com is not displayed"
        logger.info(f"Checking the Continue zocdoc button text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.CONTINUE_TO_ZOCDOC_BUTTON_TEXT)}")
        assert "Continue to Zocdoc" in self.covid19_inperson_page.get_text(self.covid19_inperson_page.CONTINUE_TO_ZOCDOC_BUTTON_TEXT), "Continue to Zocdoc is not displayed"
        logger.info(f"Checking the Book appointment button text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.BOOK_APPOINTMENT_BUTTON)}")
        assert "By clicking the link above, you will be redirected to a third-party website that is neither owned nor controlled by Pfizer. Pfizer is not responsible for the content or services of this third-party website." in self.covid19_inperson_page.get_text(self.covid19_inperson_page.DISCLAIMER_TEXT_IS), "Disclaimer text is not displayed"

        # Scenario:2 Verify "Booking is quick and simple" section

    def test_verify_booking_is_quick_and_simple_section(self):
        logger.info("Test Verify booking is quick and simple section")
        logger.info("Scroll to the Booking heading")
        self.covid19_inperson_page.scroll_to_element(self.covid19_inperson_page.BOOKING_HEADING)
        logger.info("Verify the booking heading is displayed")
        self.covid19_inperson_page.is_visible(self.covid19_inperson_page.BOOKING_HEADING), "Booking heading is not displayed"
        logger.info(f"Checking the Heading text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.HEADING_TEXT_IS)}")
        assert "Booking is quick and simple." in self.covid19_inperson_page.get_text(self.covid19_inperson_page.HEADING_TEXT_IS), "Booking is quick and simple. is not displayed"
        logger.info(f"Checking the Booking subtext is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.BOOKING_SUBTEXT_IS)}")
        assert "Provided by Zocdoc" in self.covid19_inperson_page.get_text(self.covid19_inperson_page.BOOKING_SUBTEXT_IS), "Provided by Zocdoc is not displayed"
        logger.info(f"Checking the Step 1 tag text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.STEP_1_TAG_TEXT)}")
        assert "Step 1" in self.covid19_inperson_page.get_text(self.covid19_inperson_page.STEP_1_TAG_TEXT)
        logger.info(f"Checking the Step 1 Heading text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.STEP_1_HEADING_TEXT)}")
        assert "Search for a doctor near you" in self.covid19_inperson_page.get_text(self.covid19_inperson_page.STEP_1_HEADING_TEXT)
        logger.info(f"Checking the Step 1 text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.STEP_1_TEXT_IS)}")
        assert "Select a provider type and enter your ZIP code." in self.covid19_inperson_page.get_text(self.covid19_inperson_page.STEP_1_TEXT_IS)
        logger.info(f"Checking the Step 2 tag text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.STEP_2_TAG_TEXT)}")
        assert "Step 2" in self.covid19_inperson_page.get_text(self.covid19_inperson_page.STEP_2_TAG_TEXT), "Step 2 is not displayed"
        logger.info(f"Checking the Step 2 heading text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.STEP_2_HEADING_TEXT)}")
        assert "Choose who you want to see" in self.covid19_inperson_page.get_text(self.covid19_inperson_page.STEP_2_HEADING_TEXT), "Choose who you want to see is not displayed"
        logger.info(f"Checking the Step 2 text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.STEP_2_TEXT_IS)}")
        assert "Read patient reviews and provider profiles. See availability, insurance coverage, and more." in self.covid19_inperson_page.get_text(self.covid19_inperson_page.STEP_2_TEXT_IS), "Read patient reviews and provider profiles See availability, insurance coverage, and more are not displayed"
        logger.info(f"Checking the Step 3 tag text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.STEP_3_TAG_TEXT)}")
        assert "Step 3" in self.covid19_inperson_page.get_text(self.covid19_inperson_page.STEP_3_TAG_TEXT), "Step 3 is not displayed"
        logger.info(f"Checking the Step 3 heading text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.STEP_3_HEADING_TEXT)}")
        assert "Schedule an appointment that works best for you" in self.covid19_inperson_page.get_text(self.covid19_inperson_page.STEP_3_HEADING_TEXT), "Schedule an appointment that works best for you is not displayed"
        logger.info(f"Checking the Confirmed tag text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.CONFIRMED_TAG_TEXT)}")
        assert "Confirmed" in self.covid19_inperson_page.get_text(self.covid19_inperson_page.CONFIRMED_TAG_TEXT), "Confirmed is not displayed"
        logger.info(f"Verifying  the Confirmed heading text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.CONFIRMED_HEADING_TEXT_IS)}")
        assert "Get confirmation" in self.covid19_inperson_page.get_text(self.covid19_inperson_page.CONFIRMED_HEADING_TEXT_IS), "Get confirmation is not displayed"
        logger.info(f"Verifying the Confirmed text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.CONFIRMED_TEXT_IS)}")
        assert "Receive an email with appointment details, and you’re ready to go!" in self.covid19_inperson_page.get_text(self.covid19_inperson_page.CONFIRMED_TEXT_IS), "Receive an email with appointment details, and you’re ready to go! is not displayed"

    def test_verify_save_on_your_prescribed_pfizer_medications(self):
        logger.info("Test Verify Save_on_your_prescribed_Pfizer_medications")
        logger.info("Scroll to the save prescribed medication section")
        self.covid19_inperson_page.scroll_to_element(self.covid19_inperson_page.SAVE_PRESCRIBED_MEDICATIONS_SECTION)
        logger.info("Verify the save prescribed medications section is displayed")
        assert self.covid19_inperson_page.is_visible(self.covid19_inperson_page.SAVE_PRESCRIBED_MEDICATIONS_SECTION), "Save prescribed medications section is not displayed"
        logger.info(f"Verifying the save prescribed medications title text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.SAVE_PRESCRIBED_MEDICATIONS_TITLE_TEXT_IS)}")
        assert "Save on your prescribed Pfizer medications, and get support when you need it." in self.covid19_inperson_page.get_text(self.covid19_inperson_page.SAVE_PRESCRIBED_MEDICATIONS_TITLE_TEXT_IS), "Save on your prescribed Pfizer medications, and get support when you need it is not displayed"
        logger.info(f"Verifying the save prescribed medications subtext is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.SAVE_PRESCRIBED_MEDICATIONS_SUBTEXT_IS)}")
        assert "From co-pay savings cards to financial assistance programs, we have options that can help. Our dedicated customer support team can also help you navigate your insurance benefits, understand your options, and more." in self.covid19_inperson_page.get_text(self.covid19_inperson_page.SAVE_PRESCRIBED_MEDICATIONS_SUBTEXT_IS), "Save prescribed medications section is not displayed"
        logger.info(f"Verifying the get started button text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.GET_STARTED_BUTTON_TEXT_IS)}")
        assert "Get started" in self.covid19_inperson_page.get_text(self.covid19_inperson_page.GET_STARTED_BUTTON_TEXT_IS), "Get started is not displayed"
        logger.info("Click the get started button")
        self.covid19_inperson_page.click_get_started_button()
        self.covid19_inperson_page.wait_for_timeout(2)
        assert f"{self.base_url}/prescription-assistance" in self.covid19_inperson_page.get_url()

        # Scenario:4 Verify disclaimer text on "Covid-19 In-person Appointment" page

    def test_verify_disclaimer_text_on_covid19_inperson_appointment(self):
        logger.info("Test verify_disclaimer_text_on_Covid19_Inperson_Appointment")
        logger.info("Click the bottom of the page")
        self.covid19_inperson_page.scroll_to_element(self.covid19_inperson_page.BOTTOM_OF_THE_PAGE)
        self.covid19_inperson_page.wait_for_timeout(2)
        logger.info(f"Verifying the Bottom of disclaimer text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.BOTTOM_OF_DISCLAIMER_TEXT_IS)}")
        assert "FOR U.S. RESIDENTS ONLY. The information provided is for educational purposes only and is not intended to replace discussions with a healthcare professional.© 2025 Pfizer Inc. All rights reserved. PP-UNP-USA-6048" in self.covid19_inperson_page.get_text(self.covid19_inperson_page.BOTTOM_OF_DISCLAIMER_TEXT_IS), "Bottom-of-the-page is not displayed"

        #  Scenario: 5 Verify "FAQ" section

    def test_verify_faq_section(self):
        logger.info("Test verify faq_section")
        logger.info("Scroll to the fag Section")
        self.covid19_inperson_page.scroll_to_element(self.covid19_inperson_page.FAG_SECTION)
        logger.info("Verify the fag 1 icon is displayed")
        self.covid19_inperson_page.is_visible(self.covid19_inperson_page.FAG_1_ICON), "Fag 1 icon is not displayed"
        logger.info("Click the fag 1 icon")
        self.covid19_inperson_page.click_fag_1_icon()
        logger.info("Verify the fag 1 details is displayed")
        self.covid19_inperson_page.is_visible(self.covid19_inperson_page.FAG_1_DETAILS), "Fag 1 details is not displayed"
        logger.info(f"Verifying the fag 1 details text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.FAG_1_DETAILS_TEXT_IS)}")
        assert "It all depends. Zocdoc allows you to search for different healthcare providers based on their availability. You can search for the soonest available appointment, and find a time and provider that works best for you." in self.covid19_inperson_page.get_text(self.covid19_inperson_page.FAG_1_DETAILS_TEXT_IS), "It all depends. Zocdoc allows you to search for different healthcare providers based on their availability. You can search for the soonest available appointment, and find a time and provider that works best for you."
        logger.info("Click the fag 1 icon")
        self.covid19_inperson_page.click_fag_1_icon()
        logger.info("Verify fag 2 icon is displayed")
        self.covid19_inperson_page.is_visible(self.covid19_inperson_page.FAG_2_ICON), "Fag 2 icon is not displayed"
        logger.info("Click the fag 2 icon")
        self.covid19_inperson_page.click_fag_2_icon()
        logger.info("Verify the fag 2 details is displayed")
        self.covid19_inperson_page.is_visible(self.covid19_inperson_page.FAG_2_DETAILS), "Fag 2 details is not displayed"
        logger.info(f"Verifying the Fag 2 details text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.FAG_2_DETAILS_TEXT_IS)}")
        assert "There is no cost for booking an in-person visit on Zocdoc, but you will be responsible for the cost of the doctor visit itself. If you have health insurance, you can search for providers who accept your plan." in self.covid19_inperson_page.get_text(self.covid19_inperson_page.FAG_2_DETAILS_TEXT_IS), "Fag 2 details text is not displayed"
        logger.info("Click the fag 2 icon")
        self.covid19_inperson_page.click_fag_2_icon()
        logger.info("Verify fag 3 icon is displayed")
        self.covid19_inperson_page.is_visible(self.covid19_inperson_page.FAG_3_ICON), "Fag 3 icon is not displayed"
        logger.info("Click the fag 3 icon")
        self.covid19_inperson_page.click_fag_3_icon()
        logger.info("Verify the fag 3 details is displayed")
        self.covid19_inperson_page.is_visible(self.covid19_inperson_page.FAG_3_DETAILS), "Fag 3 details is not displayed"
        logger.info(f"Verifying the Fag 3 details text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.FAG_3_DETAILS_TEXT_IS)}")
        assert "Yes. You can book an appointment for someone else on Zocdoc. Log in to Zocdoc with your own account, select a provider and appointment time, and then under “Patient” select “Someone else” and enter their information." in self.covid19_inperson_page.get_text(self.covid19_inperson_page.FAG_3_DETAILS_TEXT_IS), "Fag 3 details text is not displayed"
        logger.info("Click the fag 3 icon")
        self.covid19_inperson_page.click_fag_3_icon()
        logger.info("Verify the fag 4 icon is displayed")
        self.covid19_inperson_page.is_visible(self.covid19_inperson_page.FAG_4_ICON), "Fag 4 icon is not displayed"
        logger.info("Click the fag 4 icon")
        self.covid19_inperson_page.click_fag_4_icon()
        logger.info("Verify the fag 4 details is displayed")
        self.covid19_inperson_page.is_visible(self.covid19_inperson_page.FAG_4_DETAILS), "Fag 4 details is not displayed"
        logger.info(f"Verifying the Fag 4 details text is: {self.covid19_inperson_page.get_text(self.covid19_inperson_page.FAG_4_DETAILS_TEXT_IS)}")
        assert "After discussing your symptoms and doing any tests, your Zocdoc provider will give you any needed prescriptions, which you can fill on your own." in self.covid19_inperson_page.get_text(self.covid19_inperson_page.FAG_4_DETAILS_TEXT_IS), "Fag 4 details text is not displayed"
        logger.info("Click the fag 4 icon")
        self.covid19_inperson_page.click_fag_4_icon()
