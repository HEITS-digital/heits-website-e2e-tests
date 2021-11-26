import pytest

from utils.data import Urls

__ACCEPTED_COOKIE_LS = 'window.localStorage.setItem("accepted-cookie", "true")'


@pytest.fixture
def set_up(page):
    page.goto(Urls.BASE_URL.value)
    # inject local storage k/v to set accept cookies on true
    page.evaluate(__ACCEPTED_COOKIE_LS)
    # reload for the injecting of local storage to take effect
    page.reload()
    # wait for load state of the page to baseUrl to be completed
    page.wait_for_load_state()
    # almost same as return
    yield page
