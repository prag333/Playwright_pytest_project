from pages.base_page import BasePage

class HealthquestionnairesPage(BasePage):

    CANCER_BUTTON = ('XPATH', "(//a[contains(@class, 'button text button-icon')])[1]")
    HEART_HEALTH_BUTTON = ('XPATH', "(//span[contains(@class, 'icon icon-card-down-arrow')])[2]")
    MIGRAINE_BUTTON = ('XPATH', "(//a[contains(@class, 'button text button-icon')])[3]")
    VACCINS_BUTTON = ('XPATH', "(//span[contains(@class, 'icon icon-card-down-arrow')])[4]")
    FIRST_NAME = ('XPATH', "//input[contains(@id, 'first_name')]")
    ASK_A_QUESTION = ('XPATH', "//*[text()='Ask a question']")

    def click_cancer_button(self):
        self.wait_until_visible(self.CANCER_BUTTON, timeout=1000)
        self.click(self.CANCER_BUTTON)

    def click_heart_health_button(self):
        self.wait_until_visible(self.HEART_HEALTH_BUTTON, timeout=1000)
        self.click(self.HEART_HEALTH_BUTTON)

    def click_migraine_button(self):
        self.wait_until_visible(self.MIGRAINE_BUTTON, timeout=1000)
        self.click(self.MIGRAINE_BUTTON)

    def click_vaccins_button(self):
        self.wait_until_visible(self.VACCINS_BUTTON, timeout=1000)
        self.click(self.VACCINS_BUTTON)

    def click_first_name(self):
        self.wait_until_visible(self.FIRST_NAME, timeout=1000)
        self.click(self.FIRST_NAME)

    def click_ask_a_question(self):
        self.wait_until_visible(self.ASK_A_QUESTION, timeout=1000)
        self.click(self.ASK_A_QUESTION)
