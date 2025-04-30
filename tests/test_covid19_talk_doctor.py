import pytest
from pages.covid19_talk_doctor_page import Covid19TalkDoctorPage
from pages.home_page import HomePage
from tests.conftest import driver
import logging

logger = logging.getLogger(__name__)


class TestCovid19TalkDoctorPage:

    @pytest.fixture(autouse=True)
    def setup(self, driver, BASE_URL):
        self.base_url = BASE_URL
        self.covid19_doctor_page = Covid19TalkDoctorPage(driver)
        self.home_page = HomePage(driver)

        logger.info("Common steps for Covid19TalkDoctorPage")
        self.home_page.go_to_homepage(self.base_url)
        assert "Pfizer" in driver.title()
        logger.info("Verify the accept all displayed")
        assert self.covid19_doctor_page.is_visible(self.covid19_doctor_page.ACCEPT_ALL, timeout=30)
        logger.info("Click the accept cookies")
        self.home_page.click_accept_cookies()
        logger.info("Scroll to the menu button")
        self.covid19_doctor_page.scroll_to_element(self.covid19_doctor_page.MENU_BUTTON)
        logger.info("Click the Menu button")
        self.covid19_doctor_page.click_menu_button()
        logger.info(f"Checking the covid19 flu text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.COVID19_FLU_TEXT_IS)}")
        assert self.covid19_doctor_page.is_visible(self.covid19_doctor_page.COVID19_FLU_TEXT_IS)
        logger.info("Click the covid19 flu button")
        self.covid19_doctor_page.click_covid19_flu_button()
        logger.info("Verify Talk to a doctor now text is displayed")
        assert self.covid19_doctor_page.is_visible(self.covid19_doctor_page.TALK_TO_DOCTOR_NOW_TEXT_IS)
        logger.info("Click the talk to a doctor button")
        self.covid19_doctor_page.click_talk_to_a_doctor_button()
        assert f"{self.base_url}/respiratory/telehealth" in self.covid19_doctor_page.get_url()
        assert 'Book a Telehealth Respiratory Appointment | PfizerForAll™' in self.covid19_doctor_page.get_title(), "Book a Telehealth Respiratory Appointment | PfizerForAll™ is not displayed"

         # Scenario:-1 Verify the hero banner

    def test_verify_the_hero_banner(self):
        logger.info("Test verify the hero banner")
        logger.info("Scroll to the title")
        self.covid19_doctor_page.scroll_to_element(self.covid19_doctor_page.TITLE)
        logger.info(f"Title text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.TITLE_TEXT_IS)}")
        assert "See a doctor right away with telehealth." in self.covid19_doctor_page.get_text(self.covid19_doctor_page.TITLE_TEXT_IS), "See a doctor right away with telehealth."
        logger.info(f" Verifying the Title text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.SUBTEXT_TEXT_IS)}")
        assert "If you’re feeling sick, you can connect to care right from home. We partner with UpScript, an independent telehealth provider. They can find you a doctor who will listen, evaluate your symptoms, and help make a plan. Treatments for COVID-19 and flu must be taken within the first few days of symptoms." in self.covid19_doctor_page.get_text(self.covid19_doctor_page.SUBTEXT_TEXT_IS), "Subtext is not displayed"
        logger.info(f"Verifying the Schedule upscript button text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.SCHEDULE_UPSCRIPT_BUTTON_TEXT_IS)}")
        assert "Schedule with UpScriptCare for $35" in self.covid19_doctor_page.get_text(self.covid19_doctor_page.SCHEDULE_UPSCRIPT_BUTTON_TEXT_IS), "Schedule with UpScriptCare for $35 is not displayed"

        # Scenario:-2 Verify the upscript site leaving popup

    def test_verify_the_upscript_site_leaving_popup(self):
        logger.info("Test verify the upscript site leaving popup")
        logger.info("Click the Schedule upscript button")
        self.covid19_doctor_page.click_schedule_upscript_button()
        logger.info("Verify the pop up is displayed")
        assert self.covid19_doctor_page.is_visible(self.covid19_doctor_page.POP_UP), "Popup is not displayed"
        logger.info(f"Verifying the Eyebrow text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.EYEBROW_TEXT_IS)}")
        assert "You’re a click away from finding a doctor through UpScriptCare" in self.covid19_doctor_page.get_text(self.covid19_doctor_page.EYEBROW_TEXT_IS), "you are a click away from finding a doctor through UpScriptCare is not displayed"
        logger.info(f"Verifying the Continue button text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.CONTINUE_BUTTON_TEXT_IS)}")
        assert "See a doctor at UpScriptCare" in self.covid19_doctor_page.get_text(self.covid19_doctor_page.CONTINUE_BUTTON_TEXT_IS), "see a doctor at UpScriptCare is not displayed"
        logger.info(f"Verifying the Disclaimer text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.DISCLAIMER_TEXT_IS)}")
        assert "See full terms and conditions at UpScriptCare.com. By clicking the link above, you will be redirected to a third-party website that is neither owned nor controlled by Pfizer. Pfizer is not responsible for the content or services of this third-party website." in self.covid19_doctor_page.get_text(self.covid19_doctor_page.DISCLAIMER_TEXT_IS)
        logger.info("Verify Cancel button is displayed")
        assert self.covid19_doctor_page.is_visible(self.covid19_doctor_page.CANCEL_BUTTON), "Cancel button is not displayed"
        logger.info("Click the cancel button")
        self.covid19_doctor_page.click_cancel_button()
        self.covid19_doctor_page.wait_for_timeout(2)
        logger.info("Click the pop up button")
        assert not self.covid19_doctor_page.is_visible(self.covid19_doctor_page.POP_UP), "Popup is not displayed"

        # Scenario:-3 Verify the Telehealth appointments+C6

    def test_verify_the_telehealth_appointments(self):
        logger.info("Test verify the telehealth appointments")
        logger.info("Clik the schedule upscript button")
        self.covid19_doctor_page.click_schedule_upscript_button()
        logger.info("Clik to the Continue upscript button")
        self.covid19_doctor_page.click_continue_upscript_button()
        self.covid19_doctor_page.wait_for_timeout(5)
        assert f"https://upscriptcare.com/" in self.covid19_doctor_page.get_url_from_new_tab(context=self.covid19_doctor_page)
        logger.info("Close the current tab")
        self.covid19_doctor_page.close_current_tab(self.covid19_doctor_page)
        self.home_page.wait_for_timeout(1)
        self.covid19_doctor_page.is_window_focused()
        logger.info("Verify the Pop up title is displayed")
        assert self.covid19_doctor_page.is_visible(self.covid19_doctor_page.POP_UP_TITLE), "Popup title is not displayed"
        logger.info(f"Verifying the Popup title text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.POP_UP_TITLE_TEXT_IS)}")
        assert "Additional support you can find on PfizerForAll™" in self.covid19_doctor_page.get_text(self.covid19_doctor_page.POP_UP_TITLE_TEXT_IS), "Popup title text is not displayed"
        #  And I expect that element 'telehealth > hero_banner > pop_up_cards' appears exactly '3' times

    def test_verify_talk_to_a_doctor_right_away_section(self):
        logger.info("Test verify the talk to a doctor right away section")
        logger.info("Scroll to the talk to a doctor")
        self.covid19_doctor_page.scroll_to_element(self.covid19_doctor_page.TALK_TO_A_DOCTOR)
        logger.info("Verify the talk to a doctor is displayed")
        self.covid19_doctor_page.is_visible(self.covid19_doctor_page.TALK_TO_A_DOCTOR), "Talk to a doctor is not displayed"
        logger.info(f"Verifying the Talk to a doctor text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.TALK_TO_A_DOCTOR_TEXT)}")
        assert "See a doctor right away with telehealth." in self.covid19_doctor_page.get_text(self.covid19_doctor_page.TALK_TO_A_DOCTOR_TEXT), "see a doctor right away with telehealth."
        logger.info("Verify the talk to a doctor description is displayed")
        self.covid19_doctor_page.is_visible(self.covid19_doctor_page.TALK_TO_A_DOCTOR_DESCRIPTION), "Talk to a doctor description is not displayed"
        logger.info(f"Verifying the Talk to a doctor description text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.TALK_TO_A_DOCTOR_DESCRIPTION_TEXT)}")
        assert "If you’re feeling sick, you can connect to care right from home. We partner with UpScript, an independent telehealth provider. They can find you a doctor who will listen, evaluate your symptoms, and help make a plan. Treatments for COVID-19 and flu must be taken within the first few days of symptoms." in self.covid19_doctor_page.get_text(self.covid19_doctor_page.TALK_TO_A_DOCTOR_DESCRIPTION_TEXT)

    def test_verify_convenience_section(self):
        logger.info("Test verify the convenience section")
        self.covid19_doctor_page.scroll_to_element(self.covid19_doctor_page.HEADING)
        logger.info("Verify the heading is displayed")
        self.covid19_doctor_page.is_visible(self.covid19_doctor_page.HEADING), "Heading is not displayed"
        logger.info(f"Verifying the Heading text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.HEADING_TEXT_IS)}")
        assert "Convenience, convenience, convenience." in self.covid19_doctor_page.get_text(self.covid19_doctor_page.HEADING_TEXT_IS), "Heading text is not displayed"
        logger.info(f"Verifying the Text text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.TEXT_TEXT_IS)}")
        assert "Get answers fast when you’re not feeling well." in self.covid19_doctor_page.get_text(self.covid19_doctor_page.TEXT_TEXT_IS), "Get answers fast when you are not feeling well. is not displayed"
        logger.info(f"Verifying the Bullet 1 text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.BULLET_1_TEXT_IS)}")
        assert "All visits are virtual." in self.covid19_doctor_page.get_text(self.covid19_doctor_page.BULLET_1_TEXT_IS), "Bullet 1 text is not displayed"
        logger.info(f"Verifying the Bullet 2text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.BULLET_2_TEXT_IS)}")
        assert "UpScriptCare providers are available 6AM – 12AM EST. Every day." in self.covid19_doctor_page.get_text(self.covid19_doctor_page.BULLET_2_TEXT_IS), "Bullet 2 text is not displayed"
        logger.info(f"Verifying theBullet 3 text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.BULLET_3_TEXT_IS)}")
        assert "Medications can be delivered right to your door or you can pick them up at your pharmacy." in self.covid19_doctor_page.get_text(self.covid19_doctor_page.BULLET_3_TEXT_IS), "Bullet 3 text is not displayed"
        logger.info(f"Verifying the Bullet 4 text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.BULLET_4_TEXT_IS)}")
        assert "You can use your HSA or FSA accounts to help cover the cost of your visit." in self.covid19_doctor_page.get_text(self.covid19_doctor_page.BULLET_4_TEXT_IS), "Bullet 4 text is not displayed"

        # Scenario:6 Verify "UpScriptCare is quick and simple" section

    def test_verify_upscriptcare_is_quick_and_simple_section(self):
        logger.info("Test verify the upscriptcare is quick and simple section")
        logger.info("Scroll to the upscript heading")
        self.covid19_doctor_page.scroll_to_element(self.covid19_doctor_page.UPSCRIPT_HEADING)
        logger.info("Verify the upcript heading is displayed")
        self.covid19_doctor_page.is_visible(self.covid19_doctor_page.UPSCRIPT_HEADING), "Upscript Heading is not displayed"
        logger.info(f"Verifying the Step 1 tag text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.STEP_1_TAG_TEXT_IS)}")
        assert "Step 1" in self.covid19_doctor_page.get_text(self.covid19_doctor_page.STEP_1_TAG_TEXT_IS), "Step 1 is not displayed"
        logger.info(f"Verifying the Step 1 heading text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.STEP_1_HEADING_TEXT_IS)}")
        assert "Get registered" in self.covid19_doctor_page.get_text(self.covid19_doctor_page.STEP_1_HEADING_TEXT_IS), "Get registered is not displayed"
        logger.info(f"Verifying the Step 1 text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.STEP_1_TEXT_IS)}")
        assert "Create an UpScriptCare account." in self.covid19_doctor_page.get_text(self.covid19_doctor_page.STEP_1_TEXT_IS), "Create an UpScriptCare account."
        logger.info(f"Verifying the Step 2 tag text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.STEP_2_TAG_TEXT_IS)}")
        assert "Step 2" in self.covid19_doctor_page.get_text(self.covid19_doctor_page.STEP_2_TAG_TEXT_IS), "Step 2 is not displayed"
        logger.info(f"Verifying the Step 2 heading text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.STEP_2_HEADING_TEXT_IS)}")
        assert "Answer a 5-minute questionnaire" in self.covid19_doctor_page.get_text(self.covid19_doctor_page.STEP_2_HEADING_TEXT_IS), "Answer a 5-minute questionnaire is not displayed"
        logger.info(f"Verifying the Step 2 text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.STEP_2_TEXT_IS)}")
        assert "There are a few medical questions that will help move things along." in self.covid19_doctor_page.get_text(self.covid19_doctor_page.STEP_2_TEXT_IS), "Step 2 text is not displayed"
        logger.info(f"Verifying the Step 3 tag text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.STEP_3_TAG_TEXT_IS)}")
        assert "Step 3" in self.covid19_doctor_page.get_text(self.covid19_doctor_page.STEP_3_TAG_TEXT_IS), "Step 3 is not displayed"
        logger.info(f"Verifying the Step 3 heading text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.STEP_3_HEADING_TEXT_IS)}")
        assert "Checkout" in self.covid19_doctor_page.get_text(self.covid19_doctor_page.STEP_3_HEADING_TEXT_IS), "Checkout is not displayed"
        logger.info(f"Verifying the Step 3 text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.STEP_3_TEXT_IS)}")
        assert "Provide address and payment details." in self.covid19_doctor_page.get_text(self.covid19_doctor_page.STEP_3_TEXT_IS), "Provide address and payment details. is not displayed"
        logger.info(f"Verifying the Step 4 tag text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.STEP_4_TAG_TEXT_IS)}")
        assert "Step 4" in self.covid19_doctor_page.get_text(self.covid19_doctor_page.STEP_4_TAG_TEXT_IS), "Step 4 is not displayed"
        logger.info(f"Verifying the Step 4 heading text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.STEP_4_HEADING_TEXT_IS)}")
        assert "Talk with a doctor" in self.covid19_doctor_page.get_text(self.covid19_doctor_page.STEP_4_HEADING_TEXT_IS), "Talk with a doctor is not displayed"
        logger.info(f"Verifying the Step 4 text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.STEP_4_TEXT_IS)}")
        assert "Get your questions answered, and discuss treatment options that may be right for you. (Consultation type is dependent on your state regulations.)" in self.covid19_doctor_page.get_text(self.covid19_doctor_page.STEP_4_TEXT_IS), "Get your questions answered, and discuss treatment options that may be right for you. (Consultation type is dependent on your state regulations.) is not displayed"

        # Scenario: 7 Verify "Save on your prescribed Pfizer medications, and get support when you need it." section

    def test_verify_save_on_your_prescribed_pfizer_medications(self):
        logger.info("Test verify the save on your prescribed pfizer medications")
        logger.info("Scroll to the save prescribed medications section")
        self.covid19_doctor_page.scroll_to_element(self.covid19_doctor_page.SAVE_PRESCRIBED_MEDICATIONS_SECTION)
        logger.info("Verify the save prescribed medications section is displayed")
        self.covid19_doctor_page.is_visible(self.covid19_doctor_page.SAVE_PRESCRIBED_MEDICATIONS_SECTION), "Save Prescribed medicattions section is not displayed"
        logger.info(f"Verifying the Save prescribed medications section title text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.SAVE_PRESCRIBED_MEDICATIONS_SECTION_TITLE_TEXT_IS)}")
        assert "Save on your prescribed Pfizer medications, and get support when you need it." in self.covid19_doctor_page.get_text(self.covid19_doctor_page.SAVE_PRESCRIBED_MEDICATIONS_SECTION_TITLE_TEXT_IS), "Save on your prescribed Pfizer medications, and get support when you need it.is not displayed"
        logger.info(f"Verifying the Save prescribed medications section title text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.SAVE_PRESCRIBED_MEDICATIONS_SECTION_SUBTEXT_IS)}")
        assert "From co-pay savings cards to financial assistance programs, we have options that can help. Our dedicated customer support team can also help you navigate your insurance benefits, understand your options, and more." in self.covid19_doctor_page.get_text(self.covid19_doctor_page.SAVE_PRESCRIBED_MEDICATIONS_SECTION_SUBTEXT_IS)
        logger.info(f"Verifying the Get started button text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.GET_STARTED_BUTTON_TEXT_IS)}")
        assert "Get started" in self.covid19_doctor_page.get_text(self.covid19_doctor_page.GET_STARTED_BUTTON_TEXT_IS), "Get started is not displayed"
        logger.info("Click the get started button")
        self.covid19_doctor_page.click_get_started_button()
        assert f"{self.base_url}/prescription-assistance" in self.covid19_doctor_page.get_url()

        # Scenario: Verify disclaimer text on Covid19 talk to doctor page

    def test_verify_disclaimer_text_on_covid19_talk_to_doctor_page(self):
        logger.info("Test verify disclaimer text on covid19 talk to doctor page")
        logger.info("Scroll to the Bottom of disclaimer")
        self.covid19_doctor_page.scroll_to_element(self.covid19_doctor_page.BOTTOM_OF_DISCLAIMER)
        logger.info(f"Verifying the Bottom of disclaimer text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.BOTTOM_OF_DISCLAIMER_TEXT_IS)}")
        assert "FOR U.S. RESIDENTS ONLY. The information provided is for educational purposes only and is not intended to replace discussions with a healthcare professional.© 2025 Pfizer Inc. All rights reserved. PP-UNP-USA-6048" in self.covid19_doctor_page.get_text(self.covid19_doctor_page.BOTTOM_OF_DISCLAIMER_TEXT_IS)

        # Scenario: Verify FAQ section

    def test_verify_faq_section(self):
        logger.info("Test verify the fag section")
        logger.info("Scroll to the fag section")
        self.covid19_doctor_page.scroll_to_element(self.covid19_doctor_page.FAG_SECTION)
        logger.info("Verify the fag 1 icon is displayed")
        self.covid19_doctor_page.is_visible(self.covid19_doctor_page.FAG_1_ICON), "Fag 1 icon is not displayed"
        logger.info("Click the fag 1 icon")
        self.covid19_doctor_page.click_fag_1_icon()
        logger.info("Verify the fag 1 details is displayed")
        self.covid19_doctor_page.is_visible(self.covid19_doctor_page.FAG_1_DETAILS), "Fag 1 details is not displayed"
        logger.info(f"Verifying the Fag 1 details text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.FAG_1_DETAILS_TEXT_IS)}")
        assert "In most cases, you’ll be able to schedule an appointment and be seen virtually by a healthcare provider within 30 minutes." in self.covid19_doctor_page.get_text(self.covid19_doctor_page.FAG_1_DETAILS_TEXT_IS), "In most cases, you’ll be able to schedule an appointment and be seen virtually by a healthcare provider within 30 minutes. is not displayed"
        logger.info("Click the fag 1 icon")
        self.covid19_doctor_page.click_fag_1_icon()
        logger.info("Verify the fag 2 icon is displayed")
        self.covid19_doctor_page.is_visible(self.covid19_doctor_page.FAG_2_ICON), "Fag 2 icon is not displayed"
        logger.info("Click to the fag 2 icon")
        self.covid19_doctor_page.click_fag_2_icon()
        logger.info("Verify the fag 2 details is displayed")
        self.covid19_doctor_page.is_visible(self.covid19_doctor_page.FAG_2_DETAILS), "Fag 2 details is not displayed"
        logger.info(f"Verifying the Fag 2 details text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.FAG_2_DETAILS_TEXT_IS)}")
        assert "A telehealth visit with a medical expert on UpScriptCare costs $35." in self.covid19_doctor_page.get_text(self.covid19_doctor_page.FAG_2_DETAILS_TEXT_IS), "A telehealth visit with a medical expert on UpScriptCare costs $35. is displayed"
        logger.info("Click the fag 2 icon")
        self.covid19_doctor_page.click_fag_2_icon()
        logger.info("Verify the fag 3 icon is displayed")
        self.covid19_doctor_page.is_visible(self.covid19_doctor_page.FAG_3_ICON), "Fag 3 icon is not displayed"
        logger.info("Click the fag 3 icon")
        self.covid19_doctor_page.click_fag_3_icon()
        logger.info("Click fag 3 details is displayed")
        self.covid19_doctor_page.is_visible(self.covid19_doctor_page.FAG_3_DETAILS), "Fag 3 details is not displayed"
        logger.info(f"Verifying the Fag 3 details text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.FAG_3_DETAILS_TEXT_IS)}")
        assert "Yes, you can help someone book their UpScriptCare appointment, but that person will still need to be present during the virtual visit." in self.covid19_doctor_page.get_text(self.covid19_doctor_page.FAG_3_DETAILS_TEXT_IS), "Yes, you can help someone book their UpScriptCare appointment, but that person will still need to be present during the virtual visit. is not displayed"
        logger.info("CLick the fag 3 icon")
        self.covid19_doctor_page.click_fag_3_icon()
        logger.info("Verify the fag 4 icon is displayed")
        self.covid19_doctor_page.is_visible(self.covid19_doctor_page.FAG_4_ICON), "Fag 4 icon is not displayed"
        logger.info("Click the fag 4 icon")
        self.covid19_doctor_page.click_fag_4_icon()
        logger.info("Verify the fag 4 details is displayed")
        self.covid19_doctor_page.is_visible(self.covid19_doctor_page.FAG_4_DETAILS), "Fag 4 details is not displayed"
        logger.info(f"Verifying the Fag 4 details text is: {self.covid19_doctor_page.get_text(self.covid19_doctor_page.FAG_4_DETAILS_TEXT_IS)}")
        assert "Not necessarily. You’ll just need to complete a medical questionnaire and have your computer or phone ready for the virtual appointment. You also may want to have your FSA or HSA info ready (if you have either type of account) as you can use those funds towards payment." in self.covid19_doctor_page.get_text(self.covid19_doctor_page.FAG_4_DETAILS_TEXT_IS), "Fag 4 details is not displayed"
