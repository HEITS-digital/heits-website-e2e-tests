import pytest

from utils.data import Urls

__ACCEPTED_COOKIE_LS = 'window.localStorage.setItem("accepted-cookie", "true")'
__I_ACCEPT_XPATH = "//button/span[contains(text(), 'accept')]"


@pytest.fixture
def setup(page):
    page.goto(Urls.BASE_URL.value)
    page.wait_for_selector(__I_ACCEPT_XPATH).click()
    yield page
