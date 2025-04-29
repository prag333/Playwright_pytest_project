from pages.base_page import BasePage


class HomePage(BasePage):
    # Define locators as tuples (locator_type, locator_value)
    ACCEPT_COKKIES = ('XPATH', "//button[contains(@id, 'onetrust-accept-btn-handler')]")
    TAKE_HEALTH_QUESTIONNAIRES = ('XPATH', "//span[contains(@class, 'icon icon-prior-authorization-form')]")
    TAKE_HEALTH_QUESTIONNAIRES_SECTION = ('XPATH', "//a[contains(text(), 'Take health questionnaires')]")
    TAKE_HEALTH_QUESTIONNAIRES_BUTTON = ('XPATH', "//p[contains(text(), 'Take health')]/following-sibling::p[2]/span")
    MANAGE_MIGRAINE = ('XPATH', "//span[contains(@class, 'icon icon-migraine-white')]")
    MANAGE_MIGRAINE_SECTION = ('XPATH', "//a[contains(text(), 'Manage migraine')]")
    MANAGE_MIGRAINE_BUTTON = ('XPATH', "//p[contains(text(), 'Manage')]/following-sibling::p[2]/span")
    NAVIGATE_MENOPAUSE = ('XPATH', "//p[contains(@class, 'button-container button-container-multi')]")
    NAVIGATE_MENOPAUSE_SECTION = ('XPATH', "//a[contains(text(), 'Navigate menopause')]")
    NAVIGATE_MENOPAUSE_BUTTON = ('XPATH', "//p/span[contains(text(), 'Navigate')]/../following-sibling::p[2]/span")
    SCHEDULE_VACCINES = ('XPATH', "//span[contains(@class, 'icon icon-bandage')]")
    SCHEDULE_VACCINES_SECTION = ('XPATH', "//a[contains(text(), 'Schedule vaccines')]")
    SCHEDULE_VACCINES_BUTTON = ('XPATH', "//p[contains(text(), 'Schedule')]/following-sibling::p[2]/span")
    SAVE_ON_PFIZER_MEDICATIONS = ('XPATH', "//span[contains(@class, 'icon icon-prescription-medication-bottle-white')]")
    SAVE_ON_PFIZER_MEDICATIONS_SECTION = ('XPATH', "//div/a[contains(text(), 'Save on Pfizer medications')]")
    SAVE_ON_PFIZER_MEDICATIONS_BUTTON = ('XPATH', "//p[contains(text(), 'Save on')]/following-sibling::p[2]/span")
    GET_ANSWERS_TO_HEALTH_AND_WELLNESS_QUESTIONS = ('XPATH', "//span[contains(@class, 'icon icon-icon-health-and-wellness')]")
    HEALTH_AND_WELLNESS_MEDICATIONS_SECTION = ('XPATH', "//a[contains(text(), 'Get answers to health and wellness questions')]")
    GET_ANSWERS_TO_HEALTH_AND_WELLNESS_QUESTIONS_BUTTON = ('XPATH', "//p[contains(text(), 'Get answers to')]/following-sibling::p[2]/span")
    COVID19_GET_STARTED_BUTTON = ('XPATH', "//a[contains(@id, 'homepage-pfizer-blue-started-16')]")


    def go_to_homepage(self, url: str):
        self.page.goto(url)

    def go_back_to_previous_page(self):
        """Navigates to the previous page in the browser history."""
        self.go_back()

    def click_accept_cookies(self):
        """Accept the cookies."""
        self.wait_until_visible(self.ACCEPT_COKKIES, timeout=25000)
        self.click(self.ACCEPT_COKKIES)

    def click_questionaries_section(self):
        """Click questionaries section."""
        self.wait_until_visible(self.TAKE_HEALTH_QUESTIONNAIRES_BUTTON, timeout=5000)
        self.click(self.TAKE_HEALTH_QUESTIONNAIRES_SECTION)

    def click_migraine_section(self):
        """Click migraine section."""
        self.wait_until_visible(self.MANAGE_MIGRAINE_SECTION, timeout=5000)
        self.click(self.MANAGE_MIGRAINE_SECTION)

    def click_menopause_section(self):
        """Click menopause section."""
        self.wait_until_visible(self.NAVIGATE_MENOPAUSE_BUTTON, timeout=5000)
        self.click(self.NAVIGATE_MENOPAUSE_SECTION)

    def click_vaccine_options_section(self):
        """Click vaccine section."""
        self.wait_until_visible(self.SCHEDULE_VACCINES_BUTTON, timeout=5000)
        self.click(self.SCHEDULE_VACCINES_SECTION)

    def click_prescription_assistance_section(self):
        """Click prescription assistance section."""
        self.wait_until_visible(self.SAVE_ON_PFIZER_MEDICATIONS_BUTTON, timeout=5000)
        self.click(self.SAVE_ON_PFIZER_MEDICATIONS_SECTION)

    def click_health_wellness_section(self):
        """Click health wellness section."""
        self.wait_until_visible(self.GET_ANSWERS_TO_HEALTH_AND_WELLNESS_QUESTIONS_BUTTON, timeout=5000)
        self.click(self.HEALTH_AND_WELLNESS_MEDICATIONS_SECTION)

    def click_covid19_get_started(self):
        """Click covid19 get started section."""
        self.wait_until_visible(self.COVID19_GET_STARTED_BUTTON, timeout=300)
        self.click(self.COVID19_GET_STARTED_BUTTON)
