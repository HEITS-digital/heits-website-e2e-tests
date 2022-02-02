
from playwright.sync_api import Page, Locator

from utils.data import MenuCloseHeader, MenuItems
from utils.playwright_utils import PlaywrightUtils


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.playwright_utils = PlaywrightUtils(page)

    # private
    __I_ACCEPT_COOKIE_BUTTON_XPATH = "//span[contains(text(),'I accept')]"
    __HEADER_HEITS_XPATH = "//h1[text()='HEITS']"
    __HEADER_MENU_BUTTON_XPATH = "//button/span[contains(text(), '{}')]"
    __MENU_ITEM = "//span[contains(text(),'{}')]"

    # getters
    def get_header(self) -> Locator:
        return self.page.locator(self.__HEADER_HEITS_XPATH)

    def get_menu_or_close_header(self, menu_or_close: MenuCloseHeader) -> Locator:
        return self.page.locator(self.__HEADER_MENU_BUTTON_XPATH.format(menu_or_close))

    def get_menu_or_close_header_inner_text(self, menu_or_close: MenuCloseHeader) -> str:
        return self.playwright_utils.wait_and_get_locator(self.__HEADER_MENU_BUTTON_XPATH.format(menu_or_close)).inner_text()

    # clicks
    def accept_cookie(self):
        self.page.wait_for_selector(self.__I_ACCEPT_COOKIE_BUTTON_XPATH).click()

    def click_menu_header_button(self, menu_or_close: MenuCloseHeader):
        self.get_menu_or_close_header(menu_or_close).click()

    def click_menu_item(self, item: MenuItems):
        """
         function that clicks whatever menu item based on the enum class e.g. Machine learning, User experience etc.
        :param item: items that are found in the dropdown after clicking Menu button from home page
        """
        self.page.wait_for_selector(self.__MENU_ITEM.format(item)).click()
