from pages.base_page import BasePage

class Covid19Page(BasePage):

    PNEUMONIA = ('XPATH', "//h3[contains(@id, 'pneumonia')]")
    FLU = ('XPATH', "//h3[contains(@id, 'flu')]")
    RSV = ('XPATH', "//h3[contains(@id, 'rsv')]")
    TALK_TO_A_DOCTOR_BUTTON = ('XPATH', "//a[contains(@id, 'respiratory-non-homepage--2')]")
    FREQUENTLY_ASKED_QUETIONS_1ST_QUESTION = ('XPATH', "(//span[contains(@class, 'icon icon-lib-mat-expand-more')])[1]")
    FREQUENTLY_ASKED_QUETIONS_2ND_QUESTION = ('XPATH', "(//span[contains(@class, 'icon icon-lib-mat-expand-more')])[2]")
    KEEP_UP_WITH_VACCINATIONS_CARD = ('XPATH', "//h3[contains(@id, 'keep-up-with-vaccinations.')]")
    GO_T0_THE_GUIDE_BUTTON = ('XPATH', "//a[contains(@id, 'respiratory-non-homepage-guide-1')]")
    MAKE_AN_APPOINTMENT_BUTTON = ('XPATH', "//a[contains(@id, 'respiratory-non-homepage--3')]")

    def click_talk_to_a_doctor_button(self):
        self.wait_until_visible(self.TALK_TO_A_DOCTOR_BUTTON, timeout=2000)
        self.click(self.TALK_TO_A_DOCTOR_BUTTON)

    def click_frequently_asked_quetions_1st_question(self):
        self.wait_until_visible(self.FREQUENTLY_ASKED_QUETIONS_1ST_QUESTION, timeout=2000)
        self.click(self.FREQUENTLY_ASKED_QUETIONS_1ST_QUESTION)

    def click_frequently_asked_quetions_2nd_question(self):
        self.wait_until_visible(self.FREQUENTLY_ASKED_QUETIONS_2ND_QUESTION, timeout=2000)
        self.click(self.FREQUENTLY_ASKED_QUETIONS_2ND_QUESTION)

    def click_keep_up_with_vaccinations_card(self):
        self.wait_until_visible(self.KEEP_UP_WITH_VACCINATIONS_CARD, timeout=2000)
        self.click(self.KEEP_UP_WITH_VACCINATIONS_CARD)

    def click_go_to_the_guide_button(self):
        self.wait_until_visible(self.GO_T0_THE_GUIDE_BUTTON, timeout=2000)
        self.click(self.GO_T0_THE_GUIDE_BUTTON)

    def click_make_an_appointment_button(self):
        self.wait_until_visible(self.MAKE_AN_APPOINTMENT_BUTTON, timeout=2000)
        self.click(self.MAKE_AN_APPOINTMENT_BUTTON)
