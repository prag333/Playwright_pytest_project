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

        #   Given Browser is maximized
        #         And I am on the url '/'
        #         And I pause for '5' s

        logger.info("Common steps for Covid19TalkDoctorPage")
        self.home_page.go_to_homepage(self.base_url)
        assert "Pfizer" in driver.title()
        assert self.covid19_orderat_page.is_visible(self.covid19_orderat_page.ACCEPT_ALL, timeout=30)
        self.home_page.click_accept_cookies()
        self.covid19_orderat_page.scroll_to_element(self.covid19_orderat_page.MENU_BUTTON)
        self.covid19_orderat_page.click_menu_button()
        assert "COVID-19 & flu" in self.covid19_orderat_page.get_text(self.covid19_orderat_page.COVID19_FLU_TEXT_IS), "COVID-19 & flu text is not displayed"
        self.covid19_orderat_page.click_covid19_flu_button()
        assert "Order at-home tests" in self.covid19_orderat_page.get_text(self.covid19_orderat_page.ORDER_AT_HOME_TESTS_IS), "Order at-home tests is"
        self.covid19_orderat_page.click_order_at_home_tests_button()
        assert f"{self.base_url}/respiratory/testing" in self.covid19_orderat_page.get_url()
        # assert "Respiratory Testing | PfizerForAll™" in self.covid19_orderat_page.get_text(self.covid19_orderat_page.TITLE_IS), "Title is not displayed"

        # Scenario: 1 Verify navigation to Instacart and Amazon from Hero section of COVID-19 Order at-home page
    def test_verify_navigation_to_Instacart_and_Amazon_from_Hero_section_covid19_order_at_home_page(self):
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.HERO_TEXT), "Hero text is not displayed"
        assert "An at-home test can tell you if you have COVID-19 or flu." in self.covid19_orderat_page.get_text(self.covid19_orderat_page.HERO_TEXT_IS), "Hero text is not displayed"
        assert "There are many tests that can detect if you have COVID-19 or flu. Order online and get a test delivered as early as today." in self.covid19_orderat_page.get_text(self.covid19_orderat_page.SUB_TEXT_IS), "Sub text is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TESTS_ON_AMAZON), "Shop tests on Amazon is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.SHOP_TESTS_ON_INSTACART), "Shop tests on Instacart is not displayed"
        self.covid19_orderat_page.wait_for_timeout(5)
        self.covid19_orderat_page.click_shop_tests_on_instacart()
        # Then There are '2' tabs currently opened
        assert f"{self.base_url}/respiratory/testing" in self.covid19_orderat_page.get_url()
        self.covid19_orderat_page.is_window_focused()
        self.covid19_orderat_page.wait_for_timeout(2)
        self.covid19_orderat_page.close_current_tab(self.covid19_orderat_page)
        self.home_page.wait_for_timeout(1)
        self.covid19_orderat_page.is_window_focused()
        self.covid19_orderat_page.wait_for_timeout(5)
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUPPORT), "Additional Support is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CARD_1_SYMBOL), "Additional support card 1 symbol is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CARD_1_TITLE), "Additional support card 1 title is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CARD_1_PARA), "Additional support card 1 paragraph is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CARD_1_ACTION), "Additional support card 1 action is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CARD_2_SYMBOL), "Additional support card 2 symbol is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CARD_2_TITLE), "Additional support card 2 title is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CARD_2_PARA), "Additional support card 2 paragraph is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CARD_2_ACTION), "Additional support card 2 action is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CARD_3_SYMBOL), "Additional support card 3 symbol is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CARD_3_TITLE), "Additional support card 3 title is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CARD_3_PARA), "Additional support card 3 paragraph is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CARD_3_ACTION), "Additional support card 3 action is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.INSTACART_ADDITIONAL_SUP_CLOSE_BUTTON), "Additional support close button is not displayed"
        self.covid19_orderat_page.click_instacart_additional_sup_close_button()
        self.covid19_orderat_page.click_shop_tests_on_amazon()
        #    Then There are '2' tabs currently opened
        assert f"{self.base_url}/respiratory/testing" in self.covid19_orderat_page.get_url()
        self.covid19_orderat_page.is_window_focused()
        self.covid19_orderat_page.wait_for_timeout(2)
        self.covid19_orderat_page.close_current_tab(self.covid19_orderat_page)
        self.home_page.wait_for_timeout(1)
        self.covid19_orderat_page.is_window_focused()
        self.covid19_orderat_page.wait_for_timeout(5)
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUPPORT), "Additional support is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CARD_1_SYMBOL), "Amazon additional support card 1 symbol is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CARD_1_TITLE), "Amazon additional support card 1 title is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CARD_1_PARA), "Amazon additional support card 1 paragraph is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CARD_1_ACTION), "Amazon additional support card 1 action is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CARD_2_SYMBOL), "Amazon additional support card 2 symbol is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CARD_2_TITLE), "Amazon additional support card 2 title is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CARD_2_PARA), "Amazon additional support card 2 paragraph is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CARD_2_ACTION), "Amazon additional support card 2 action is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CARD_3_SYMBOL), "Amazon additional support card 3 symbol is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CARD_3_TITLE), "Amazon additional support card 3 title is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CARD_3_PARA), "Amazon additional support card 3 paragraph is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CARD_3_ACTION), "Amazon additional support card 3 action is not displayed"
        self.covid19_orderat_page.is_visible(self.covid19_orderat_page.AMAZON_ADDITIONAL_SUP_CLOSE_BUTTON), "Amazon additional support close button is not displayed"
        self.covid19_orderat_page.click_amazon_additional_sup_close_button()
        #  Then The title is 'Respiratory Testing | PfizerForAll™'

        #  Scenario: 2 Verify "Test so you know" section
