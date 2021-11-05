import unittest
import pytest

from pages.home_page import HomePage
from utils.data import MenuCloseHeader


@pytest.mark.usefixtures("set_up")
class HomeTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def before_test(self, set_up):
        self.home_page = HomePage(set_up)

    def test_home_page_header(self):
        self.home_page.accept_cookie_if_visible()
        assert self.home_page.get_header().inner_text() == "HEITS", \
            f"Text is {self.home_page.get_header().inner_text()}"

    def test_menu_button(self):
        self.home_page.accept_cookie_if_visible()
        self.home_page.click_menu_header_button(MenuCloseHeader.MENU.value)
        self.home_page.click_menu_header_button(MenuCloseHeader.CLOSE.value)
