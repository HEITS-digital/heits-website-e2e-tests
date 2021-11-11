from playwright._impl._locator import Locator
from playwright.sync_api import Page

from utils.data import MenuCloseHeader
from utils.playwright_utils import PlaywrightUtils


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.playwright_utils = PlaywrightUtils(page)

    # private
    __I_ACCEPT_COOKIE_BUTTON_XPATH = "//span[contains(text(),'I accept')]"
    __HEADER_HEITS_XPATH = "//h1[contains(text(), 'HEITS')]"
    __HEADER_MENU_BUTTON_XPATH = "//a/span[contains(text(), '{}')]"

    def get_header(self) -> Locator:
        return self.page.locator(self.__HEADER_HEITS_XPATH)

    def get_menu_or_close_header(self, menu_or_close: MenuCloseHeader) -> Locator:
        return self.page.locator(self.__HEADER_MENU_BUTTON_XPATH.format(menu_or_close))

    def get_menu_or_close_header_inner_text(self, menu_or_close: MenuCloseHeader) -> str:
        return self.page.locator(self.__HEADER_MENU_BUTTON_XPATH.format(menu_or_close)).inner_text()

    # clicks
    def click_menu_header_button(self, menu_or_close: MenuCloseHeader):
        self.get_menu_or_close_header(menu_or_close).click()

    def accept_cookie(self):
        self.page.wait_for_selector(self.__I_ACCEPT_COOKIE_BUTTON_XPATH).click()
