import unittest
import pytest
from delayed_assert import expect, assert_expectations

from pages.home_page import HomePage
from utils.data import MenuItems


@pytest.mark.usefixtures("setup")
class HomeTest(unittest.TestCase):
    __HEITS = 'HEITS'
    __MENU = 'Menu'
    __CLOSE = 'Close'

    @pytest.fixture(autouse=True)
    def before_test(self, setup):
        self.home_page = HomePage(setup)

    def test_home_page_header(self):
        assert self.home_page.get_header_inner_text() == self.__HEITS

    def test_menu_button(self):
        menu_inner_text = self.home_page.get_menu_header_inner_text()
        expect(self.home_page.get_menu_header_inner_text() == self.__MENU,
               f"actual : {menu_inner_text}"
               f"expected {self.__MENU}")

        self.home_page.click_menu_header_button()

        close_inner_text = self.home_page.get_close_header_inner_text()
        expect(close_inner_text == self.__CLOSE,
               f"actual {close_inner_text}, "
               f"expected {self.__CLOSE} ")

        self.home_page.click_close_header_button()
        expect(self.home_page.get_menu_header_inner_text() == self.__MENU,
               f"actual {self.home_page.get_menu_header_inner_text()} , "
               f"expected {self.__MENU}")

        assert_expectations()

    def test_machine_learning_page(self):
        self.home_page.click_menu_header_button()
        self.home_page.click_menu_item(MenuItems.MACHINE_LEARNING.values[0])
        self.home_page.page.wait_for_url(MenuItems.MACHINE_LEARNING.values[1])
        assert self.home_page.page.url == MenuItems.MACHINE_LEARNING.values[1]

    def test_digital_software_development_page(self):
        self.home_page.click_menu_header_button()
        self.home_page.click_menu_item(MenuItems.DIGITAL_SOFTWARE_DEVELOPMENT.values[0])
        self.home_page.page.wait_for_url(MenuItems.DIGITAL_SOFTWARE_DEVELOPMENT.values[1])
        assert self.home_page.page.url == MenuItems.DIGITAL_SOFTWARE_DEVELOPMENT.values[1]

    def test_user_experience_page(self):
        self.home_page.click_menu_header_button()
        self.home_page.click_menu_item(MenuItems.USER_EXPERIENCE.values[0])
        self.home_page.page.wait_for_url(MenuItems.USER_EXPERIENCE.values[1])
        assert self.home_page.page.url == MenuItems.USER_EXPERIENCE.values[1]

    def test_culture_page(self):
        self.home_page.click_menu_header_button()
        self.home_page.click_menu_item(MenuItems.CULTURE.values[0])
        self.home_page.page.wait_for_url(MenuItems.CULTURE.values[1])
        assert self.home_page.page.url == MenuItems.CULTURE.values[1]

    def test_our_work_page(self):
        self.home_page.click_menu_header_button()
        self.home_page.click_menu_item(MenuItems.OUR_WORK.values[0])
        self.home_page.page.wait_for_url(MenuItems.OUR_WORK.values[1])
        assert self.home_page.page.url == MenuItems.OUR_WORK.values[1]

    def test_engagement_models_page(self):
        self.home_page.click_menu_header_button()
        self.home_page.click_menu_item(MenuItems.ENGAGEMENT_MODELS.values[0])
        self.home_page.page.wait_for_url(MenuItems.ENGAGEMENT_MODELS.values[1])
        assert self.home_page.page.url == MenuItems.ENGAGEMENT_MODELS.values[1]
