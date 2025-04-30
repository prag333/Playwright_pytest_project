from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def get_url(self) -> str:
        """Get current URL."""
        return self.page.url

    def find_element(self, locator: tuple):
        """Find a single element based on the locator type (XPATH, CSS, ID, TEXT)."""
        locator_type, locator_value = locator

        if locator_type == 'XPATH':
            return self.page.locator(locator_value)
        elif locator_type == 'CSS':
            return self.page.locator(locator_value)
        elif locator_type == 'ID':
            return self.page.locator(f'#{locator_value}')
        elif locator_type == 'TEXT':
            return self.page.locator(f'text={locator_value}')
        else:
            raise ValueError(f"Unsupported locator type: {locator_type}")

    def click(self, locator: tuple):
        """Click on a single element."""
        self.find_element(locator).click()

    def get_text(self, locator: tuple):
        """Get text from a single element."""
        try:
            return self.find_element(locator).text_content()
        except PlaywrightTimeoutError:
            return None

    def is_visible(self, locator: tuple, timeout: int = 10) -> bool:
        """Check if element is visible on the page."""
        try:
            self.wait_until_visible(locator, timeout=timeout)
            return self.find_element(locator).is_visible(timeout=timeout * 1000)
        except TimeoutError:
            return False

    def wait_until_visible(self, locator: tuple, timeout: int = 10) -> bool:
        """Wait until the element is visible on the page."""
        try:
            self.find_element(locator).wait_for(state="visible", timeout=timeout * 1000)
            return True
        except PlaywrightTimeoutError:
            return False

    def scroll_to_element(self, locator: tuple):
        """Scroll the page until the element is in view."""
        self.find_element(locator).scroll_into_view_if_needed()

    def go_back(self, timeout: int = 5):
        """Navigates to the previous page in the browser history."""
        self.page.go_back(timeout=timeout * 1000)

    def wait_for_timeout(self, seconds: float):
        """
        Waits for a specified number of seconds using Playwright's wait_for_timeout.
        Does not block like time.sleep.
        """
        self.page.wait_for_timeout(seconds * 1000)

    def get_title(self):
        """Return the title of the page."""
        return self.page.title()

    def is_element_enabled(self, locator: tuple):
        """Check if element is enabled."""
        try:
            self.wait_until_visible(locator, timeout=10)
            return self.find_element(locator).is_enabled()
        except PlaywrightTimeoutError:
            print("Element not enabled")
            return False

    def is_window_focused(self):
        """Check if window is focused."""
        try:
            return self.page.evaluate("document.hasFocus()")
        except PlaywrightTimeoutError:
            return False

    @staticmethod
    def get_url_from_new_tab(context):
        """Return the URL for new tab"""
        try:
            context1 = context.page.context
            new_tab = [p for p in context1.pages if p != context.page][0]
            new_tab.wait_for_load_state()
            return new_tab.url
        except PlaywrightTimeoutError:
            return None

    @staticmethod
    def close_current_tab(context):
        """Close the current tab"""
        context1 = context.page.context
        new_tab = [p for p in context1.pages if p != context.page][0]
        new_tab.wait_for_load_state()
        new_tab.close()

    def get_open_tab_count(self):
        return len(self.page.context.pages)