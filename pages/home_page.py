from playwright._impl._locator import Locator
from playwright.sync_api import Page

from utils.data import MenuCloseHeader
from utils.playwright_utils import PlaywrightUtils

I_ACCEPT_COOKIE_BUTTON_XPATH = "//span[contains(text(),'I accept')]"
HEADER_HEITS_XPATH = "//h1[contains(text(), 'HEITS')]"
HEADER_MENU_BUTTON_XPATH = "//a/span[contains(text(), '{}')]"


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.playwright_utils = PlaywrightUtils(page)

    # Voids
    def accept_cookie_if_visible(self):
        # accept the cookie pop-up
        cookie_i_accept_button = self.playwright_utils.wait_and_get_element(I_ACCEPT_COOKIE_BUTTON_XPATH)
        if cookie_i_accept_button is not None:
            cookie_i_accept_button.click()

    # Elements
    def get_header(self) -> Locator:
        return self.page.locator(HEADER_HEITS_XPATH)

    def get_menu_or_close_header(self, menu_or_close: MenuCloseHeader) -> Locator:
        return self.page.locator(HEADER_MENU_BUTTON_XPATH.format(menu_or_close))

    # Clicks
    def click_menu_header_button(self, menu_or_close: MenuCloseHeader):
        self.get_menu_or_close_header(menu_or_close).click()
