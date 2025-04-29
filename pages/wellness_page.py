from pages.base_page import BasePage

class WellnessPage(BasePage):

    CANCER_BUTTON = ('XPATH', "(//div[contains(@class, 'core-cards-body standard-block-content-spacing core-cards-body-stretch')])[1]")
    MAIN_MENU = ('XPATH', "//button[contains(@type, 'button')]")
    MAIN_MENU_BUTTON = ('XPATH', "//div[contains(@class, 'nav-hamburger')]")
    COVID19_GET_STARTED = ('XPATH', "//a[contains(@id, 'homepage-pfizer-blue-started-16')]")
    LEARN_MORE_ABOUT_SYMPTOMS = ('XPATH', "//a[contains(@id, 'homepage-pfizer-blue-symptoms-12')]")
    HEALTH_QUESTIONNAIRES_BUTTON = ('XPATH', "//a[contains(@id, 'homepage-pfizer-blue-questionnaires-0')]")
    NAVIGATE_MENOPAUSE_BUTTON = ('XPATH', "//a[contains(@id, 'homepage-pfizer-blue-menopause-2')]")

    def click_cancer_button(self):
        self.wait_until_visible(self.CANCER_BUTTON, timeout=1000)
        self.click(self.CANCER_BUTTON)

    def click_main_menu_button(self):
        self.wait_until_visible(self.MAIN_MENU_BUTTON, timeout=1000)
        self.click(self.MAIN_MENU_BUTTON)

    def click_health_questionnaries_button(self):
        self.wait_until_visible(self.HEALTH_QUESTIONNAIRES_BUTTON, timeout=1000)
        self.click(self.HEALTH_QUESTIONNAIRES_BUTTON)

    def click_navigate_menopause_button(self):
        self.wait_until_visible(self.NAVIGATE_MENOPAUSE_BUTTON, timeout=1000)
        self.click(self.NAVIGATE_MENOPAUSE_BUTTON)




