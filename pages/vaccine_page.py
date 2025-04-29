from pages.base_page import BasePage


class VaccinePage(BasePage):

    FIND_AND_SCHEDULE_NOW = ('XPATH', "//*[text()='Find and schedule now']")
    FIND_AND_SCHEDULE_NOW_BUTTON = ('XPATH', "//span[contains(@class, 'icon icon-icon-external-link-white')]")
    CHECK_YOUR_VACCINE_ELIGIBILITY = ('XPATH', "//*[text()='Check your vaccine eligibility']")
    CHECK_YOUR_VACCINE_ELIGIBILITY_BUTTON = ('XPATH', "(//span[contains(@aria-label, 'Icon - icon-external-link')])[2]")
    COVID19 = ('XPATH', "//h3[contains(@id, 'covid19')]")
    FLU = ('XPATH', "//h3[contains(@id, 'flu')]")
    FIRST_NAME = ('XPATH', "//input[contains(@id, 'first_name')]")
    LAST_NAME = ('XPATH', "//input[contains(@id, 'last_name')]")
    EMAIL_ADDRESS = ('XPATH', "//input[contains(@type, 'email')]")

    def click_find_and_schedule_now_button(self):
        self.wait_until_visible(self.FIND_AND_SCHEDULE_NOW_BUTTON, timeout=1000)
        self.click(self.FIND_AND_SCHEDULE_NOW_BUTTON)

    def click_check_your_vaccine_eligibility_button(self):
        self.wait_until_visible(self.CHECK_YOUR_VACCINE_ELIGIBILITY_BUTTON, timeout=1000)
        self.click(self.CHECK_YOUR_VACCINE_ELIGIBILITY_BUTTON)

    def click_first_name(self):
        self.wait_until_visible(self.FIRST_NAME, timeout=1000)
        self.click(self.FIRST_NAME)

    def click_last_name(self):
        self.wait_until_visible(self.LAST_NAME, timeout=1000)
        self.click(self.LAST_NAME)

    def click_email_address(self):
        self.wait_until_visible(self.EMAIL_ADDRESS, timeout=1000)
        self.click(self.EMAIL_ADDRESS)
