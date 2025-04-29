from pages.base_page import BasePage


class HomeFeaturePage(BasePage):

    ACCEPT_ALL = ('XPATH', "//button[contains(@id, 'onetrust-accept-btn-handler')]")
    PFIZER_FOR_ALL_LOGO = ('XPATH', "//span[contains(@class, 'icon icon-pfizer-for-all-home')]")
    MENU = ('XPATH', "(//button[contains(@class, 'primary')])[1]")
    # Scenario 1
    GET_HELP_WITH_TEXT_IS = ('XPATH', "//*[text()='Get Help With']")
    COVID19_FLU_TEXT_IS = ('XPATH', "//*[text()='COVID-19 & flu']")
    MIGRAINE_TEXT_IS = ('XPATH', "(//*[text()='Migraine'])[1]")
    VACCINES_TEXT_IS = ('XPATH', "(//*[text()='Vaccines'])[1]")
    MENOPAUSE_TEXT_IS = ('XPATH', "(//*[text()='Menopause'])[1]")
    HEALTH_QUESTIONNAIRES_TEXT_IS = ('XPATH', "(//*[text()='Health questionnaires'])[1]")
    SAVE_ON_PFIZER_MED_TEXT = ('XPATH', "(//*[text()='Save on Pfizer medications'])[1]")
    ADDITIONAL_RESOURCES_TEXT_IS = ('XPATH', "//h2[text()='Additional Resources']")
    SUPPORT_TEXT_IS = ('XPATH', "(//a[text()='Support'])[1]")
    CLOSE_BTN = ('XPATH', "//div[contains(@class, 'nav-hamburger')]")

    # Scenario :-2
    HOME = ('XPATH', "//li[contains(@class, 'active-item')][1]/a")
    NAVIGATE_MENOPAUSE_TEXT_IS = ('XPATH', "//a[text()='Navigate menopause']")
    NAVIGATE_MENOPAUSE = ('XPATH', "//a[contains(@id, 'homepage-pfizer-blue-menopause-2')]")
    MANAGE_MIGRAINE_TEXT_IS = ('XPATH', "//a[text()='Manage migraine']")
    MANAGE_MIGRAINE = ('XPATH', "//a[contains(@id, 'homepage-pfizer-blue-migraine-1')]")
    SCHEDULE_VACCINES_TEXT_IS = ('XPATH', "//a[text()='Schedule vaccines']")
    SCHEDULE_VACCINES = ('XPATH', "//a[contains(@id, 'homepage-pfizer-blue-vaccines-3')]")
    SAVE_ON_PFIZER_MED = ('XPATH', "//a[contains(@id, 'homepage-pfizer-blue-medications-4')]")
    SAVE_ON_PFIZER_MED_TEXT_IS = ('XPATH', "(//*[text()='Save on Pfizer medications'])[2]")
    TAKE_HEALTH_QUESTION_TEXT_IS = ('XPATH', "//*[text()='Take health questionnaires']")
    TAKE_HEALTH_QUESTION = ('XPATH', "//a[contains(@id, 'homepage-pfizer-blue-questionnaires-0')]")
    GET_ANSWERS_TO_HEALTH_AND_WELLNESS_QUESTIONS_TEXT_IS = ('XPATH', "//a[text()='Get answers to health and wellness questions']")

    # Scenario :- 3
    FLU_TITLE = ('XPATH', "//h2[contains(@id, 'covid19-flu-or-just-a-cold-lets-find-out')]")
    FLU_TITLE_TEXT_IS = ('XPATH',"//h2[text()='COVID‑19, flu, or just a cold? Let’s find out.']")
    FLU_TEXT_TEXT_IS = ('XPATH', "//p[text()='Take a step towards feeling better with quick access to doctors, tests, and treatments.']")
    FLU_GET_STARTED_BUTTON = ('XPATH', "//a[contains(@id, 'homepage-pfizer-blue-started-16')]")
    MIGRAINE_TITLE = ('XPATH', "//h2[contains(@id, 'a-newer-way-to-manage-migraine-is-here')]")
    MIGRAINE_TITLE_TEXT_IS = ('XPATH', "//h2[text()= 'A newer way to manage migraine is here.']")
    MIGRAINE_TEXT_TEXT_IS = ('XPATH', "//p[text()='Talk to a doctor about options that may be right for you.']")
    MIGRAINE_GET_STARTED_BUTTON = ('XPATH', "//a[contains(@id, 'homepage-pfizer-blue-started-17')]")

    #   Scenario :- 4
    PREVENTION_TITLE = ('XPATH', "//h2[contains(@ id, 'find-and-schedule-vaccines-you-and-your-family-may-be-eligible-for')]")
    PREVENTION_TITLE_TEXT_IS = ('XPATH', "//h2[contains(@ id, 'find-and-schedule-vaccines-you-and-your-family-may-be-eligible-for')]")
    PREVENTION_GET_STARTED = ('XPATH', "//a[contains(@ id, 'homepage-pfizer-blue-started-18')]")

    # Scenario :- 5
    HEADER = ('XPATH', "//h2[contains(@id, 'were-committed-to-helping-you-afford-your-pfizer-medications')]")
    HEADER_TEXT = ('XPATH', "//h2[contains(@id, 'were-committed-to-helping-you-afford-your-pfizer-medications')]")
    DESCRIBE = ('XPATH', "//p[text()='From co-pay cards to assistance with information on the prior authorization process, we’re here to help with your prescribed Pfizer medications. And if you’re eligible for our programs, we can also help you get access to your prescribed medications regardless of income.']")
    DESCRIBE_TEXT = ('XPATH', "//p[text()='From co-pay cards to assistance with information on the prior authorization process, we’re here to help with your prescribed Pfizer medications. And if you’re eligible for our programs, we can also help you get access to your prescribed medications regardless of income.']")
    GET_STARTED = ('XPATH', "//a[contains(@id, 'homepage-pfizer-blue-started-19')]")

    # Scenario :- 6
    BOTTOM_OF_THE_PAGE_DISCLAIMER = ('XPATH', "//p[text()='© 2025 Pfizer Inc. All rights reserved. PP-UNP-USA-6048']")
    DISCLAIMER_TEXT = ('XPATH', "//div[@class='section fragment-container custom-form-container']//div[@class= 'default-content-wrapper']")

    def click_menu(self):
        self.wait_until_visible(self.MENU, timeout=5)
        self.click(self.MENU)

    def click_home(self):
        self.wait_until_visible(self.HOME, timeout=1000)
        self.click(self.HOME)

    def click_navigate_menopause(self):
        self.wait_until_visible(self.NAVIGATE_MENOPAUSE, timeout=10)
        self.click(self.NAVIGATE_MENOPAUSE)

    def click_manage_migraine(self):
        self.wait_until_visible(self.MANAGE_MIGRAINE, timeout=10)
        self.click(self.MANAGE_MIGRAINE)

    def click_schedule_vaccines(self):
        self.wait_until_visible(self.SCHEDULE_VACCINES, timeout=10)
        self.click(self.SCHEDULE_VACCINES)

    def click_save_on_pfizer_med(self):
        self.wait_until_visible(self.SAVE_ON_PFIZER_MED, timeout=10)
        self.click(self.SAVE_ON_PFIZER_MED)

    def click_take_health_question(self):
        self.wait_until_visible(self.TAKE_HEALTH_QUESTION, timeout=10)
        self.click(self.TAKE_HEALTH_QUESTION)

    def click_ful_get_started_button(self):
        self.wait_until_visible(self.FLU_GET_STARTED_BUTTON, timeout=10)
        self.click(self.FLU_GET_STARTED_BUTTON)

    def click_migraine_get_started_button(self):
        self.wait_until_visible(self.MIGRAINE_GET_STARTED_BUTTON, timeout=10)
        self.click(self.MIGRAINE_GET_STARTED_BUTTON)

    def click_prevention_get_started(self):
        self.wait_until_visible(self.PREVENTION_GET_STARTED, timeout=10)
        self.click(self.PREVENTION_GET_STARTED)

    def click_get_started(self):
        self.wait_until_visible(self.GET_STARTED, timeout=10)
        self.click(self.GET_STARTED)
