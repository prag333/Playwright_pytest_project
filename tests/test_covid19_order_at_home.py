import pytest
from pages.covid19_order_at_home_page import Covid19OrderAtHomePage
from pages.home_page import HomePage
from tests.conftest import driver
import logging

logger = logging.getLogger(__name__)

class TestCovid19OrderAtHomePage:

    @pytest.fixture(autouse=True)
    def setup(self, driver, BASE_URL):
        self.base_url = BASE_URL
        self.covid19_orderat_page = Covid19OrderAtHomePage(driver)
        self.home_page = HomePage(driver)
        logger.info("Common steps for Covid19TalkDoctorPage")
        self.home_page.go_to_homepage(self.base_url)
        assert "Pfizer" in driver.title()
        logger.info("Verify the accept all displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.ACCEPT_ALL, timeout=30)
        logger.info("Click the accept cookies")
        self.home_page.click_accept_cookies()
        logger.info("Scroll to the menu button")
        self.covid19_orderat_page.scroll_to_element(self.covid19_orderat_page.MENU_BUTTON)
        logger.info("Click the Menu button")
        self.covid19_orderat_page.click_menu_button()
        logger.info(f"Checking the covid19 flu text is: {self.covid19_orderat_page.get_text(self.covid19_orderat_page.COVID19_FLU_TEXT_IS)}")
        assert "COVID-19 & flu" in self.covid19_orderat_page.get_text(self.covid19_orderat_page.COVID19_FLU_TEXT_IS), "COVID-19 & flu text is not displayed"
        logger.info("Click the covid19 flu button")
        self.covid19_orderat_page.click_covid19_flu_button()
        logger.info(f"Checking the Order at home tests text is: {self.covid19_orderat_page.get_text(self.covid19_orderat_page.ORDER_AT_HOME_TESTS_IS)}")
        assert "Order at-home tests" in self.covid19_orderat_page.get_text(self.covid19_orderat_page.ORDER_AT_HOME_TESTS_IS), "Order at-home tests is"
        logger.info("Click the Order at home tests button")
        self.covid19_orderat_page.click_order_at_home_tests_button()
        assert f"{self.base_url}/respiratory/testing" in self.covid19_orderat_page.get_url()
        assert "Respiratory Testing | PfizerForAll™" in self.covid19_orderat_page.get_title()

        # Scenario: 1 Verify navigation to Instacart and Amazon from Hero section of COVID-19 Order at-home page

    def test_verify_navigation_to_Instacart_and_amazon_from_hero_section_covid19_order_at_home_page(self):
        logger.info("Test verify the Navigation to Instacart and Amazon from Hero section of COVID-19 Order at-home page")
        logger.info("Verifying Hero text is displayed")
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.HERO_TEXT), "Hero text is not displayed"
        logger.info(f"Checking the Hero text is: {self.covid19_orderat_page.get_text(self.covid19_orderat_page.HERO_TEXT_IS)}")
        assert "An at-home test can tell you if you have COVID-19 or flu." in self.covid19_orderat_page.get_text(self.covid19_orderat_page.HERO_TEXT_IS), "Hero text is not displayed"
        logger.info(f"Checking the Sub text is: {self.covid19_orderat_page.get_text(self.covid19_orderat_page.SUB_TEXT_IS)}")
        assert "There are many tests that can detect if you have COVID-19 or flu. Order online and get a test delivered as early as today." in self.covid19_orderat_page.get_text(self.covid19_orderat_page.SUB_TEXT_IS), "Sub text is not displayed"
        logger.info("Verifying the Shop tests on Amazon is displayed")
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TESTS_ON_AMAZON), "Shop tests on Amazon is not displayed"
        logger.info("Verifying the Shop tests on Instacart is displayed")
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TESTS_ON_INSTACART), "Shop tests on Instacart is not displayed"
        logger.info("Clik the Shop tests on instacart")
        self.covid19_orderat_page.click_shop_tests_on_instacart()
        self.covid19_orderat_page.wait_for_timeout(5)
        opened_tabs = self.covid19_orderat_page.get_open_tab_count()
        assert opened_tabs == 2, "There are no 2 opened tabs"
        assert "https://www.instacart.com/store/brands/pfizer-for-all" in self.covid19_orderat_page.get_url_from_new_tab(self.covid19_orderat_page)
        self.covid19_orderat_page.is_window_focused()
        logger.info("Verifying the the close current tab")
        self.covid19_orderat_page.close_current_tab(self.covid19_orderat_page)
        logger.info("Clik the Shop tests on instacart")
        self.covid19_orderat_page.click_shop_tests_on_instacart()
        self.covid19_orderat_page.is_window_focused()
        self.covid19_orderat_page.wait_for_timeout(2)
        self.covid19_orderat_page.close_current_tab(self.covid19_orderat_page)
        logger.info("Verifying the additional Support is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUPPORT), "Additional Support is not displayed"
        logger.info("Verifying the Additional support card 1 symbol is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CARD_1_SYMBOL), "Additional support card 1 symbol is not displayed"
        logger.info("Verifying the Additional support card 1 title is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CARD_1_TITLE), "Additional support card 1 title is not displayed"
        logger.info("Additional support card 1 paragraph is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CARD_1_PARA), "Additional support card 1 paragraph is not displayed"
        logger.info("Verifying the Additional support card 1 action is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CARD_1_ACTION), "Additional support card 1 action is not displayed"
        logger.info("Verifying the Additional support card 2 symbol is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CARD_2_SYMBOL), "Additional support card 2 symbol is not displayed"
        logger.info("Verifying the Additional support card 2 title is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CARD_2_TITLE), "Additional support card 2 title is not displayed"
        logger.info("Verifying the Additional support card 2 paragraph is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CARD_2_PARA), "Additional support card 2 paragraph is not displayed"
        logger.info("Additional support card 2 action is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CARD_2_ACTION), "Additional support card 2 action is not displayed"
        logger.info("Verifying the Additional support card 3 symbol is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CARD_3_SYMBOL), "Additional support card 3 symbol is not displayed"
        logger.info("Verifying the Additional support card 3 title is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CARD_3_TITLE), "Additional support card 3 title is not displayed"
        logger.info("Verifying the Additional support card 3 paragraph is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CARD_3_PARA), "Additional support card 3 paragraph is not displayed"
        logger.info("Verifying the Additional support card 3 paragraph is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CARD_3_ACTION), "Additional support card 3 action is not displayed"
        logger.info("Verifying the Additional support close button is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CLOSE_BUTTON), "Additional support close button is not displayed"
        logger.info("Click the Instacart support close Button")
        self.covid19_orderat_page.click_instacart_additional_sup_close_button()
        logger.info("Click the Shop tests on amazon")
        self.covid19_orderat_page.click_shop_tests_on_amazon()
        self.covid19_orderat_page.wait_for_timeout(2)
        self.covid19_orderat_page.is_window_focused()
        opened_tabs = self.covid19_orderat_page.get_open_tab_count()
        assert opened_tabs == 2, "There are no 2 opened tabs"
        assert "https://www.amazon.com/s?k=covid-flu+test" in self.covid19_orderat_page.get_url_from_new_tab(self.covid19_orderat_page)
        self.covid19_orderat_page.is_window_focused()
        self.covid19_orderat_page.wait_for_timeout(2)
        self.covid19_orderat_page.close_current_tab(self.covid19_orderat_page)
        self.covid19_orderat_page.is_window_focused()
        logger.info("Verifying the Amazon additional Support is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUPPORT), "AMAZON Additional support is not displayed"
        logger.info("Verifying the Amazon additional support card 1 symbol is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CARD_1_SYMBOL), "Amazon additional support card 1 symbol is not displayed"
        logger.info("Verifying the Amazon additional support card 1 title is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CARD_1_TITLE), "Amazon additional support card 1 title is not displayed"
        logger.info("Verifying the Amazon additional support card 1 paragraph is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CARD_1_PARA), "Amazon additional support card 1 paragraph is not displayed"
        logger.info("Verifying the Amazon additional support card 1 action is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CARD_1_ACTION), "Amazon additional support card 1 action is not displayed"
        logger.info("Verifying the Amazon additional support card 2 symbol is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CARD_2_SYMBOL), "Amazon additional support card 2 symbol is not displayed"
        logger.info("Verifying the Amazon additional support card 2 title is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CARD_2_TITLE), "Amazon additional support card 2 title is not displayed"
        logger.info("Verifying the Amazon additional support card 2 paragraph is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CARD_2_PARA), "Amazon additional support card 2 paragraph is not displayed"
        logger.info("Verifying the Amazon additional support card 2 action is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CARD_2_ACTION), "Amazon additional support card 2 action is not displayed"
        logger.info("Verifying the Amazon additional support card 3 symbol is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CARD_3_SYMBOL), "Amazon additional support card 3 symbol is not displayed"
        logger.info("Verifying the Amazon additional support card 3 title is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CARD_3_TITLE), "Amazon additional support card 3 title is not displayed"
        logger.info("Verifying the Amazon additional support card 3 paragraph is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CARD_3_PARA), "Amazon additional support card 3 paragraph is not displayed"
        logger.info("Verifying the Amazon additional support card 3 action is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CARD_3_ACTION), "Amazon additional support card 3 action is not displayed"
        logger.info("Verifying the Amazon additional support close button is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CLOSE_BUTTON), "Amazon additional support close button is not displayed"
        logger.info("Click the Amazon additional support close button")
        self.covid19_orderat_page.click_amazon_additional_sup_close_button()
        assert "Respiratory Testing | PfizerForAll™" in self.covid19_orderat_page.get_title()

    def test_verify_test_so_you_know_section(self):
        logger.info("Test verify the test so you know section")
        logger.info("Scroll to the test you know Section")
        self.covid19_orderat_page.scroll_to_element(self.covid19_orderat_page.TEST_YOU_KNOW)
        logger.info("Verify the test you know is displayed")
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.TEST_YOU_KNOW), "Test You's Know is not displayed"
        logger.info(f"Verifying the Test you know text is: {self.covid19_orderat_page.get_text(self.covid19_orderat_page.TEST_YOU_KNOW_TEXT_IS)}")
        assert "Test so you know." in self.covid19_orderat_page.get_text(
            self.covid19_orderat_page.TEST_YOU_KNOW_TEXT_IS), "Test you know text is not displayed"
        logger.info(f"Verifying the Test you know para text is: {self.covid19_orderat_page.get_text(self.covid19_orderat_page.TEST_YOU_KNOW_PARA_TEXT_IS)}")
        assert "That way you can quickly put a plan in place, including talking to a healthcare provider or taking steps to prevent spread of either virus." in self.covid19_orderat_page.get_text(
            self.covid19_orderat_page.TEST_YOU_KNOW_PARA_TEXT_IS), "Test you know text is not displayed"
        logger.info(f"Verifying the Flu text is: {self.covid19_orderat_page.get_text(self.covid19_orderat_page.FLU_TEXT_IS)}")
        assert "Flu" in self.covid19_orderat_page.get_text(self.covid19_orderat_page.FLU_TEXT_IS), "FLU text is not displayed"
        logger.info(f"Verifying the Covid19 text is: {self.covid19_orderat_page.get_text(self.covid19_orderat_page.COVID19_TEXT_IS)}")
        assert "COVID‑19" in self.covid19_orderat_page.get_text(self.covid19_orderat_page.COVID19_TEXT_IS), "Covid19 text is not displayed"
        logger.info(f"Verifying the Flu days text is: {self.covid19_orderat_page.get_text(self.covid19_orderat_page.FLU_DAYS_TEXT_IS)}")
        assert "2 Days" in self.covid19_orderat_page.get_text(self.covid19_orderat_page.FLU_DAYS_TEXT_IS), "FLU days text is not displayed"
        logger.info(f"Verifying the Covid19 days text is: {self.covid19_orderat_page.get_text(self.covid19_orderat_page.COVID19_DAYS_TEXT_IS)}")
        assert "5 Days" in self.covid19_orderat_page.get_text(self.covid19_orderat_page.COVID19_DAYS_TEXT_IS), "Covid19 days text is not displayed"
        logger.info(f"Verifying the Flu and Covid text is: {self.covid19_orderat_page.get_text(self.covid19_orderat_page.FLU_ANS_COVID_TEXT_IS)}")
        assert "The critical period after you first experience symptoms is when medications are most effective. Treatment with medication is not appropriate for everyone, and it's important to talk to your healthcare provider within these timeframes to determine if treatment is appropriate for you." in self.covid19_orderat_page.get_text(
            self.covid19_orderat_page.FLU_ANS_COVID_TEXT_IS), "FLU ANS COVID text is not displayed"
        # Scenario: 3 Verify "The sooner you test" floating section

    def test_verify_the_sooner_you_test_floating_section(self):
        logger.info("Test verify the The sooner you test floating section")
        logger.info("Verifying scroll to the Disclaimer")
        self.covid19_orderat_page.scroll_to_element(self.covid19_orderat_page.DISCLAIMER)
        self.covid19_orderat_page.wait_for_timeout(5)
        logger.info("Verifying the Order a test now is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.ORDER_A_TEST_NOW), "Order a test now is not displayed"
        self.covid19_orderat_page.wait_for_timeout(5)
        logger.info("Click the order a test now")
        self.covid19_orderat_page.click_order_a_test_now()
        logger.info("Verifying the Leaving pfizerforall popup")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.LEAVING_PFIZERFORALL_POPUP), "Leaving pfizerforall is not displayed"
        logger.info("Verifying the Shop tests on amazon is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TESTS_ON_AMAZON_IS), "Shop tests on amazon is not displayed"
        logger.info("Verifying the Shop tests on instacart is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TESTS_ON_INSTACART_IS), "Shop tests on instacart is not displayed"
        logger.info("Verifying the Stay on this site is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.STAY_ON_THIS_SITE), "Stay on site is not displayed"
        logger.info("Click the Stay on this site button")
        self.covid19_orderat_page.click_stay_on_this_site()
        logger.info("Click the order a test now")
        self.covid19_orderat_page.click_order_a_test_now()
        logger.info("Click the shop tests on amazon ")
        self.covid19_orderat_page.click_shop_tests_on_amazon_is()
        self.covid19_orderat_page.wait_for_timeout(2)
        self.covid19_orderat_page.is_window_focused()
        opened_tabs = self.covid19_orderat_page.get_open_tab_count()
        assert opened_tabs == 2, "There are no 2 opened tabs"
        assert "https://www.amazon.com/s?k=covid-flu+test" in self.covid19_orderat_page.get_url_from_new_tab(self.covid19_orderat_page)
        self.covid19_orderat_page.is_window_focused()
        self.covid19_orderat_page.wait_for_timeout(2)
        self.covid19_orderat_page.close_current_tab(self.covid19_orderat_page)
        self.home_page.wait_for_timeout(1)
        logger.info("Verifying the Shop test Amazon additional support is displayed ")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEST_AMAZON_ADDITIONAL_SUPPORT), "Shop test Amazon additional support is not displayed "
        logger.info("Verifying the Shop test Amazon additional sup card 1 symbol is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEST_AMAZON_ADDITIONAL_SUP_CARD_1_SYMBOL), "Shop test Amazon additional sup card 1 symbol is not displayed"
        logger.info("Verifying the Shop test Amazon additional sup card 1 title is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEST_AMAZON_ADDITIONAL_SUP_CARD_1_TITLE), "Shop test Amazon additional sup card 1 title is not displayed"
        logger.info("Verifying the Shop test Amazon additional sup card 1 paragraph is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEST_AMAZON_ADDITIONAL_SUP_CARD_1_PARA), "Shop test Amazon additional sup card 1 paragraph is not displayed"
        logger.info("Verifying the Shop test Amazon additional sup card 1 action is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEST_AMAZON_ADDITIONAL_SUP_CARD_1_ACTION), "Shop test Amazon additional sup card 1 action is not displayed"
        logger.info("Verifying the Shop test Amazon additional sup card 2 symbol is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEST_AMAZON_ADDITIONAL_SUP_CARD_2_SYMBOL), "Shop test Amazon additional sup card 2 symbol is not displayed"
        logger.info("Verifying the Shop test Amazon additional sup card 2 title is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEST_AMAZON_ADDITIONAL_SUP_CARD_2_TITLE), "Shop test Amazon additional sup card 2 title is not displayed"
        logger.info("Verifying the Shop test Amazon additional sup card 2 paragraph is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEST_AMAZON_ADDITIONAL_SUP_CARD_2_PARA), "Shop test Amazon additional sup card 2 paragraph is not displayed"
        logger.info("Verifying the Shop test Amazon additional sup card 2 action is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEST_AMAZON_ADDITIONAL_SUP_CARD_2_ACTION), "Shop test Amazon additional sup card 2 action is not displayed"
        logger.info("Verifying the Shop test Amazon additional sup card 3 symbol is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEST_AMAZON_ADDITIONAL_SUP_CARD_3_SYMBOL), "Shop test Amazon additional sup card 3 symbol is not displayed"
        logger.info("Verifying the Shop test Amazon additional sup card 3 title is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEST_AMAZON_ADDITIONAL_SUP_CARD_3_TITLE), "Shop test Amazon additional sup card 3 title is not displayed"
        logger.info("Verifying the Shop test Amazon additional sup card 3 paragraph is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEST_AMAZON_ADDITIONAL_SUP_CARD_3_PARA), "Shop test Amazon additional sup card 3 paragraph is not displayed"
        logger.info("Shop test Amazon additional support card 3 action is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEST_AMAZON_ADDITIONAL_SUP_CARD_3_ACTION), "Shop test Amazon additional support card 3 action is not displayed"
        logger.info("Shop test Amazon additional support close is displayed")
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEST_AMAZON_ADDITIONAL_SUP_CLOSE_BUTTON), "Shop test Amazon additional support close is not displayed"
        logger.info("Click the test amazon additional support close button")
        self.covid19_orderat_page.click_shop_test_amazon_additional_sup_close_button()
        logger.info("Click the Order atest now")
        self.covid19_orderat_page.click_order_a_test_now()
        logger.info("Click the Shop tests on instacart")
        self.covid19_orderat_page.click_shop_tests_on_instacart_is()
        self.covid19_orderat_page.wait_for_timeout(2)
        self.covid19_orderat_page.is_window_focused()
        opened_tabs = self.covid19_orderat_page.get_open_tab_count()
        assert opened_tabs == 2, "There are no 2 opened tabs"
        assert "https://www.instacart.com/store/brands/pfizer-for-all" in self.covid19_orderat_page.get_url_from_new_tab(self.covid19_orderat_page)
        self.covid19_orderat_page.is_window_focused()
        self.covid19_orderat_page.wait_for_timeout(2)
        self.covid19_orderat_page.close_current_tab(self.covid19_orderat_page)
        self.home_page.wait_for_timeout(1)
        self.covid19_orderat_page.is_window_focused()
        self.covid19_orderat_page.wait_for_timeout(5)
        logger.info("Verifying the Shop test instacart additional support is displayed")
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEST_INSTACART_ADDITIONAL_SUPPORT), "Shop test instacart additional support is not displayed"
        logger.info("Verifying the Shop test instacart additional support card 1 symbol is displayed")
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEXT_INSTACART_ADDITIONAL_SUP_CARD_1_SYMBOL), "Shop test instacart additional support card 1 symbol is not displayed"
        logger.info("Verifying the Shop test instacart additional support card 1 title is displayed")
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEXT_INSTACART_ADDITIONAL_SUP_CARD_1_TITLE), "Shop test instacart additional support card 1 title is not displayed"
        logger.info("Verifying the Shop test instacart additional support card 1 parameter is displayed")
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEXT_INSTACART_ADDITIONAL_SUP_CARD_1_PARA), "Shop test instacart additional support card 1 parameter is not displayed"
        logger.info("Verifying the Shop test instacart additional support card 1 action is displayed")
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEXT_INSTACART_ADDITIONAL_SUP_CARD_1_ACTION), "Shop test instacart additional support card 1 action is not displayed"
        logger.info("Verifying the Shop test instacart additional support card 2 symbol is displayed")
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEXT_INSTACART_ADDITIONAL_SUP_CARD_2_SYMBOL), "Shop test instacart additional support card 2 symbol is not displayed"
        logger.info("Verifying the Shop test instacart additional support card 2 title is displayed")
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEXT_INSTACART_ADDITIONAL_SUP_CARD_2_TITLE), "Shop test instacart additional support card 2 title is not displayed"
        logger.info("Verifying the Shop test instacart additional support card 2 parameter is displayed")
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEXT_INSTACART_ADDITIONAL_SUP_CARD_2_PARA), "Shop test instacart additional support card 2 parameter is not displayed"
        logger.info("Verifying the Shop test instacart additional support card 2 action is displayed")
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEXT_INSTACART_ADDITIONAL_SUP_CARD_2_ACTION), "Shop test instacart additional support card 2 action is not displayed"
        logger.info("Verifying the Shop test instacart additional support card 3 symbol is displayed")
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEXT_INSTACART_ADDITIONAL_SUP_CARD_3_SYMBOL), "Shop test instacart additional support card 3 symbol is not displayed"
        logger.info("Verifying the Shop test instacart additional support card 3 title is displayed")
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEXT_INSTACART_ADDITIONAL_SUP_CARD_3_TITLE), "Shop test instacart additional support card 3 title is not displayed"
        logger.info("Verifying the Shop test instacart additional support card 3 parameter is displayed")
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEXT_INSTACART_ADDITIONAL_SUP_CARD_3_PARA), "Shop test instacart additional support card 3 parameter is not displayed"
        logger.info("Verifying the Shop test instacart additional support card 3 action is displayed")
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEXT_INSTACART_ADDITIONAL_SUP_CARD_3_ACTION), "Shop test instacart additional support card 3 action is not displayed"
        logger.info("Verifying the Shop test instacart additional support close button is displayed")
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TEST_INSTACART_ADDITIONAL_SUP_CLOSE_BUTTON), "Shop test instacart additional support close button is not displayed"
        logger.info("Click the Shop test instacart additional support close button")
        self.covid19_orderat_page.click_shop_test_instacart_additional_sup_close_button()

        #  Scenario:4 Verify "Not Sure If a COVID" section

    def test_verify_not_sure_if_a_covid_section(self):
        logger.info("Test veri the not sure if a covid section")
        logger.info("Verify the not sure covid")
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.NOT_SURE_COVID), "Not sure covid is not displayed"
        logger.info(f"Verifying the Not sure covid text is: {self.covid19_orderat_page.get_text(self.covid19_orderat_page.NOT_SURE_COVID_TEXT_IS)}")
        assert "Not sure if a COVID‑19 or flu at-home test is right for you? Talk to a doctor about your symptoms." in self.covid19_orderat_page.get_text(
            self.covid19_orderat_page.NOT_SURE_COVID_TEXT_IS), "Not sure covid text is not displayed"
        logger.info(f"Verifying the Not sure card 1 text is: {self.covid19_orderat_page.get_text(self.covid19_orderat_page.NOT_SURE_CARD_1_TEXT_IS)}")
        assert "Talk to a doctor quickly,from anywhere." in self.covid19_orderat_page.get_text(
            self.covid19_orderat_page.NOT_SURE_CARD_1_TEXT_IS), "Not sure card1 text is not displayed"
        logger.info(f"Verifying the Not sure card 2 text is: {self.covid19_orderat_page.get_text(self.covid19_orderat_page.NOT_SURE_CARD_2_TEXT_IS)}")
        assert "Make an appointment to see a doctor near you, on your schedule." in self.covid19_orderat_page.get_text(
            self.covid19_orderat_page.NOT_SURE_CARD_2_TEXT_IS), "Not sure card2 text is not displayed"
        logger.info("Click the not sure card 1 arrow button")
        self.covid19_orderat_page.click_not_sure_card_1_arrow()
        assert f"{self.base_url}/respiratory/telehealth" in self.covid19_orderat_page.get_url()
        logger.info("Go back to the previous page")
        self.home_page.go_back_to_previous_page()
        logger.info("Click not sure card 2 arrow")
        self.covid19_orderat_page.click_not_sure_card_2_arrow()

        # Scenario: 5 Verify "Frequently asked questions" section

    def test_verify_frequently_asked_questions_section(self):
        logger.info("Test verify the frequently asked questions section")
        logger.info("Verify the Question 1")
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.QUESTION_1), "Question 1 is not displayed"
        logger.info(f"Verifying the Question 1 text is: {self.covid19_orderat_page.get_text(self.covid19_orderat_page.QUESTION_1_TEXT_IS)}")
        assert "Where can I get a test for COVID‑19 or flu?" in self.covid19_orderat_page.get_text(
            self.covid19_orderat_page.QUESTION_1_TEXT_IS), "Question 1 text is not displayed"
        logger.info(f"Verifying the Question 2 text is: {self.covid19_orderat_page.get_text(self.covid19_orderat_page.QUESTION_2_TEXT_IS)}")
        assert "How accurate are at-home COVID‑19 tests?" in self.covid19_orderat_page.get_text(
            self.covid19_orderat_page.QUESTION_2_TEXT_IS), "Question 2 text is not displayed"
        logger.info(f"Verifying the Question 3 text is: {self.covid19_orderat_page.get_text(self.covid19_orderat_page.QUESTION_3_TEXT_IS)}")
        assert "Why should I get tested for COVID‑19 or flu?" in self.covid19_orderat_page.get_text(
            self.covid19_orderat_page.QUESTION_3_TEXT_IS), "Question 3 text is not displayed"
        logger.info(f"Verifying the Question 4 text is: {self.covid19_orderat_page.get_text(self.covid19_orderat_page.QUESTION_4_TEXT_IS)}")
        assert "Are there any tests for RSV?" in self.covid19_orderat_page.get_text(
            self.covid19_orderat_page.QUESTION_4_TEXT_IS), "Question 4 text is not displayed"
        logger.info("Click the Question 1 span")
        self.covid19_orderat_page.click_question_1_span()
        logger.info("Click the Question 2 span")
        self.covid19_orderat_page.click_question_2_span()
        logger.info("Click the Question 3 span")
        self.covid19_orderat_page.click_question_3_span()
        logger.info("Click the Question 4 span")
        self.covid19_orderat_page.click_question_4_span()
        logger.info(f"Verifying the Answer 1 text is: {self.covid19_orderat_page.get_text(self.covid19_orderat_page.ANSWER_1_TEXT_IS)}")
        assert "No need to leave home. You can easily buy them online. There are two types of at-home tests: antigen and molecular." in self.covid19_orderat_page.get_text(
            self.covid19_orderat_page.ANSWER_1_TEXT_IS), "Answer 1 text is not displayed"
        logger.info(f"Verifying the Answer 2 text is: {self.covid19_orderat_page.get_text(self.covid19_orderat_page.ANSWER_2_TEXT_IS)}")
        assert "The good news is that any positive result from an at-home test, antigen or molecular, is considered reliable. For antigen tests in the case of a negative result, the FDA recommends that you test again after 48 hours, and maybe once more again after 48 hours (depending on your symptoms and situation)." in self.covid19_orderat_page.get_text(
            self.covid19_orderat_page.ANSWER_2_TEXT_IS), "Answer 2 text is not displayed"
        logger.info(f"Verifying the Answer 3 text is: {self.covid19_orderat_page.get_text(self.covid19_orderat_page.ANSWER_3_TEXT_IS)}")
        assert "Testing as soon as you have symptoms can give you important information to determine your next steps, including getting proper medical care or treatment, if appropriate. Timing is everything. If you test positive for COVID‑19 or flu, talk to a doctor to determine if prescription medications are appropriate for you and make sure you're taking appropriate steps to prevent spreading the illness to others. For both COVID‑19 and flu, these medications are most effective when taken early—within 5 days of feeling COVID‑19 symptoms and within 2 days of feeling flu symptoms." in self.covid19_orderat_page.get_text(
            self.covid19_orderat_page.ANSWER_3_TEXT_IS), "Answer 3 text is not displayed"
        logger.info(f"Verifying the Answer 4 text is: {self.covid19_orderat_page.get_text(self.covid19_orderat_page.ANSWER_4_TEXT_IS)}")
        assert "Yes. There are several in-office tests that your doctor can do to determine if you have RSV, including rapid antigen testing. If you think you have symptoms of RSV, talk to your healthcare provider right away." in self.covid19_orderat_page.get_text(
            self.covid19_orderat_page.ANSWER_4_TEXT_IS), "Answer 4 text is not displayed"

        # Scenario: 6 Verify disclaimer text on COVID-19 Order at-home tests page

    def test_verify_disclaimer_text_on_covid19_order_at_home_test_page(self):
        logger.info("Test verify the disclaimer text on covid19 order at home test page")
        logger.info("Scroll to the bottom of the page")
        self.covid19_orderat_page.scroll_to_element(self.covid19_orderat_page.BOTTOM_OF_THE_PAGE)
        logger.info(f"Verifying the Disclaimer text is: {self.covid19_orderat_page.get_text(self.covid19_orderat_page.DISCLAIMER_TEXT_IS)}")
        assert "FOR U.S. RESIDENTS ONLY. The information provided is for educational purposes only and is not intended to replace discussions with a healthcare professional.© 2025 Pfizer Inc. All rights reserved. PP-UNP-USA-6048" in self.covid19_orderat_page.get_text(
            self.covid19_orderat_page.DISCLAIMER_TEXT_IS), "Disclaimer text is not displayed"

