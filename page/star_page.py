import time

from appium.webdriver.common.appiumby import AppiumBy

from page.base_page import base_page
from page.task_page import TaskPage
from utils import constants


class StarPage(base_page):

    def __init__(self, driver):
        super(StarPage, self).__init__(driver=driver)
        self.id_star_tab = (AppiumBy.ID, "com.google.android.apps.tasks:id/stars_tab")

    def click_on_starred_tasks(self):
        self.click_on(self.id_star_tab)

    def get_star_task_list(self, task: TaskPage):
        starred_tasks = task.get_task_list()
        web_elements_starred_tasks = []
        for star_task in starred_tasks:
            if constants.text_starred_item in star_task.tag_name:
                web_elements_starred_tasks.append(star_task)

        return web_elements_starred_tasks

    def get_all_starred_task_titles(self, task: TaskPage):
        list_items = self.get_star_task_list(task)
        tasks_names = []
        for item in list_items:
            tasks_names.append(item.tag_name.replace(constants.text_replace_starred_item, ''))
        return tasks_names
