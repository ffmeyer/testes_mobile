import time

from appium.webdriver.common.appiumby import AppiumBy

from page.base_page import base_page


class TaskPropertiesPage(base_page):

    def __init__(self, driver):
        super(TaskPropertiesPage, self).__init__(driver=driver)
        self.id_add_task = (AppiumBy.ID, "com.google.android.apps.tasks:id/star_option")
        self.xpath_three_dots = (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Mais opções']")
        self.id_delete_task = (AppiumBy.ID, 'com.google.android.apps.tasks:id/title')
        self.id_delete_notification = (AppiumBy.ID, 'com.google.android.apps.tasks:id/snackbar_text')

    def star_task(self):
        self.get_element(self.id_add_task)

    def delete_task(self):
        self.click_on(self.xpath_three_dots)
        self.click_on(self.id_delete_task)

    def get_delete_ui_message_text(self):
        return self.get_element(self.id_delete_notification).text



