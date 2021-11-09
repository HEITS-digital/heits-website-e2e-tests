import pytest


@pytest.fixture
def set_up(page):
    page.goto("https://apex.heits.digital/#")

    # almost same as return
    yield page
