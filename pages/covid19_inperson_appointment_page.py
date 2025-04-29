from pages.base_page import BasePage


class Covid19InPersonAppointmentPage(BasePage):

    ACCEPT_ALL = ('XPATH', "//button[contains(@id, 'onetrust-accept-btn-handler')]")
    MENU_BUTTON = ('XPATH', "(//button[contains(@class, 'primary')])[1]")
    COVID19_FLU_TEXT_IS = ('XPATH', "//a[text()='COVID-19 & flu']")
    COVID19_FLU_BUTTON = ('XPATH', "//a[text()='COVID-19 & flu']")
    COVID19_FLU_OVERVIEW_TEXT_IS = ('XPATH', "//a[text()='COVID-19 & flu overview']")
    COVID19_FLU_OVERVIEW_BUTTON = ('XPATH', "//a[text()='COVID-19 & flu overview']")
    MAKE_AN_APPOINTMENT = ('XPATH', "//h2[contains(@id, 'make-an-appointment-to-see-a-doctor-near-you-on-your-schedule')]")
    MAKE_AN_APPOINTMENT_ARROW_BUTTON = ('XPATH', "//a[contains(@id, 'respiratory-non-homepage--3')]")
    TITLE = ('XPATH', "//span[contains(@class, 'icon icon-pfizer-for-all-home')]")
    TITLE_TEXT_IS = ('XPATH', "//h1[contains(@id, 'see-a-doctor-in-person-near-you')]")
    SUBTEXT_TEXT_IS = ('XPATH',"//p[text()='We’ve made it simple to find one. Make an appointment to talk to a doctor near you, on your schedule.']")
    # Scenario 1
    BOOK_APPOINTMENT_BUTTON = ('XPATH', "//a[contains(@id, 'respiratory-in-person-appointment-2')]")
    ZOCDOC_TITLE_TEXT_IS = ('XPATH', "//div[@class='top-text']//h2[contains(@id, 'you-are-leaving-pfizerforall-to-go-to-zocdoccom')]")
    CONTINUE_TO_ZOCDOC_BUTTON_TEXT = ('XPATH', "//a[contains(@id, 'overlay-external-link-0')]")
    DISCLAIMER_TEXT_IS = ('XPATH', "//*[text()='By clicking the link above, you will be redirected to a third-party website that is neither owned nor controlled by Pfizer. Pfizer is not responsible for the content or services of this third-party website.']")
    # Scenario :-2
    BOOKING_HEADING = ('XPATH', "//h2[contains(@id, 'booking-is-quick-and-simple')]")
    HEADING_TEXT_IS = ('XPATH', "//*[text()='Booking is quick and simple.']")
    BOOKING_SUBTEXT_IS = ('XPATH', "//*[text()='Provided by Zocdoc']")
    STEP_1_TAG_TEXT = ('XPATH', "//*[text()='Step 1']")
    STEP_1_HEADING_TEXT = ('XPATH', "//h3[contains(@id, 'search-for-a-doctor-near-you')]")
    STEP_1_TEXT_IS = ('XPATH', "//*[text()='Select a provider type and enter your ZIP code.']")
    STEP_2_TAG_TEXT = ('XPATH', "//*[text()='Step 2']")
    STEP_2_HEADING_TEXT = ('XPATH', "//h3[contains(@id, 'choose-who-you-want-to-see')]")
    STEP_2_TEXT_IS = ('XPATH', "//div[text()='Read patient reviews and provider profiles. See availability, insurance coverage, and more.']")
    STEP_3_TAG_TEXT = ('XPATH', "//*[text()='Step 3']")
    STEP_3_HEADING_TEXT = ('XPATH', "//h3[contains(@id, 'schedule-an-appointment-that-works-best-for-you')]")
    CONFIRMED_TAG_TEXT = ('XPATH', "//p[text()='Confirmed']")
    CONFIRMED_HEADING_TEXT_IS = ('XPATH', "//h3[contains(@id, 'get-confirmation')]")
    CONFIRMED_TEXT_IS = ('XPATH', "//div[text()='Receive an email with appointment details, and you’re ready to go!']")
    # Scenario :- 3
    SAVE_PRESCRIBED_MEDICATIONS_SECTION = ('XPATH', "//h2[contains(@id, 'save-on-your-prescribed-pfizer-medications-and-get-support-when-you-need-it')]")
    SAVE_PRESCRIBED_MEDICATIONS_TITLE_TEXT_IS = ('XPATH', "//h2[contains(@id, 'save-on-your-prescribed-pfizer-medications-and-get-support-when-you-need-it')]")
    SAVE_PRESCRIBED_MEDICATIONS_SUBTEXT_IS = ('XPATH',"//p[text()='From co-pay savings cards to financial assistance programs, we have options that can help. Our dedicated customer support team can also help you navigate your insurance benefits, understand your options, and more.']")
    GET_STARTED_BUTTON_TEXT_IS = ('XPATH', "//span[text()='Get started']")
    GET_STARTED_BUTTON = ("XPATH", "//a[contains(@id, 'respiratory-in-person-appointment-started-0')]")
    # Scenario :- 4
    BOTTOM_OF_THE_PAGE = ('XPATH', "//p[text()='© 2025 Pfizer Inc. All rights reserved. PP-UNP-USA-6048']")
    BOTTOM_OF_DISCLAIMER_TEXT_IS = ("XPATH", "//div[@class='section fragment-container custom-form-container']//div[@class= 'default-content-wrapper']")
    # Scenario :- 5
    FAG_SECTION = ('XPATH', "//h2[contains(@id, 'frequently-asked-questions')]")
    FAG_1_ICON = ('XPATH', "(//span[contains(@class, 'icon icon-lib-mat-expand-more')])[1]")
    FAG_1_DETAILS = ('XPATH', "(//div[contains(@class, 'custom-accordion-item-body')])[1]")
    FAG_1_DETAILS_TEXT_IS = ('XPATH', "(//div[contains(@class, 'custom-accordion-item-body')])[1]")
    FAG_2_ICON = ('XPATH', "(//span[contains(@class, 'icon icon-lib-mat-expand-more')])[2]")
    FAG_2_DETAILS = ('XPATH', "(//div[contains(@class, 'custom-accordion-item-body')])[2]")
    FAG_2_DETAILS_TEXT_IS = ('XPATH', "(//div[contains(@class, 'custom-accordion-item-body')])[2]")
    FAG_3_ICON = ('XPATH', "(//span[contains(@class, 'icon icon-lib-mat-expand-more')])[3]")
    FAG_3_DETAILS = ('XPATH', "(//div[contains(@class, 'custom-accordion-item-body')])[3]")
    FAG_3_DETAILS_TEXT_IS = ('XPATH', "(//div[contains(@class, 'custom-accordion-item-body')])[3]")
    FAG_4_ICON = ('XPATH', "(//span[contains(@class, 'icon icon-lib-mat-expand-more')])[4]")
    FAG_4_DETAILS = ('XPATH', "(//div[contains(@class, 'custom-accordion-item-body')])[4]")
    FAG_4_DETAILS_TEXT_IS = ('XPATH', "(//div[contains(@class, 'custom-accordion-item-body')])[4]")

    def click_menu_button(self):
        self.wait_until_visible(self.MENU_BUTTON, timeout=5)
        self.click(self.MENU_BUTTON)

    def click_covid19_flu_button(self):
        self.wait_until_visible(self.COVID19_FLU_BUTTON, timeout=5)
        self.click(self.COVID19_FLU_BUTTON)

    def click_covid19_flu_overview_button(self):
        self.wait_until_visible(self.COVID19_FLU_OVERVIEW_BUTTON, timeout=5)
        self.click(self.COVID19_FLU_OVERVIEW_BUTTON)

    def click_make_an_appointment_arrow_button(self):
        self.wait_until_visible(self.MAKE_AN_APPOINTMENT_ARROW_BUTTON, timeout=5)
        self.click(self.MAKE_AN_APPOINTMENT_ARROW_BUTTON)

    def click_book_appointment_button(self):
        self.wait_until_visible(self.BOOK_APPOINTMENT_BUTTON, timeout=5)
        self.click(self.BOOK_APPOINTMENT_BUTTON)

    def click_get_started_button(self):
        self.wait_until_visible(self.GET_STARTED_BUTTON, timeout=5)
        self.click(self.GET_STARTED_BUTTON)

    def click_fag_1_icon(self):
        self.wait_until_visible(self.FAG_1_ICON, timeout=5)
        self.click(self.FAG_1_ICON)

    def click_fag_2_icon(self):
        self.wait_until_visible(self.FAG_2_ICON, timeout=5)
        self.click(self.FAG_2_ICON)

    def click_fag_3_icon(self):
        self.wait_until_visible(self.FAG_3_ICON, timeout=5)
        self.click(self.FAG_3_ICON)

    def click_fag_4_icon(self):
        self.wait_until_visible(self.FAG_4_ICON, timeout=5)
        self.click(self.FAG_4_ICON)


