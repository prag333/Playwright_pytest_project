import pytest
from pages.covid19_overview_page import Covid19OverviewPage
from pages.home_page import HomePage
from tests.conftest import driver

class TestCovidPage:

    @pytest.fixture(autouse=True)
    def setup(self, driver, BASE_URL):
        self.base_url = BASE_URL
        self.covid19_page = Covid19OverviewPage(driver)
        self.home_page = HomePage(driver)

        self.home_page.go_to_homepage(self.base_url)
        assert "Pfizer" in driver.title()
        assert self.covid19_page.is_visible(self.covid19_page.ACCEPT_ALL, timeout=30)
        self.home_page.click_accept_cookies()
        self.covid19_page.click_menu()
        assert self.covid19_page.is_visible(self.covid19_page.COVID19_FLU)
        self.covid19_page.click_covid19_flu()
        assert self.covid19_page.is_visible(self.covid19_page.COVID19_FLU_OVERVIEW, timeout=5)
        self.covid19_page.click_covid19_flu_overview()
        assert self.covid19_page.is_visible(self.covid19_page.TITLE_PFIZER_FOR_ALL, timeout=5)

    def __test_telehealth_page(self):
        assert self.covid19_page.is_visible(self.covid19_page.HERO_TEXT)
        assert "COVID-19" in self.covid19_page.get_text(self.covid19_page.HERO_TEXT_CONTAINS_COVID19), "Covid-19 is not displayed"
        assert "Book a $35 virtual visit now" == self.covid19_page.get_text(self.covid19_page.BOOK_A_35_VIRTUAL_VISIT_NOW), \
                                                 "Book a $35 virtual visit now is not displayed"
        assert "Learn about your telehealth options" == self.covid19_page.get_text(self.covid19_page.LEARN_ABOUT_YOUR_TELEHEALTH_OPTIONS), \
            "Learn about your telehealth options is not displayed"
        self.covid19_page.scroll_to_element(self.covid19_page.DISCLAIMER_TEXT_IS)
        assert ("FOR U.S. RESIDENTS ONLY. The information provided is for educational purposes only and is not intended "
                "to replace discussions with a healthcare professional.© 2025 Pfizer Inc. All rights reserved. "
                "PP-UNP-USA-6048") in self.covid19_page.get_text(self.covid19_page.DISCLAIMER_TEXT_IS), \
            "DISCLAIMER is not displayed"
        self.covid19_page.click_telehealth_option_is()
        assert "telehealth" in self.covid19_page.get_url()
        assert self.covid19_page.is_visible(self.covid19_page.SCHEDULE_BTN)

    def __test_verify_what_works_section(self):
        self.covid19_page.scroll_to_element(self.covid19_page.HEADER)
        assert self.covid19_page.is_visible(self.covid19_page.HEADER), "Header is not displayed"
        assert "Find what works for you." in self.covid19_page.get_text(self.covid19_page.HEADER_TEXT_IS), \
            "HEADER TEXT is not displayed"
        assert self.covid19_page.is_visible(self.covid19_page.P_TEXT_IS)
        assert ("There are many ways to test for COVID-19 or the flu and treat your symptoms. "
        "This guide makes it easier to choose your next step.") in self.covid19_page.get_text(self.covid19_page.P_TEXT_IS), "p text is not displayed"
        self.covid19_page.click_go_to_guide()
        assert "I need to know if I have COVID‑19 or flu." in self.covid19_page.get_text(self.covid19_page.MIGHT_HAVE_TEXT), "Might have text is not displayed"
        assert "I tested positive for COVID‑19 or flu." in self.covid19_page.get_text(self.covid19_page.TESTED_POSITIVE_TEXT), "Tested positive text is not displayed"
        self.covid19_page.wait_until_visible(self.covid19_page.MIGHT_HAVE)
        self.covid19_page.click_might_have()
        assert self.covid19_page.is_visible(self.covid19_page.ANTIGEN_TESTS_HEADER, timeout=10), "ANTIGEN_TESTS_HEADER is not displayed"
        assert "The sooner you test, the sooner you’ll have answers." in self.covid19_page.get_text(self.covid19_page.ANTIGEN_HEADER_TEXT_IS), "Antigen text is not displayed"
        assert ("There are many tests that can detect if you have COVID-19 or flu. "
        "Order online and get a test delivered as early as today.") in self.covid19_page.get_text(self.covid19_page.MIGHT_HAVE_P_TEXT), "Might have text is not displayed"
        assert "Shop tests on Amazon" in self.covid19_page.get_text(self.covid19_page.MOLECULAR_TESTS_HEADER_TEXT), "Molecular tests is not displayed"
        assert "Shop tests on Instacart" in self.covid19_page.get_text(self.covid19_page.ANTIGEN_TESTS_HEADER_TEXT), "Antigen tests is not displayed"
        self.covid19_page.click_antigen_tests_header_button()
        assert "Additional support you can find on PfizerForAll" in self.covid19_page.get_text(self.covid19_page.ADDITIONAL_SUPPORT_HEADER_TEXT), \
            "Additional support text is not displayed"
        assert "Respiratory illness? Talk to a telehealth doctor." in self.covid19_page.get_text(self.covid19_page.RESPIRATORY_ILLNESS_HEADER_TEXT), \
            "Respiratory illness text is not displayed"
        assert "Stay home and talk to a doctor online" in self.covid19_page.get_text(self.covid19_page.RESPIRATORY_ILLNESS_INFO_TEXT), \
            "Response text is not displayed"
        assert self.covid19_page.is_visible(self.covid19_page.LEARN_HOW_BUTTON)
        assert "Learn how" in self.covid19_page.get_text(self.covid19_page.LEARN_HOW_BUTTON), "Learn how is not displayed"
        assert "Keep up with vaccinations." in self.covid19_page.get_text(self.covid19_page.KEEP_UP_WITH_VACCINATION_HEADER_TEXT), "Keep up text is not displayed"
        assert "Help protect yourself from contagious" in self.covid19_page.get_text(self.covid19_page.KEEP_UP_WITH_VACCINATION_INFO_TEXT), \
            "Help protect yourself from contagious is not displayed"
        assert "See how" in self.covid19_page.get_text(self.covid19_page.SEE_HOW_BUTTON), "See how is not displayed"
        assert "Take a test, right at home." in self.covid19_page.get_text(self.covid19_page.TAKE_A_TEST_RIGHT_AT_HOME_HEADER_TEXT), \
            "Take a test, right at home is not displayed"
        assert "COVID-19 or flu? With some similar" in self.covid19_page.get_text(self.covid19_page.TAKE_A_TEST_RIGHT_AT_HOME_INFO_TEXT), \
            "COVID-19 or flu? With some similar is not displayed"
        assert self.covid19_page.is_visible(self.covid19_page.EXPLORE_YOUR_OPTIONS_BUTTON)
        assert "Explore your options" in self.covid19_page.get_text(self.covid19_page.EXPLORE_YOUR_OPTIONS_BUTTON), "Explore your options is not displayed"
        assert self.covid19_page.is_visible(self.covid19_page.MOLECULAR_TESTS_HEADER_TEXT_AMAZON)
        assert self.covid19_page.is_visible(self.covid19_page.MOLECULAR_TESTS_HEADER_BUTTON)
        self.covid19_page.click_molecular_tests_header_button()
        assert self.covid19_page.is_visible(self.covid19_page.ANTIGEN_TESTS_HEADER_INSTACART)
        # assert self.covid19_page.is_visible(self.covid19_page.MOLECULAR_TESTS_HEADER_AMAZON

    def test_verify_tested_positive_for_covid19(self):
        self.covid19_page.click_go_to_guide()
        assert self.covid19_page.is_visible(self.covid19_page.TESTED_POSITIVE), "tested_positive is not displayed"
        assert "I tested positive for COVID‑19 or flu." in self.covid19_page.get_text(self.covid19_page.TESTED_POSITIVE_TEXT), "I tested positive text is not displayed"
        self.covid19_page.click_tested_positive_button()
        self.home_page.wait_for_timeout(1)
        assert "If you’re sick, you can talk to a doctor about treatments now." in self.covid19_page.get_text(self.covid19_page.QUICK_ANSWER_GUIDE_TEXT), "Quick answer text is not displayed"
        assert self.covid19_page.is_visible(self.covid19_page.TELEHEALTH_APPOINTMENT_TEXT), "Telehealth appointment text is not displayed"
        assert "Book a $35 telehealth appointment" in self.covid19_page.get_text(self.covid19_page.TELEHEALTH_APPOINTMENT_TEXT_IS), "Book a $35 telehealth appointment is not displayed"
        assert "Book an in‑person appointment" in self.covid19_page.get_text(self.covid19_page.BOOK_IN_PERSON_APPOINTMENT_TEXT), "Book in person appointment is not displayed"
        self.covid19_page.click_telehealth_appointment_link()
        self.covid19_page.click_see_doctor_at_upscript()
        # Then There are '2' tabs currently opened
        # And The url 'https://upscriptcare.com/products/respiratory?t=respiratory_s2' is opened in a new tab
        self.home_page.wait_for_timeout(1)
        assert self.covid19_page.is_visible(self.covid19_page.TELEHEALTH_APPOINTMENT_LINK)
        assert self.covid19_page.is_visible(self.covid19_page.BOOK_IN_PERSON_APPOINTMENT_LINK)
        self.covid19_page.click_book_in_person_appointment_link()
        assert self.covid19_page.is_visible(self.covid19_page.LEAVING_PFIZER_TO_ZOCDOC_TEXT)
        self.covid19_page.click_continue_to_zocdoc()
        assert self.covid19_page.is_visible(self.covid19_page.TELEHEALTH_APPOINTMENT_LINK)

        #  Scenario 4
    def __test_verify_some_respiratory_conditions_section(self):
        self.covid19_page.scroll_to_element(self.covid19_page.RESPIRATORY_TEXT)
        assert "Some respiratory conditions have some similar symptoms. Here are a few of the most common." in self.covid19_page.get_text(self.covid19_page.RESPIRATORY_TEXT)
        # assert not self.covid19_page.is_element_enabled(self.covid19_page.COVID19), "COVID19 is not enabled"
        assert self.covid19_page.is_visible(self.covid19_page.COVID19_TEXT)
        assert "COVID‑19" in self.covid19_page.get_text(self.covid19_page.COVID19_TEXT), "Covid19 is not displayed"
        assert "COVID‑19 symptoms can include fever, chills, shortness of breath, fatigue, new loss of taste or smell, sore throat, nausea, vomiting, and diarrhea. Some can be similar to other respiratory conditions like the common cold, flu, or even pneumonia." in self.covid19_page.get_text(self.covid19_page.COVID19_INFO_TEXT)
        # assert not self.covid19_page.is_element_enabled(self.covid19_page.FLU), "FLU is not enabled"
        assert self.covid19_page.is_visible(self.covid19_page.FLU_TEXT)
        assert "Flu" in self.covid19_page.get_text(self.covid19_page.FLU_TEXT), "Flu is not displayed"
        assert "Influenza (you might know it as flu) peaks seasonally, often starting in October and can continue as late as May. It can range from mild to severe, infecting the nose, throat, or lungs." in self.covid19_page.get_text(self.covid19_page.FLU_INFO_TEXT)
        # assert not self.covid19_page.is_element_enabled(self.covid19_page.RSV), "RSV is not enabled"
        assert self.covid19_page.is_visible(self.covid19_page.RSV_TEXT), "RSV is not displayed"
        assert "RSV (respiratory syncytial virus) is a common respiratory virus that can spread easily. Symptoms can be mild and may include fever, congestion, runny nose, or sore throat. It can be more serious for infants and young children, adults 75 years and older, and pregnant people." in self.covid19_page.get_text(self.covid19_page.RSV_INFO_TEXT)
        # assert not self.covid19_page.is_element_enabled(self.covid19_page.PNEUMONIA), "pneumonia is not enabled"
        assert self.covid19_page.is_visible(self.covid19_page.PNEUMONIA_TEXT), "Pneumonia is not displayed"
        assert "Pneumococcal pneumonia is an infection of the lungs. If you're 50+ or 19+ with certain chronic conditions like asthma, diabetes, COPD, or heart disease, you're at increased risk for pneumonia." in self.covid19_page.get_text(self.covid19_page.PNEUMONIA_INFO_TEXT)

        # # Scenario 5cards on Some respiratory conditions section
    def __test_verify_cards_on_some_respiratory_conditions_section(self):
        self.covid19_page.scroll_to_element(self.covid19_page.TALK_TO_A_DOCTOR_NOW)
        assert self.covid19_page.is_element_enabled(self.covid19_page.TALK_TO_A_DOCTOR_NOW)
        assert "Talk to a doctor now about treatment options. Get your medications delivered right to your door." in self.covid19_page.get_text(self.covid19_page.TALK_TO_A_DOCTOR_NOW_TEXT)
        assert self.covid19_page.is_visible(self.covid19_page.PHONE_IMAGE), "Phone image is not displayed"
        assert self.covid19_page.is_visible(self.covid19_page.TALK_TO_A_DOCTOR_NOW_ARROW_BUTTON), "Talk to a doctor now about treatment options is not displayed"
        self.covid19_page.click_talk_to_a_doctor_now_arrow_button()
        assert f"{self.base_url}/respiratory/telehealth" in self.covid19_page.get_url()
        self.home_page.go_back_to_previous_page()
        self.home_page.wait_for_timeout(10)
        self.covid19_page.scroll_to_element(self.covid19_page.MAKE_AN_APPOINTMENT)
        assert self.covid19_page.is_element_enabled(self.covid19_page.MAKE_AN_APPOINTMENT)
        assert "Make an appointment to see a doctor near you, on your schedule." in self.covid19_page.get_text(self.covid19_page.MAKE_AN_APPOINTMENT_TEXT), "Make an appointment not displayed"
        assert self.covid19_page.is_visible(self.covid19_page.STETHOSCOPE_IMAGE), "Stethoscope image is not displayed"
        assert self.covid19_page.is_visible(self.covid19_page.MAKE_AN_APPOINTMENT_ARROW_BUTTON), "Make an appointment arrow button is not displayed"
        self.covid19_page.click_make_an_appointment_arrow_button()
        assert f"{self.base_url}/respiratory/in-person-appointment" in self.covid19_page.get_url()
        self.home_page.go_back_to_previous_page()
        self.home_page.wait_for_timeout(10)
        self.covid19_page.scroll_to_element(self.covid19_page.ORDER_TESTS)
        assert self.covid19_page.is_element_enabled(self.covid19_page.ORDER_TESTS)
        assert "Order tests for COVID‑19 and flu and get them delivered today." in self.covid19_page.get_text(self.covid19_page.ORDER_TESTS_TEXT)
        assert self.covid19_page.is_visible(self.covid19_page.SWAB_IMAGE), "SWAB image is not displayed"
        assert self.covid19_page.is_visible(self.covid19_page.ORDER_TESTS_ARROW_BUTTON), "Order tests arrow button is not displayed"
        self.covid19_page.click_order_tests_arrow_button()
        assert f"{self.base_url}/respiratory/testing" in self.covid19_page.get_url()

    #   Scenario 6
    def __test_verify_respiratory_conditions_and_faq_answers(self):
        self.covid19_page.scroll_to_element(self.covid19_page.FAG_SCETION_TEXT)
        assert "Frequently asked questions" in self.covid19_page.get_text(self.covid19_page.FAG_SCETION_TEXT), "Frequently asked questions is not displayed"
        self.covid19_page.scroll_to_element(self.covid19_page.FAG_ONE_QUESTION)
        self.covid19_page.click_fag_one_question()
        assert "Yes. There are quite a few viruses and diseases that can impact your airways and lungs. Infections from viruses can cause seasonal respiratory illnesses like colds and flu, which typically go away over time, unlike chronic respiratory conditions like asthma and COPD, which can stick around. Additionally, some people are more at risk for more serious illness from respiratory conditions than others. These include older adults, pregnant women, those with certain health conditions (like diabetes or chronic heart disease), and those who have a weakened immune system." in self.covid19_page.get_text(self.covid19_page.FAG_ONE_TEXT)
        self.covid19_page.scroll_to_element(self.covid19_page.FAG_TWO_QUESTION)
        self.covid19_page.click_fag_two_question()
        assert "Simply put, COVID‑19, flu, and RSV are contagious and for some, they could be deadly. FDA-approved vaccines now exist for COVID‑19, flu (influenza), and RSV for certain eligible people. Vaccinations are key when it comes to helping prevent infection and for some respiratory conditions, they can help protect against serious illness and even death.Certain people are also more at risk for serious illness than others. That’s why it’s important to always stay up to date on your vaccinations to help protect yourself and others." in self.covid19_page.get_text(self.covid19_page.FAG_TWO_PART1_TEXT)
        self.covid19_page.click_fag_two_question()
        self.covid19_page.scroll_to_element(self.covid19_page.FAG_THREE_QUESTION)
        self.covid19_page.click_fag_three_question()
        assert self.covid19_page.is_visible(self.covid19_page.FAG_THREE_ANSWER), "Fag three answer is not displayed"
        assert "You can order antigen or molecular COVID‑19 tests on our testing page and have them shipped right to your home. Not sure what type of test to get? We can explain your options and get a test to you today or within 24 hours." in self.covid19_page.get_text(self.covid19_page.FAG_THREE_ANSWER_TEXT_IS)
        self.covid19_page.click_fag_three_question()
        self.covid19_page.scroll_to_element(self.covid19_page.FAG_FOUR_QUESTION)
        self.covid19_page.click_fag_four_question()
        assert self.covid19_page.is_visible(self.covid19_page.FAG_FOUR_ANSWER), "Fag four answer is not displayed"
        assert "Yes, you can. There are at-home tests that check for both COVID‑19 and/or flu. Since COVID‑19 and flu share some similar symptoms, testing for both viruses is important. Order one here." in self.covid19_page.get_text(self.covid19_page.FAG_FOUR_ANSWER_TEXT_IS)
