from pages.base_page import BasePage


class Covid19OrderAtHomePage(BasePage):


    ACCEPT_ALL = ('XPATH', "//button[contains(@id, 'onetrust-accept-btn-handler')]")
    MENU_BUTTON = ('XPATH', "(//button[contains(@class, 'primary')])[1]")
    COVID19_FLU_TEXT_IS = ('XPATH', "//a[text()='COVID-19 & flu']")
    COVID19_FLU_BUTTON = ('XPATH', "//a[text()='COVID-19 & flu']")
    ORDER_AT_HOME_TESTS_IS = ('XPATH', "//a[text()='Order at-home tests']")
    ORDER_AT_HOME_TESTS_BUTTON = ('XPATH', "//a[text()='Order at-home tests']")
    TITLE_IS = ('XPATH', "//span[contains(@class, 'icon icon-pfizer-for-all-home')]")
    # Scenario:- 1
    HERO_TEXT = ('XPATH', "//h1[contains(@id, 'an-at-home-test-can-tell-you-if-you-have-covid-19-or-flu')]")
    HERO_TEXT_IS = ('XPATH', "//h1[text()='An at-home test can tell you if you have COVID-19 or flu.']")
    SUB_TEXT_IS = ('XPATH', "//p[text()='There are many tests that can detect if you have COVID-19 or flu. Order online and get a test delivered as early as today.']")
    SHOP_TESTS_ON_AMAZON = ('XPATH', "//a[contains(@id, 'respiratory-testing-Amazon-0')]")
    SHOP_TESTS_ON_INSTACART = ('XPATH', "//a[contains(@id, 'respiratory-testing-Instacart-1')]")
    INSTACART_ADDITIONAL_SUPPORT = ('XPATH', "//h3[contains(@id, 'additional-support-you-can-find-on-pfizerforall')]")
    INSTACART_ADDITIONAL_SUP_CARD_1_SYMBOL = ('XPATH', "//span[contains(@class, 'icon icon-headsets-talk-doctor-nofillcolor')]")
    INSTACART_ADDITIONAL_SUP_CARD_1_TITLE = ('XPATH', "(//h3[text()='Respiratory illness? Talk to a telehealth doctor.'])[2]")
    INSTACART_ADDITIONAL_SUP_CARD_1_PARA = ('XPATH', "//p[text()='Stay home and talk to a doctor online today.']")
    INSTACART_ADDITIONAL_SUP_CARD_1_ACTION = ('XPATH', "//a[contains(@aria-label, 'Respiratory illness? Talk to a telehealth doctor, Learn how')]")
    INSTACART_ADDITIONAL_SUP_CARD_2_SYMBOL = ('XPATH', "//span[contains(@class, 'icon icon-vaccination-nofillcolor')]")
    INSTACART_ADDITIONAL_SUP_CARD_2_TITLE = ('XPATH', "(//h3[text()='Keep up with vaccinations.'])[2]")
    INSTACART_ADDITIONAL_SUP_CARD_2_PARA = ('XPATH', "//p[text()='Help protect yourself from contagious viruses such as COVID-19 and RSV. Check eligibility and book an appointment.']")
    INSTACART_ADDITIONAL_SUP_CARD_2_ACTION = ('XPATH', "//a[contains(@aria-label, 'Keep up with vaccinations, See how')]")
    INSTACART_ADDITIONAL_SUP_CARD_3_SYMBOL = ('XPATH', "//span[contains(@class, 'icon icon-take-test-nofillcolor')]")
    INSTACART_ADDITIONAL_SUP_CARD_3_TITLE = ('XPATH', "(//h3[contains(@id, 'take-a-test-right-at-home.')])[2]")
    INSTACART_ADDITIONAL_SUP_CARD_3_PARA = ('XPATH', "(//p[text()='COVID-19 or flu? With some similar symptoms, it’s hard to know. At-home tests are available. Explore your options.'])[2]")
    INSTACART_ADDITIONAL_SUP_CARD_3_ACTION = ('XPATH', "//a[contains(@aria-label, 'Take a test, right at home, Explore your options')]")
    INSTACART_ADDITIONAL_SUP_CLOSE_BUTTON = ('XPATH', "//span[contains(@aria-label, 'Close')]")
    AMAZON_ADDITIONAL_SUPPORT = ('XPATH', "//h3[contains(@id, 'additional-support-you-can-find-on-pfizerforall')]")
    AMAZON_ADDITIONAL_SUP_CARD_1_SYMBOL = ("XPATH", "//span[contains(@class, 'icon icon-headsets-talk-doctor-nofillcolor')]")
    AMAZON_ADDITIONAL_SUP_CARD_1_TITLE = ("XPATH", "(//h3[contains(@id, 'respiratory-illness?-talk-to-a-telehealth-doctor.')])[2]")
    AMAZON_ADDITIONAL_SUP_CARD_1_PARA = ("XPATH", "//p[text()='Stay home and talk to a doctor online today.']")
    AMAZON_ADDITIONAL_SUP_CARD_1_ACTION = ("XPATH", "//a[contains(@aria-label, 'Respiratory illness? Talk to a telehealth doctor, Learn how')]")
    AMAZON_ADDITIONAL_SUP_CARD_2_SYMBOL = ('XPATH', "//span[contains(@class, 'icon icon-vaccination-nofillcolor')]")
    AMAZON_ADDITIONAL_SUP_CARD_2_TITLE = ('XPATH', "(//h3[contains(@id, 'keep-up-with-vaccinations.')])[2]")
    AMAZON_ADDITIONAL_SUP_CARD_2_PARA = ('XPATH', "//p[text()='Help protect yourself from contagious viruses such as COVID-19 and RSV. Check eligibility and book an appointment.']")
    AMAZON_ADDITIONAL_SUP_CARD_2_ACTION = ('XPATH', "//a[contains(@aria-label, 'Keep up with vaccinations, See how')]")
    AMAZON_ADDITIONAL_SUP_CARD_3_SYMBOL = ('XPATH', "//span[contains(@class, 'icon icon-take-test-nofillcolor')]")
    AMAZON_ADDITIONAL_SUP_CARD_3_TITLE = ('XPATH', "(//h3[contains(@id, 'take-a-test-right-at-home.')])[2]")
    AMAZON_ADDITIONAL_SUP_CARD_3_PARA = ('XPATH', "(//*[text()='COVID-19 or flu? With some similar symptoms, it’s hard to know. At-home tests are available. Explore your options.'])[2]")
    AMAZON_ADDITIONAL_SUP_CARD_3_ACTION = ('XPATH', "//a[contains(@aria-label, 'Take a test, right at home, Explore your options')]")
    AMAZON_ADDITIONAL_SUP_CLOSE_BUTTON = ('XPATH', "//span[contains(@aria-label, 'Close')]")
    # Scenario :- 2
    TEST_YOU_KNOW = ('XPATH', "//h2[contains(@id, 'test-so-you-know')]")
    TEST_YOU_KNOW_TEXT_IS = ('XPATH', "//h2[text()='Test so you know.']")
    TEST_YOU_KNOW_PARA_TEXT_IS = ('XPATH', "//p[text()='That way you can quickly put a plan in place, including talking to a healthcare provider or taking steps to prevent spread of either virus.']")
    FLU_TEXT_IS = ('XPATH', "//p[text()='Flu']")
    COVID19_TEXT_IS = ('XPATH', "//p[text()='COVID‑19']")
    FLU_DAYS_TEXT_IS = ('XPATH', "//h2[text()='2 Days']")
    COVID19_DAYS_TEXT_IS = ('XPATH', "//h2[text()='5 Days']")
    FLU_ANS_COVID_TEXT_IS = ('XPATH', "(//div[contains(., 'The critical period after you first experience')])[4]")
    # Scenario :- 3
    DISCLAIMER = ('XPATH', "//*[text()='© 2025 Pfizer Inc. All rights reserved. PP-UNP-USA-6048']")
    ORDER_A_TEST_NOW = ('XPATH', "//a[contains(@id, 'respiratory-testing-3')]")
    LEAVING_PFIZERFORALL_POPUP = ('XPATH', "//h3[contains(@id, 'you-are-leaving-pfizerforall')]")
    SHOP_TESTS_ON_AMAZON_IS = ('XPATH', "(//a[contains(@class, 'button primary long-cta')])[1]")
    SHOP_TESTS_ON_INSTACART_IS = ('XPATH', "(//a[contains(@class, 'button primary long-cta')])[2]")
    STAY_ON_THIS_SITE = ('XPATH', "//a[text()='Stay on this site']")
    SHOP_TEST_AMAZON_ADDITIONAL_SUPPORT = ('XPATH', "//h3[contains(@id, 'additional-support-you-can-find-on-pfizerforall')]")
    SHOP_TEST_AMAZON_ADDITIONAL_SUP_CARD_1_SYMBOL = ('XPATH', "//span[contains(@class, 'icon icon-headsets-talk-doctor-nofillcolor')]")
    SHOP_TEST_AMAZON_ADDITIONAL_SUP_CARD_1_TITLE = ('XPATH', "(//h3[contains(@id, 'respiratory-illness?-talk-to-a-telehealth-doctor.')])[2]")
    SHOP_TEST_AMAZON_ADDITIONAL_SUP_CARD_1_PARA = ('XPATH', "//p[text()='Stay home and talk to a doctor online today.']")
    SHOP_TEST_AMAZON_ADDITIONAL_SUP_CARD_1_ACTION = ('XPATH', "//a[contains(@aria-label, 'Respiratory illness? Talk to a telehealth doctor, Learn how')]")
    SHOP_TEST_AMAZON_ADDITIONAL_SUP_CARD_2_SYMBOL = ('XPATH', "//span[contains(@class, 'icon icon-vaccination-nofillcolor')]")
    SHOP_TEST_AMAZON_ADDITIONAL_SUP_CARD_2_TITLE = ('XPATH', "(//h3[contains(@id, 'keep-up-with-vaccinations.')])[2]")
    SHOP_TEST_AMAZON_ADDITIONAL_SUP_CARD_2_PARA = ('XPATH', "//p[text()='Help protect yourself from contagious viruses such as COVID-19 and RSV. Check eligibility and book an appointment.']")
    SHOP_TEST_AMAZON_ADDITIONAL_SUP_CARD_2_ACTION = ('XPATH', "//a[contains(@aria-label, 'Keep up with vaccinations, See how')]")
    SHOP_TEST_AMAZON_ADDITIONAL_SUP_CARD_3_SYMBOL = ('XPATH', "//span[contains(@class, 'icon icon-take-test-nofillcolor')]")
    SHOP_TEST_AMAZON_ADDITIONAL_SUP_CARD_3_TITLE = ('XPATH', "(//h3[contains(@id, 'take-a-test-right-at-home.')])[2]")
    SHOP_TEST_AMAZON_ADDITIONAL_SUP_CARD_3_PARA = ('XPATH', "(//p[text()='COVID-19 or flu? With some similar symptoms, it’s hard to know. At-home tests are available. Explore your options.'])[2]")
    SHOP_TEST_AMAZON_ADDITIONAL_SUP_CARD_3_ACTION = ('XPATH', "//a[contains(@aria-label, 'Take a test, right at home, Explore your options')]")
    SHOP_TEST_AMAZON_ADDITIONAL_SUP_CLOSE_BUTTON = ('XPATH', "//span[contains(@aria-label, 'Close')]")
    SHOP_TEST_INSTACART_ADDITIONAL_SUPPORT = ('XPATH', "//h3[contains(@id, 'additional-support-you-can-find-on-pfizerforall')]")
    SHOP_TEXT_INSTACART_ADDITIONAL_SUP_CARD_1_SYMBOL = ('XPATH', "//span[contains(@class, 'icon icon-headsets-talk-doctor-nofillcolor')]")
    SHOP_TEXT_INSTACART_ADDITIONAL_SUP_CARD_1_TITLE = ('XPATH', "(//h3[contains(@id, 'respiratory-illness?-talk-to-a-telehealth-doctor.')])[2]")
    SHOP_TEXT_INSTACART_ADDITIONAL_SUP_CARD_1_PARA = ('XPATH', "//p[text()='Stay home and talk to a doctor online today.']")
    SHOP_TEXT_INSTACART_ADDITIONAL_SUP_CARD_1_ACTION = ('XPATH', "//a[contains(@aria-label, 'Respiratory illness? Talk to a telehealth doctor, Learn how')]")
    SHOP_TEXT_INSTACART_ADDITIONAL_SUP_CARD_2_SYMBOL = ('XPATH', "//span[contains(@class, 'icon icon-vaccination-nofillcolor')]")
    SHOP_TEXT_INSTACART_ADDITIONAL_SUP_CARD_2_TITLE = ('XPATH', "(//h3[contains(@id, 'keep-up-with-vaccinations.')])[2]")
    SHOP_TEXT_INSTACART_ADDITIONAL_SUP_CARD_2_PARA = ('XPATH', "//p[text()='Help protect yourself from contagious viruses such as COVID-19 and RSV. Check eligibility and book an appointment.']")
    SHOP_TEXT_INSTACART_ADDITIONAL_SUP_CARD_2_ACTION = ('XPATH', "//a[contains(@aria-label, 'Keep up with vaccinations, See how')]")
    SHOP_TEXT_INSTACART_ADDITIONAL_SUP_CARD_3_SYMBOL = ('XPATH', "//span[contains(@class, 'icon icon-take-test-nofillcolor')]")
    SHOP_TEXT_INSTACART_ADDITIONAL_SUP_CARD_3_TITLE = ('XPATH', "(//h3[contains(@id, 'take-a-test-right-at-home.')])[2]")
    SHOP_TEXT_INSTACART_ADDITIONAL_SUP_CARD_3_PARA = ('XPATH', "(//p[text()='COVID-19 or flu? With some similar symptoms, it’s hard to know. At-home tests are available. Explore your options.'])[2]")
    SHOP_TEXT_INSTACART_ADDITIONAL_SUP_CARD_3_ACTION = ('XPATH', "//a[contains(@aria-label, 'Take a test, right at home, Explore your options')]")
    SHOP_TEST_INSTACART_ADDITIONAL_SUP_CLOSE_BUTTON = ('XPATH', "//span[contains(@aria-label, 'Close')]")
    # Scenario :- 4
    NOT_SURE_COVID = ('XPATH', "//h2[contains(@id, 'not-sure-if-a-covid19-or-flu-at-home-test-is-right-for-you-talk-to-a-doctor-about-your-symptoms')]")
    NOT_SURE_COVID_TEXT_IS = ('XPATH', "//h2[contains(@id, 'not-sure-if-a-covid19-or-flu-at-home-test-is-right-for-you-talk-to-a-doctor-about-your-symptoms')]")
    NOT_SURE_CARD_1_TEXT_IS = ('XPATH', "//h3[contains(@id, 'talk-to-a-doctor-quicklyfrom-anywhere')]")
    NOT_SURE_CARD_2_TEXT_IS = ('XPATH', "//h3[contains(@id, 'make-an-appointment-to-see-a-doctor-near-you-on-your-schedule')]")
    NOT_SURE_CARD_1_ARROW = ('XPATH', "//a[contains(@id, 'respiratory-testing--0')]")
    NOT_SURE_CARD_2_ARROW = ('XPATH', "(//a[contains(@id, 'respiratory-testing--1')])[1]")
    # Scenario :- 5
    QUESTION_1 = ('XPATH', "(//div[contains(@class, 'summary custom-accordion-item-label')])[1]")
    QUESTION_1_TEXT_IS = ('XPATH', "//*[text()='Where can I get a test for COVID‑19 or flu?']")
    QUESTION_2_TEXT_IS = ('XPATH', "//*[text()='How accurate are at-home COVID‑19 tests?']")
    QUESTION_3_TEXT_IS = ('XPATH', "//*[text()='Why should I get tested for COVID‑19 or flu?']")
    QUESTION_4_TEXT_IS = ('XPATH', "//*[text()='Are there any tests for RSV?']")
    QUESTION_1_SPAN = ('XPATH', "(//span[contains(@class, 'icon icon-lib-mat-expand-more')])[1]")
    QUESTION_2_SPAN = ('XPATH', "(//span[contains(@class, 'icon icon-lib-mat-expand-more')])[2]")
    QUESTION_3_SPAN = ('XPATH', "(//span[contains(@class, 'icon icon-lib-mat-expand-more')])[3]")
    QUESTION_4_SPAN = ('XPATH', "(//span[contains(@class, 'icon icon-lib-mat-expand-more')])[4]")
    ANSWER_1_TEXT_IS = ('XPATH', "(//div[contains(@class, 'custom-accordion-item-body')])[1]")
    ANSWER_2_TEXT_IS = ('XPATH', "(//div[contains(@class, 'custom-accordion-item-body')])[2]")
    ANSWER_3_TEXT_IS = ('XPATH', "(//div[contains(@class, 'custom-accordion-item-body')])[3]")
    ANSWER_4_TEXT_IS = ('XPATH', "(//div[contains(@class, 'custom-accordion-item-body')])[4]")
    # Scenario :- 5
    BOTTOM_OF_THE_PAGE = ('XPATH', "//*[text()='© 2025 Pfizer Inc. All rights reserved. PP-UNP-USA-6048']")
    DISCLAIMER_TEXT_IS = ('XPATH', "//div[@class='section fragment-container custom-form-container']//div[@class= 'default-content-wrapper']")


    def click_menu_button(self):
        self.wait_until_visible(self.MENU_BUTTON, timeout=5)
        self.click(self.MENU_BUTTON)

    def click_covid19_flu_button(self):
        self.wait_until_visible(self.COVID19_FLU_BUTTON, timeout=5)
        self.click(self.COVID19_FLU_BUTTON)

    def click_order_at_home_tests_button(self):
        self.wait_until_visible(self.ORDER_AT_HOME_TESTS_BUTTON, timeout=5)
        self.click(self.ORDER_AT_HOME_TESTS_BUTTON)

    def click_shop_tests_on_instacart(self):
        self.wait_until_visible(self.SHOP_TESTS_ON_INSTACART, timeout=5)
        self.click(self.SHOP_TESTS_ON_INSTACART)

    def click_instacart_additional_sup_close_button(self):
        self.wait_until_visible(self.INSTACART_ADDITIONAL_SUP_CLOSE_BUTTON, timeout=5)
        self.click(self.INSTACART_ADDITIONAL_SUP_CLOSE_BUTTON)

    def click_shop_tests_on_amazon(self):
        self.wait_until_visible(self.SHOP_TESTS_ON_AMAZON, timeout=5)
        self.click(self.SHOP_TESTS_ON_AMAZON)

    def click_amazon_additional_sup_close_button(self):
        self.wait_until_visible(self.AMAZON_ADDITIONAL_SUP_CLOSE_BUTTON, timeout=5)
        self.click(self.AMAZON_ADDITIONAL_SUP_CLOSE_BUTTON)

    def click_order_a_test_now(self):
        self.wait_until_visible(self.ORDER_A_TEST_NOW, timeout=5)
        self.click(self.ORDER_A_TEST_NOW)

    def click_stay_on_this_site(self):
        self.wait_until_visible(self.STAY_ON_THIS_SITE, timeout=5)
        self.click(self.STAY_ON_THIS_SITE)

    def click_shop_tests_on_amazon_is(self):
        self.wait_until_visible(self.SHOP_TESTS_ON_AMAZON_IS, timeout=5)
        self.click(self.SHOP_TESTS_ON_AMAZON_IS)

    def click_shop_test_amazon_additional_sup_close_button(self):
        self.wait_until_visible(self.SHOP_TEST_AMAZON_ADDITIONAL_SUP_CLOSE_BUTTON, timeout=5)
        self.click(self.SHOP_TEST_AMAZON_ADDITIONAL_SUP_CLOSE_BUTTON)

    def click_shop_tests_on_instacart_is(self):
        self.wait_until_visible(self.SHOP_TESTS_ON_INSTACART_IS, timeout=5)
        self.click(self.SHOP_TESTS_ON_INSTACART_IS)

    def click_shop_test_instacart_additional_sup_close_button(self):
        self.wait_until_visible(self.SHOP_TEST_INSTACART_ADDITIONAL_SUP_CLOSE_BUTTON, timeout=5)
        self.click(self.SHOP_TEST_INSTACART_ADDITIONAL_SUP_CLOSE_BUTTON)

    def click_not_sure_card_1_arrow(self):
        self.wait_until_visible(self.NOT_SURE_CARD_1_ARROW, timeout=5)
        self.click(self.NOT_SURE_CARD_1_ARROW)

    def click_not_sure_card_2_arrow(self):
        self.wait_until_visible(self.NOT_SURE_CARD_2_ARROW, timeout=5)
        self.click(self.NOT_SURE_CARD_2_ARROW)

    def click_question_1_span(self):
        self.wait_until_visible(self.QUESTION_1_SPAN, timeout=5)
        self.click(self.QUESTION_1_SPAN)

    def click_question_2_span(self):
        self.wait_until_visible(self.QUESTION_2_SPAN, timeout=5)
        self.click(self.QUESTION_2_SPAN)

    def click_question_3_span(self):
        self.wait_until_visible(self.QUESTION_3_SPAN, timeout=5)
        self.click(self.QUESTION_3_SPAN)

    def click_question_4_span(self):
        self.wait_until_visible(self.QUESTION_4_SPAN, timeout=5)
        self.click(self.QUESTION_4_SPAN)


