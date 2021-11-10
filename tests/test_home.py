import unittest
import pytest
from delayed_assert import expect, assert_expectations

from pages.home_page import HomePage
from utils.data import MenuCloseHeader


@pytest.mark.usefixtures("set_up")
class HomeTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def before_test(self, set_up):
        self.home_page = HomePage(set_up)

    def test_home_page_header(self):
        assert self.home_page.get_header().inner_text() == "HEITS", \
            f"Text is {self.home_page.get_header().inner_text()}"

    def test_menu_button(self):
        menu_inner_text = self.home_page.get_menu_or_close_header_inner_text(MenuCloseHeader.MENU.value)
        expect(self.home_page.get_menu_or_close_header_inner_text(MenuCloseHeader.MENU.value) == 'Menu',
               f"expected Menu , actual {menu_inner_text}")

        self.home_page.click_menu_header_button(MenuCloseHeader.MENU.value)

        close_inner_text = self.home_page.get_menu_or_close_header_inner_text(MenuCloseHeader.CLOSE.value)
        expect(close_inner_text == 'Close',
               f"expected Close , actual {close_inner_text}")

        self.home_page.click_menu_header_button(MenuCloseHeader.CLOSE.value)
        expect(self.home_page.get_menu_or_close_header_inner_text(MenuCloseHeader.MENU.value) == 'Menu',
               f"expected Menu , actual {self.home_page.get_menu_or_close_header_inner_text(MenuCloseHeader.MENU.value)}")

        assert_expectations()
