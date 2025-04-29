from pages.base_page import BasePage


class Covid19TalkDoctorPage(BasePage):
    ACCEPT_ALL = ('XPATH', "//button[contains(@id, 'onetrust-accept-btn-handler')]")
    MENU_BUTTON = ('XPATH', "(//button[contains(@class, 'primary')])[1]")
    COVID19_FLU_TEXT_IS = ('XPATH', "//a[text()='COVID-19 & flu']")
    COVID19_FLU_BUTTON = ('XPATH', "//a[text()='COVID-19 & flu']")
    TALK_TO_DOCTOR_NOW_TEXT_IS = ('XPATH', "(//a[text()='Talk to a doctor now'])[2]")
    TALK_TO_DOCTOR_NOW_BUTTON = ('XPATH', "(//a[text()='Talk to a doctor now'])[2]")

    # Scenario 1 :-
    TITLE = ('XPATH', "//h1[contains(@id, 'see-a-doctor-right-away-with-telehealth')]")
    TITLE_TEXT_IS = ('XPATH', "//h1[text()='See a doctor right away with telehealth.']")
    SUBTEXT_TEXT_IS = ('XPATH', "//p[text()='If you’re feeling sick, you can connect to care right from home. "
                                "We partner with UpScript, an independent telehealth provider. They can find you a "
                                "doctor who will listen, evaluate your symptoms, and help make a plan. Treatments for "
                                "COVID-19 and flu must be taken within the first few days of symptoms.']")
    SCHEDULE_UPSCRIPT_BUTTON_TEXT_IS = ('XPATH', "//a[contains(@id, 'respiratory-telehealth-2')]")
    SCHEDULE_UPSCRIPT_BUTTON = ('XPATH', "//a[contains(@id, 'respiratory-telehealth-2')]")
    # Scenario 2
    POP_UP = ('XPATH', "//div[contains(@class, 'overlay-text')]")
    EYEBROW_TEXT_IS = ('XPATH', "(//h2[contains(@id, 'youre-a-click-away-from-finding-a-doctor-through-upscriptcare')])[2]")
    CONTINUE_BUTTON_TEXT_IS = ('XPATH', "//*[text()='See a doctor at UpScriptCare']")
    DISCLAIMER_TEXT_IS = ('XPATH', "//*[text()='See full terms and conditions at UpScriptCare.com. By clicking the link above, you will be redirected to a third-party website that is neither owned nor controlled by Pfizer. Pfizer is not responsible for the content or services of this third-party website.']")
    CANCEL_BUTTON = ('XPATH', "//span[contains(@ aria-label, 'Close')]")
    # Scenario 3
    CONTINUE_UPSCRIPT_BUTTON = ('XPATH', "//*[text()='See a doctor at UpScriptCare']")
    POP_UP_TITLE = ('XPATH', "//h3[contains(@id, 'additional-support-you-can-find-on-pfizerforall')]")
    POP_UP_TITLE_TEXT_IS = ('XPATH', "//h3[text()='Additional support you can find on PfizerForAll™']")
    # Scenario 4
    TALK_TO_A_DOCTOR = ('XPATH', "//h3[contains(@id, 'migraine?-talk-to-a-telehealth-doctor.')]")
    TALK_TO_A_DOCTOR_TEXT = ('XPATH', "//h1[text()='See a doctor right away with telehealth.']")
    TALK_TO_A_DOCTOR_DESCRIPTION = ('XPATH', "//p[text()='If you’re feeling sick, you can connect to care right from home. We partner with UpScript, an independent telehealth provider. They can find you a doctor who will listen, evaluate your symptoms, and help make a plan. Treatments for COVID-19 and flu must be taken within the first few days of symptoms.']")
    TALK_TO_A_DOCTOR_DESCRIPTION_TEXT = ('XPATH', "//p[text()='If you’re feeling sick, you can connect to care right from home. We partner with UpScript, an independent telehealth provider. They can find you a doctor who will listen, evaluate your symptoms, and help make a plan. Treatments for COVID-19 and flu must be taken within the first few days of symptoms.']")
    # Scenario 5
    HEADING = ('XPATH', "//h2[contains(@id, 'convenience-convenience-convenience')]")
    HEADING_TEXT_IS = ('XPATH', "//h2[text()='Convenience, convenience, convenience.']")
    TEXT_TEXT_IS = ('XPATH', "//p[text()='Get answers fast when you’re not feeling well.']")
    BULLET_1_TEXT_IS = ('XPATH', "//li[text()='All visits are virtual.']")
    BULLET_2_TEXT_IS = ('XPATH', "//li[text()='UpScriptCare providers are available 6AM – 12AM EST. Every day.']")
    BULLET_3_TEXT_IS = ('XPATH', "//li[text()='Medications can be delivered right to your door or you can pick them up at your pharmacy.']")
    BULLET_4_TEXT_IS = ('XPATH', "//li[text()='You can use your HSA or FSA accounts to help cover the cost of your visit.']")
    # Scenario 6
    UPSCRIPT_HEADING = ('XPATH', "//h2[contains(@id, 'upscriptcare-is-quick-and-simple')]")
    STEP_1_TAG_TEXT_IS = ('XPATH', "//p[text()='Step 1']")
    STEP_1_HEADING_TEXT_IS = ('XPATH', "//h3[contains(@id, 'get-registered')]")
    STEP_1_TEXT_IS = ('XPATH', "//*[text()='Create an UpScriptCare account.']")
    STEP_2_TAG_TEXT_IS = ('XPATH', "//*[text()='Step 2']")
    STEP_2_HEADING_TEXT_IS = ('XPATH', "//*[text()='Answer a 5-minute questionnaire']")
    STEP_2_TEXT_IS = ('XPATH', "//*[text()='There are a few medical questions that will help move things along.']")
    STEP_3_TAG_TEXT_IS = ('XPATH', "//*[text()='Step 3']")
    STEP_3_HEADING_TEXT_IS = ('XPATH', "//*[text()='Checkout']")
    STEP_3_TEXT_IS = ('XPATH', "//*[text()='Provide address and payment details.']")
    STEP_4_TAG_TEXT_IS = ('XPATH', "//*[text()='Step 4']")
    STEP_4_HEADING_TEXT_IS = ('XPATH', "//*[text()='Talk with a doctor']")
    STEP_4_TEXT_IS = ('XPATH', "//*[text()='Get your questions answered, and discuss treatment options that may be right for you. (Consultation type is dependent on your state regulations.)']")
    # Scenario 7
    SAVE_PRESCRIBED_MEDICATIONS_SECTION = ('XPATH', "//h2[contains(@id, 'save-on-your-prescribed-pfizer-medications-and-get-support-when-you-need-it')]")
    SAVE_PRESCRIBED_MEDICATIONS_SECTION_TITLE_TEXT_IS = ('XPATH', "//h2[contains(@id, 'save-on-your-prescribed-pfizer-medications-and-get-support-when-you-need-it')]")
    SAVE_PRESCRIBED_MEDICATIONS_SECTION_SUBTEXT_IS = ('XPATH', "//*[text()='From co-pay savings cards to financial assistance programs, we have options that can help. Our dedicated customer support team can also help you navigate your insurance benefits, understand your options, and more.']")
    GET_STARTED_BUTTON_TEXT_IS = ('XPATH', "//a[contains(@aria-label, 'Get started')]//*[text()='Get started']")
    GET_STARTED_BUTTON = ('XPATH', "//a[contains(@id, 'respiratory-telehealth-started-0')]")
    # Scenario :- 8
    BOTTOM_OF_DISCLAIMER = ('XPATH', "//p[text()='© 2025 Pfizer Inc. All rights reserved. PP-UNP-USA-6048']")
    BOTTOM_OF_DISCLAIMER_TEXT_IS = ('XPATH', "//div[@class='section fragment-container custom-form-container']//div[@class= 'default-content-wrapper']")
    # Scenario :- 9
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

    def click_talk_to_a_doctor_button(self):
        self.wait_until_visible(self.TALK_TO_DOCTOR_NOW_BUTTON, timeout=5)
        self.click(self.TALK_TO_DOCTOR_NOW_BUTTON)

    def click_schedule_upscript_button(self):
        self.wait_until_visible(self.SCHEDULE_UPSCRIPT_BUTTON, timeout=5)
        self.click(self.SCHEDULE_UPSCRIPT_BUTTON)

    def click_cancel_button(self):
        self.wait_until_visible(self.CANCEL_BUTTON, timeout=5)
        self.click(self.CANCEL_BUTTON)

    def click_continue_upscript_button(self):
        self.wait_until_visible(self.CONTINUE_UPSCRIPT_BUTTON, timeout=5)
        self.click(self.CONTINUE_UPSCRIPT_BUTTON)

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