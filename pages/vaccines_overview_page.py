from pages.base_page import BasePage


class VaccinesOverviewPage(BasePage):

    ACCEPT_ALL = ('XPATH', "//button[contains(@id, 'onetrust-accept-btn-handler')]")

#  Scenario 1 : Verify Navigation to Vaccine overview page

    MENU = ('XPATH', "//button[contains(@class, 'primary')]")
    VACCINES = ('XPATH', "(//*[text()='Vaccines'])[1]")
    VACCINES_OVERVIEW = ('XPATH', "(//*[text()='Vaccines overview'])[1]")

    " Then The page url is '{%BASE_URL%}/vaccine-options' "

# Scenario2: Verify Hero section on Vaccine Overview page

    VACCINES_OVERVIEW_HEADER = ('XPATH', "//h1[contains(@id, 'help-protectyourself-and-yourfamily-with-the-latestvaccines')]")
    VACCINES_OVERVIEW_HEADER_TEXT =('XPATH', "//h1[contains(@id, 'help-protectyourself-and-yourfamily-with-the-latestvaccines')]")
    VACCINES_OVERVIEW_P_TEXT = ('XPATH', "//*[text()='Find and schedule respiratory vaccinations. Depending on your insurance, some may be available at zero cost to you.']")
    CHECK_YOUR_VACCINE_ELIGIBILITY_BUTTON = ('XPATH', "//a[contains(@id, 'vaccine-options-non-homepage-eligibility-1')]")
    FIND_AND_SCHEDULE_NOW_BUTTON = ('XPATH', "//a[contains(@id, 'vaccine-options-non-homepage-now-0')]")
    "  Then There are '2' tabs currently opened "
    " When I focus the last opened window "
    "  Then The page url contains 'www.vaxassist.com/pfizer-for-all/eligibility' "
    "  When I close the current opened tab"
    "  And I focus the last opened tab "



    def click_menu(self):
        self.wait_until_visible(self.MENU, timeout=1000)
        self.click(self.MENU)

    def click_vaccines(self):
        self.wait_until_visible(self.VACCINES, timeout=1000)
        self.click(self.VACCINES)

    def click_vaccines_overview(self):
        self.wait_until_visible(self.VACCINES_OVERVIEW, timeout=1000)
        self.click(self.VACCINES_OVERVIEW)

    def click_check_your_vaccine_eligibility_button(self):
        self.wait_until_visible(self.CHECK_YOUR_VACCINE_ELIGIBILITY_BUTTON, timeout=1000)
        self.click(self.CHECK_YOUR_VACCINE_ELIGIBILITY_BUTTON)

    def click_find_and_schedule_now_button(self):
        self.wait_until_visible(self.FIND_AND_SCHEDULE_NOW_BUTTON, timeout=1000)
        self.click(self.FIND_AND_SCHEDULE_NOW_BUTTON)

