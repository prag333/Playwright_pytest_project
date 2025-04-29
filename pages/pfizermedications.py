from pages.base_page import BasePage

class PfizermedicationsPage(BasePage):

    SUBMISSION = ('XPATH', "//h3[contains(@id, 'submission')]")
    REVIEW = ('XPATH', "//h3[contains(@id, 'review')]")
    DECISION = ('XPATH', "//h3[contains(@id, 'decision')]")
    PRESCRIPTION = ('XPATH', "//h3[contains(@id, 'prescription')]")
    PRIVATE_HEALTH_INSURANCE = ('XPATH', "(//div[contains(@class, 'summary custom-accordion-item-label')])[1]")
    PRIVATE_HEALTH_INSURANCE_SECTION = ('XPATH', "(//div[contains(@class, 'details custom-accordion-item')])[1]")
    PUBLIC_HEALTH_INSURANCE = ('XPATH', "(//div[contains(@class, 'summary custom-accordion-item-label')])[2]")
    PUBLIC_HEALTH_INSURANCE_SECTION = ('XPATH', "(//div[contains(@class, 'summary custom-accordion-item-label')])[2]")
    UNDERSTAND_INSURANCE_REQUIREMENTS = ('XPATH', "//h3[contains(@id, 'understand-insurance-requirements')]")
    UNDERSTAND_INSURANCE_REQUIREMENTS_BUTTON = ('XPATH', "//span[contains(@class, 'icon icon-document-icn')]")
    SAVINGS_AND_SUPPORT_FOR_ELIGIBLE_PATIENTS = ('XPATH', "//h3[contains(@id, 'savings-and-support-for-eligible-patients')]")
    SAVINGS_AND_SUPPORT_FOR_ELIGIBLE_PATIENTS_BUTTON = ('XPATH', "//span[contains(@class, 'icon icon-save-medication-nofillcolor')]")


    def click_private_health_insurance_section(self):
        self.wait_until_visible(self.PRIVATE_HEALTH_INSURANCE_SECTION, timeout=1000)
        self.click(self.PRIVATE_HEALTH_INSURANCE_SECTION)

    def click_public_health_insurance_section(self):
        self.wait_until_visible(self.PUBLIC_HEALTH_INSURANCE_SECTION, timeout=1000)
        self.click(self.PUBLIC_HEALTH_INSURANCE_SECTION)

    def click_understand_insurance_requirements_button(self):
        self.wait_until_visible(self.UNDERSTAND_INSURANCE_REQUIREMENTS_BUTTON, timeout=1000)
        self.click(self.UNDERSTAND_INSURANCE_REQUIREMENTS_BUTTON)

    def click_savings_and_support_for_eligible_patients_button(self):
        self.wait_until_visible(self.SAVINGS_AND_SUPPORT_FOR_ELIGIBLE_PATIENTS_BUTTON, timeout=1000)
        self.click(self.SAVINGS_AND_SUPPORT_FOR_ELIGIBLE_PATIENTS_BUTTON)
