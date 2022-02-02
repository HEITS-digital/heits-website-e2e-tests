import pytest
from utils.playwright_utils import PlaywrightUtils as playwright_utils

from utils.data import Urls

__ACCEPTED_COOKIE_LS = 'window.localStorage.setItem("accepted-cookie", "true")'
__I_ACCEPT_XPATH = "//button/span[contains(text(), 'accept')]"


@pytest.fixture
def setup(page):
    page.goto(Urls.BASE_URL.value)
    playwright_utils(page).wait_and_get_locator(__I_ACCEPT_XPATH).click()
    yield page
