from playwright.sync_api import Page


class PlaywrightUtils:
    def __init__(self, page: Page):
        self.page = page
