from pages.base_page import BasePage


class Covid19OverviewPage(BasePage):

    # covid19 home page locators
    ACCEPT_ALL = ('XPATH', "//button[contains(@id, 'onetrust-accept-btn-handler')]")
    MENU = ('XPATH', "(//button[contains(@class, 'primary')])[1]")
    COVID19_FLU = ('XPATH', "(//a[contains(@role, 'button')])[3]")
    COVID19_FLU_OVERVIEW = ('XPATH', "//*[text()='COVID-19 & flu overview']")
    TITLE_PFIZER_FOR_ALL = ('XPATH', "(//span[contains(@aria-label, 'Pfizer for all home page')])[2]")

    # Scenario 1:- Verify hero section, telehealth page and disclaimer text
    HERO_TEXT = ('XPATH', "//*[text()='When you’re having']")
    HERO_TEXT_CONTAINS_COVID19 = ('XPATH', "//h1[contains(@id, 'when-youre-havingcovid-19or-flusymptoms-dontwaittalk-to-a-doctor')]")
    BOOK_A_35_VIRTUAL_VISIT_NOW = ('XPATH', "//a[contains(@aria-label, 'Book a $35 virtual visit now')]")
    LEARN_ABOUT_YOUR_TELEHEALTH_OPTIONS = ('XPATH', "//a[contains(@aria-label, 'Learn about your telehealth options')]")
    DISCLAIMER_TEXT_IS = ('XPATH', "//div[@class='section fragment-container custom-form-container']//div[@class= 'default-content-wrapper']")
    TELEHEALTH_OPTION_IS = ('XPATH', "//a[contains(@id, 'respiratory-non-homepage-options-0')]")
    SCHEDULE_BTN = ('XPATH', "(//a[contains(@aria-label, 'Schedule with UpScriptCare for $35')])[1]")

    # Scenario 2:- Verify Find what works for you section
    HEADER = ('XPATH', "//h2[contains(@id, 'find-what-works-for-you')]")
    HEADER_TEXT_IS = ('XPATH', "//*[text()='Find what works for you.']")
    P_TEXT_IS = ('XPATH', "//div[@data-valign='middle']/h2[@id='find-what-works-for-you']/../p[1]")
    GO_TO_GUIDE = ('XPATH', "//a[contains(@aria-label, 'Find what works for you, Go to the guide')]")
    MIGHT_HAVE_TEXT = ('XPATH', "//*[text()='I need to know if I have COVID‑19 or flu.']")
    TESTED_POSITIVE_TEXT = ('XPATH', "//*[text()='I tested positive for COVID‑19 or flu.']")
    MIGHT_HAVE = ('XPATH', "//a[contains(@aria-label, 'I need to know if I have COVID‑19 or flu.')]")
    ANTIGEN_TESTS_HEADER = ('XPATH', "//h2[contains(@ id, 'the-sooner-you-test-the-sooner-youll-have-answers')]")
    ANTIGEN_HEADER_TEXT_IS = ('XPATH', "//h2[contains(@ id, 'the-sooner-you-test-the-sooner-youll-have-answers')]")
    MIGHT_HAVE_P_TEXT = ('XPATH', "//div[@data-valign='middle']/h2[@id='the-sooner-you-test-the-sooner-youll-have-answers']/..")
    MOLECULAR_TESTS_HEADER_TEXT = ('XPATH', "//h3[contains(@id, 'shop-tests-on-amazon')]")
    ANTIGEN_TESTS_HEADER_TEXT = ('XPATH', "//h3[contains(@id, 'shop-tests-on-instacart')]")
    ANTIGEN_TESTS_HEADER_BUTTON = ('XPATH', "(//a[contains(@aria-label, 'Shop tests on Instacart')])[1]")
    ADDITIONAL_SUPPORT_HEADER_TEXT = ('XPATH', "//h3[contains(@id, 'additional-support-you-can-find-on-pfizerforall')]")
    RESPIRATORY_ILLNESS_HEADER_TEXT = ('XPATH', "(//*[text()='Respiratory illness? Talk to a telehealth doctor.'])[2]")
    RESPIRATORY_ILLNESS_INFO_TEXT = ('XPATH', "//*[text()='Stay home and talk to a doctor online today.']")
    LEARN_HOW_BUTTON = ('XPATH', "//a[contains(@aria-label, 'Respiratory illness? Talk to a telehealth doctor, Learn how')]")
    KEEP_UP_WITH_VACCINATION_HEADER_TEXT = ('XPATH', "(//h3[contains(@id, 'keep-up-with-vaccinations.')])[2]")
    KEEP_UP_WITH_VACCINATION_INFO_TEXT = ('XPATH', "//*[text()='Help protect yourself from contagious viruses such as COVID-19 and RSV. Check eligibility and book an appointment.']")
    SEE_HOW_BUTTON = ('XPATH', "//a[contains(@aria-label, 'Keep up with vaccinations, See how')]")
    TAKE_A_TEST_RIGHT_AT_HOME_HEADER_TEXT = ('XPATH', "(//h3[contains(@id, 'take-a-test-right-at-home.')])[2]")
    TAKE_A_TEST_RIGHT_AT_HOME_INFO_TEXT = ('XPATH', "(//*[text()='COVID-19 or flu? With some similar symptoms, it’s hard to know. At-home tests are available. Explore your options.'])[2]")
    EXPLORE_YOUR_OPTIONS_BUTTON = ('XPATH', "//a[contains(@aria-label, 'Take a test, right at home, Explore your options')]")
    # ======================
    'Then There are "2" tabs currently opened'
    " When I focus the last opened window "
    " Then The page url contains 'www.instacart.com/store/brands/pfizer-for-all "
    " When I close the current opened tab "
    " And I focus the last opened window "
    " And The element 'covid19_page > dialog_box > close_btn' is displayed "
    " And I click on element 'covid19_page > dialog_box > close_btn' "
    MOLECULAR_TESTS_HEADER_TEXT_AMAZON = ('xpath', "//h3[contains(@id, 'shop-tests-on-amazon')]")
    MOLECULAR_TESTS_HEADER_BUTTON = ('XPATH', "(//a[contains(@aria-label, 'Shop tests on Amazon')])[1]")
    "Then There are '2' tabs currently opened"
    "When I focus the last opened window"
    " Then The page url contains 'https://www.amazon.com/s?k=covid-flu+test'"
    "  When I close the last opened window "
    " And I focus the last opened window "
    " And The element 'covid19_page > dialog_box > close_btn' is displayed "
    " And I click on element 'covid19_page > dialog_box > close_btn' "
    ANTIGEN_TESTS_HEADER_INSTACART = ('XPATH', "//h2[contains(@id, 'the-sooner-you-test-the-sooner-youll-have-answers')]")
    MOLECULAR_TESTS_HEADER_AMAZON = ('XPATH', "//h3[contains(@ id, 'shop-tests-on-amazon')]")
    # Scenario 3:-  Verify I tested positive for COVID-19 or flu on the How can we help section - telehealth and in person appointment
    TESTED_POSITIVE = ('XPATH', "//h2[contains(@id, 'i-tested-positive-for-covid19-or-flu')]")
    TESTED_POSITIVE_BUTTON = ('XPATH', "//a[contains(@aria-label, 'I tested positive for COVID‑19 or flu.')]")
    QUICK_ANSWER_GUIDE_TEXT = ('XPATH', "//h2[contains(@id, 'if-youre-sick-you-can-talk-to-a-doctor-about-treatments-now')]")
    TELEHEALTH_APPOINTMENT_TEXT = ('XPATH', "//a[contains(@id, 'respiratory-quick-answer-guide-2')]")
    TELEHEALTH_APPOINTMENT_TEXT_IS = ('XPATH', "//a[contains(@aria-label, 'Book a $35 telehealth appointment')]")
    BOOK_IN_PERSON_APPOINTMENT_TEXT = ('XPATH', "//h3[contains(@id, 'book-an-inperson-appointment')]")
    TELEHEALTH_APPOINTMENT_LINK = ('XPATH', "//a[contains(@aria-label, 'Book a $35 telehealth appointment')]")
    SEE_DOCTOR_AT_UPSCRIPT = ('XPATH', "//a[contains(@id, 'overlay-external-link-0')]")
    "   Then There are '2' tabs currently opened "
    "  And The url 'https://upscriptcare.com/products/respiratory?t=respiratory_s2' is opened in a new tab "
    " When I pause for '3' s "
    " And I close the last opened window "
    " And I focus the last opened window "
    "  And The element 'covid19_page > dialog_box > close_btn' is displayed "
    "  And I click on element 'covid19_page > dialog_box > close_btn' "
    BOOK_IN_PERSON_APPOINTMENT_LINK = ('XPATH', "//a[contains(@aria-label, 'Book an in‑person appointment')]")
    LEAVING_PFIZER_TO_ZOCDOC_TEXT = ('XPATH', "(//*[text()='You are leaving PfizerForAll™ to go to Zocdoc.com'])[2]")
    CONTINUE_TO_ZOCDOC = ('XPATH', "(//a[contains(@class, 'button primary long-cta')])[2]")

    " Then There are '2' tabs currently opened "
    " When I focus the last opened window "
    "Then The page url contains 'https://www.zocdoc.com' "
    " When I pause for '3' s "
    " And I close the last opened window "
    " And I focus the last opened window "
    " And I click on element 'covid19_page > dialog_box > close_btn' "

    # Scenario 4:-  Verify Some respiratory conditions section
    RESPIRATORY_TEXT = ('XPATH', "//h2[contains(@id, 'some-respiratory-conditions-have-some-similar-symptoms-here-are-a-few-of-the-most-common')]")
    COVID19 = ('XPATH', "//h3[contains(@id, 'covid19')]")
    COVID19_TEXT = ('XPATH', "//h3[contains(@ id, 'covid19')]")
    COVID19_INFO_TEXT = ('XPATH', "(//div[contains(@class, 'cards horizontal-scroll body-cards disable-hover-effect block')]//li[contains(@data-smartcapture, 'slideshow-slide')])[1]")
    FLU = ('XPATH', "//h3[contains(@id, 'flu')]")
    FLU_TEXT = ('XPATH', "//h3[contains(@id, 'flu')]")
    FLU_INFO_TEXT = ('XPATH', "(//div[contains(@class, 'cards horizontal-scroll body-cards disable-hover-effect block')]//li[contains(@data-smartcapture, 'slideshow-slide')])[2]")
    RSV = ('XPATH', "//h3[contains(@id, 'rsv')]")
    RSV_TEXT = ('XPATH', "//h3[contains(@id, 'rsv')]")
    RSV_INFO_TEXT = ('XPATH', "(//div[contains(@class, 'cards horizontal-scroll body-cards disable-hover-effect block')]//li[contains(@data-smartcapture, 'slideshow-slide')])[3]")
    PNEUMONIA = ('XPATH', "//h3[contains(@id, 'pneumonia')]")
    PNEUMONIA_TEXT = ('XPATH', "//h3[contains(@id, 'pneumonia')]")
    PNEUMONIA_INFO_TEXT = ('XPATH', "(//div[contains(@class, 'cards horizontal-scroll body-cards disable-hover-effect block')]//li[contains(@data-smartcapture, 'slideshow-slide')])[4]")

    # Scenario 5:-  Verify clickable cards on Some respiratory conditions section

    TALK_TO_A_DOCTOR_NOW = ('XPATH', "(//*[text()='Talk to a doctor now'])[3]")
    TALK_TO_A_DOCTOR_NOW_TEXT = ('XPATH', "//h2[contains(@id, 'talk-to-a-doctor-now-about-treatment-options-get-your-medications-delivered-right-to-your-door')]")
    PHONE_IMAGE = ('XPATH', "//img[@alt='Hand holding phone']")
    TALK_TO_A_DOCTOR_NOW_ARROW_BUTTON = ('XPATH', "//a[contains(@id, 'respiratory-non-homepage--2')]")
    MAKE_AN_APPOINTMENT = ('XPATH', "//*[text()='Make an appointment']")
    MAKE_AN_APPOINTMENT_TEXT = ('XPATH', "//h2[contains(@id, 'make-an-appointment-to-see-a-doctor-near-you-on-your-schedule')]")
    STETHOSCOPE_IMAGE = ('XPATH', "//*[@alt='Stethoscope']")
    MAKE_AN_APPOINTMENT_ARROW_BUTTON = ('XPATH', "//a[contains(@id, 'respiratory-non-homepage--3')]")
    ORDER_TESTS = ('XPATH', "//*[text()='Order tests']")
    ORDER_TESTS_TEXT = ('XPATH', "//*[text()=' for COVID‑19 and flu and get them delivered today.']")
    SWAB_IMAGE = ('XPATH', "//img[@alt='Hand holding swab']")
    ORDER_TESTS_ARROW_BUTTON = ('XPATH', "//a[contains(@id, 'respiratory-non-homepage--4')]")

    # Scenario 6:- Verify Some respiratory conditions - FAQ section

    FAG_SCETION_TEXT = ('XPATH', "//h2[contains(@id, 'frequently-asked-questions')]")
    FAG_ONE_QUESTION = ('XPATH', "(//span[contains(@class, 'icon icon-lib-mat-expand-more')])[1]")
    FAG_ONE_TEXT = ('XPATH', "(//div[contains(@class, 'custom-accordion-item-body')])[1]")
    FAG_TWO_QUESTION = ('XPATH', "(//span[contains(@class, 'icon icon-lib-mat-expand-more')])[2]")
    FAG_TWO_PART1_TEXT = ('XPATH', "(//div[contains(@class, 'custom-accordion-item-body')])[2]")
    FAG_THREE_QUESTION = ('XPATH', "(//span[contains(@class, 'icon icon-lib-mat-expand-more')])[3]")
    FAG_THREE_ANSWER = ('XPATH', "(//div[contains(@class, 'custom-accordion-item-body')])[3]")
    FAG_THREE_ANSWER_TEXT_IS = ('XPATH', "(//div[contains(@class, 'custom-accordion-item-body')])[3]")
    FAG_FOUR_QUESTION = ('XPATH', "(//span[contains(@class, 'icon icon-lib-mat-expand-more')])[4]")
    FAG_FOUR_ANSWER = ('XPATH', "(//div[contains(@class, 'custom-accordion-item-body')])[4]")
    FAG_FOUR_ANSWER_TEXT_IS = ('XPATH', "(//div[contains(@class, 'custom-accordion-item-body')])[4]")

    def click_covid19_overview_page(self):
        self.wait_until_visible(self.COVID19_FLU_OVERVIEW, timeout=10)
        self.click(self.COVID19_FLU_OVERVIEW)

    def click_menu(self):
        self.wait_until_visible(self.MENU, timeout=10)
        self.click(self.MENU)

    def click_covid19_flu(self):
        self.wait_until_visible(self.COVID19_FLU, timeout=10)
        self.click(self.COVID19_FLU)

    def click_covid19_flu_overview(self):
        self.wait_until_visible(self.COVID19_FLU_OVERVIEW, timeout=10)
        self.click(self.COVID19_FLU_OVERVIEW)

    def click_telehealth_option_is(self):
        self.wait_until_visible(self.TELEHEALTH_OPTION_IS, timeout=10)
        self.click(self.TELEHEALTH_OPTION_IS)

    def click_go_to_guide(self):
        self.wait_until_visible(self.GO_TO_GUIDE, timeout=10)
        self.click(self.GO_TO_GUIDE)

    def click_might_have(self):
        self.wait_until_visible(self.MIGHT_HAVE, timeout=15)
        self.click(self.MIGHT_HAVE)

    def click_antigen_tests_header_button(self):
        self.wait_until_visible(self.ANTIGEN_TESTS_HEADER_BUTTON, timeout=10)
        self.click(self.ANTIGEN_TESTS_HEADER_BUTTON)

    def click_molecular_tests_header_button(self):
        self.wait_until_visible(self.MOLECULAR_TESTS_HEADER_BUTTON, timeout=10)
        self.click(self.MOLECULAR_TESTS_HEADER_BUTTON)

    def click_tested_positive_button(self):
        self.wait_until_visible(self.TESTED_POSITIVE_BUTTON, timeout=10)
        self.click(self.TESTED_POSITIVE_BUTTON)

    def click_telehealth_appointment_link(self):
        self.wait_until_visible(self.TELEHEALTH_APPOINTMENT_LINK, timeout=10)
        self.click(self.TELEHEALTH_APPOINTMENT_LINK)

    def click_see_doctor_at_upscript(self):
        self.wait_until_visible(self.SEE_DOCTOR_AT_UPSCRIPT, timeout=10)
        self.click(self.SEE_DOCTOR_AT_UPSCRIPT)

    def click_book_in_person_appointment_link(self):
        self.wait_until_visible(self.BOOK_IN_PERSON_APPOINTMENT_LINK, timeout=10)
        self.click(self.BOOK_IN_PERSON_APPOINTMENT_LINK)

    def click_continue_to_zocdoc(self):
        self.wait_until_visible(self.TALK_TO_A_DOCTOR_NOW_ARROW_BUTTON, timeout=10)
        self.click(self.TALK_TO_A_DOCTOR_NOW_ARROW_BUTTON)

    def click_talk_to_a_doctor_now_arrow_button(self):
        self.wait_until_visible(self.TALK_TO_A_DOCTOR_NOW_ARROW_BUTTON, timeout=10)
        self.click(self.TALK_TO_A_DOCTOR_NOW_ARROW_BUTTON)

    def click_make_an_appointment_arrow_button(self):
        self.wait_until_visible(self.MAKE_AN_APPOINTMENT_ARROW_BUTTON, timeout=10)
        self.click(self.MAKE_AN_APPOINTMENT_ARROW_BUTTON)

    def click_order_tests_arrow_button(self):
        self.wait_until_visible(self.ORDER_TESTS_ARROW_BUTTON, timeout=10)
        self.click(self.ORDER_TESTS_ARROW_BUTTON)

    def click_fag_one_question(self):
        self.wait_until_visible(self.FAG_ONE_QUESTION, timeout=10)
        self.click(self.FAG_ONE_QUESTION)

    def click_fag_two_question(self):
        self.wait_until_visible(self.FAG_TWO_QUESTION, timeout=10)
        self.click(self.FAG_TWO_QUESTION)

    def click_fag_three_question(self):
        self.wait_until_visible(self.FAG_THREE_QUESTION, timeout=10)
        self.click(self.FAG_THREE_QUESTION)

    def click_fag_four_question(self):
        self.wait_until_visible(self.FAG_FOUR_QUESTION, timeout=10)
        self.click(self.FAG_FOUR_QUESTION)

