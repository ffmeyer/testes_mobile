import time

from appium.webdriver.common.appiumby import AppiumBy

from page.base_page import base_page


class WelcomePage(base_page):

    def __init__(self, driver):
        super(WelcomePage, self).__init__(driver=driver)
        self.id_welcome_image = (AppiumBy.ID, "com.google.android.apps.tasks:id/welcome_image")
        self.id_next_button = (AppiumBy.ID, "com.google.android.apps.tasks:id/next_button")
        self.id_allow_button = (AppiumBy.ID, "com.google.android.apps.tasks:id/npr_allow_button")
        self.id_permission_allow_button = (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')

    def skip_welcome(self):
        time.sleep(2)
        self.wait_clickable_element(self.id_welcome_image)
        self.click_on(self.id_welcome_image)
        self.click_on(self.id_next_button)
        self.click_on(self.id_allow_button)
        self.click_on(self.id_permission_allow_button)
        time.sleep(5)
