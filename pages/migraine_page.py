from pages import home_page
from pages.base_page import BasePage

class MigrainePage(BasePage):

    LEARN_ABOUT_TODAY_MIGRAINE_SCEIENCE = ('XPATH', "//*[text()='Learn about today’s migraine science']")
    EXPLORE_MIGRAINE_TREATMENT_OPTIONS = ('XPATH', "//*[text()='Explore migraine treatment options']")
    TALK_TO_A_MIGRAINE_DOCTOR = ('XPATH', "//*[text()='Talk to a migraine doctor']")
    FIRST_NAME = ('XPATH', "//input[contains(@id, 'first_name')]")
    FREQUENTLY_ASKED_YOUR_QUESTIONS = ('XPATH', "//h2[contains(@id, 'frequently-asked-questions')]")
    TAKE_THE_QUIZ_SECTION = ('XPATH', "//a[contains(@id, 'migraine-non-homepage-2')]")

    def click_take_the_quiz_section(self):
        self.wait_until_visible(self.TAKE_THE_QUIZ_SECTION, timeout=1000)
        self.click(self.TAKE_THE_QUIZ_SECTION)