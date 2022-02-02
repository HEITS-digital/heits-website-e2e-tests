from playwright.sync_api import Page, Locator


class PlaywrightUtils:
    def __init__(self, page: Page):
        self.page = page

    def wait_and_get_locator(self, locator: str, milliseconds=30000) -> Locator:
        """
        :param milliseconds: how much time to wait in milliseconds
        :type milliseconds: float
        :param locator: locator in the form of xpath, css etc.
        :type locator: str
        :return: locator that will be further used for certain actions
        :rtype: Locator
        """
        element = self.page.locator(locator)
        element.wait_for(timeout=milliseconds)
        return element
