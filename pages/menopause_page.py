from pages.base_page import BasePage

class MenopausePage(BasePage):

    VASOMOR_SYMPTOMS_VMS = ('XPATH', "//h3[contains(@id, 'vasomotor-symptoms-vms')]")
    SLEEP_DISTURBANCES = ('XPATH', "//h3[contains(@id, 'sleep-disturbances')]")
    GENITOURINARY_SYNDROME_OF_MENOPAUSE = ('XPATH', "//h3[contains(@id, 'genitourinary-syndrome-of-menopause-gsm')]")
    MOOD_AND_COGNITIVE_DISTURBANCES = ('XPATH', "//h3[contains(@id, 'mood-and-cognitive-disturbances')]")
    KEEP_UP_WITH_VACCINATIONS = ('XPATH', "//h3[contains(@id, 'keep-up-with-vaccinations.')]")
    KEEP_UP_WITH_VACCINATIONS_BUTTON = ('XPATH', "//a[contains(@aria-label, 'Keep up with vaccinations, Get started')]")
    TALK_TO_A_DOCTOR = ('XPATH', "(//*[text()='Talk to a doctor'])[3]")
    TALK_TO_A_DOCTOR_BUTTON = ('XPATH', "(//span[contains(@class, 'icon icon-icon-external-link')])[3]")
    TALK_TO_A_DOCTOR_SECTION = ('XPATH', "(//a[contains(@class, 'button secondary')])[3]")

    def click_keep_up_with_vaccinations_button(self):
        self.wait_until_visible(self.KEEP_UP_WITH_VACCINATIONS_BUTTON, timeout=1000)
        self.click(self.KEEP_UP_WITH_VACCINATIONS_BUTTON)

    def click_talk_to_a_doctor_section(self):
        self.wait_until_visible(self.TALK_TO_A_DOCTOR_BUTTON, timeout=1000)
        self.click(self.TALK_TO_A_DOCTOR_SECTION)
