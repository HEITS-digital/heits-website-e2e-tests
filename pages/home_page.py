from playwright.sync_api import Page

from utils.data import MenuItems
from utils.playwright_utils import PlaywrightUtils


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.playwright_utils = PlaywrightUtils(page)

    # private
    __I_ACCEPT_COOKIE_BUTTON_XPATH = "//span[contains(text(),'I accept')]"
    __HEADER_HEITS_XPATH = "//h1[text()='HEITS']"
    __HEADER_MENU_BUTTON_XPATH = "//button/span[contains(text(), 'Menu')]"
    __HEADER_CLOSE_BUTTON_XPATH = "//button/span[contains(text(), 'Close')]"
    __MENU_ITEM = "//span[contains(text(),'{}')]"

    # getters
    def get_header_inner_text(self) -> str:
        return self.page.locator(self.__HEADER_HEITS_XPATH).inner_text()

    def get_menu_header_inner_text(self) -> str:
        return self.page.locator(self.__HEADER_MENU_BUTTON_XPATH).inner_text()

    def get_close_header_inner_text(self) -> str:
        return self.page.locator(self.__HEADER_CLOSE_BUTTON_XPATH).inner_text()

    # clicks
    def click_menu_header_button(self):
        self.page.wait_for_selector(self.__HEADER_MENU_BUTTON_XPATH).click()

    def click_close_header_button(self):
        self.page.wait_for_selector(self.__HEADER_CLOSE_BUTTON_XPATH).click()

    def click_menu_item(self, item: MenuItems):
        """
         function that clicks whatever menu item based on the enum class e.g. Machine learning, User experience etc.
        :param item: items that are found in the dropdown after clicking Menu button from home page
        """
        self.page.wait_for_selector(self.__MENU_ITEM.format(item)).click()
