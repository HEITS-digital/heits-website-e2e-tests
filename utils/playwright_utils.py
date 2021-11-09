
class PlaywrightUtils:
    def __init__(self, page):
        self.page = page

    def wait_and_get_element(self, locator):
        try:
            if self.page.locator(locator).is_visible():
                return self.page.locator(locator)
            else:
                return None
        except:
            return
