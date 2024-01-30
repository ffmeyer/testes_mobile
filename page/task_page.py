import time

from appium.webdriver.common.appiumby import AppiumBy

from page.base_page import base_page
from utils import constants


class TaskPage(base_page):

    def __init__(self, driver):
        super(TaskPage, self).__init__(driver=driver)
        self.id_add_task = (AppiumBy.ID, "com.google.android.apps.tasks:id/tasks_fab")
        self.id_add_task_title = (AppiumBy.ID, "com.google.android.apps.tasks:id/add_task_title")
        self.id_add_task_done = (AppiumBy.ID, "com.google.android.apps.tasks:id/add_task_done")
        self.id_tasks_list = (AppiumBy.ID, "com.google.android.apps.tasks:id/tasks_list")
        self.id_task_items = (AppiumBy.ID, "com.google.android.apps.tasks:id/task_item_layout")
        self.id_star_task = (AppiumBy.ID, "com.google.android.apps.tasks:id/star_button")
        self.id_done_task = (AppiumBy.ID, "com.google.android.apps.tasks:id/tasks_item_completed_check")
        self.id_properties_task = (AppiumBy.ID, "com.google.android.apps.tasks:id/task_name")
        self.id_expand_done_tasks = (AppiumBy.ID, "com.google.android.apps.tasks:id/expand")
        self.id_done_task_lists = (AppiumBy.ID, 'com.google.android.apps.tasks:id/tasks_item_completed_check')
        self.id_done_notification = (AppiumBy.ID, 'com.google.android.apps.tasks:id/snackbar_text')

    def add_task(self, task_title):
        self.wait_clickable_element(self.id_add_task)
        self.get_element(self.id_add_task)
        self.click_on(self.id_add_task)
        self.wait_clickable_element(self.id_add_task_title)
        self.get_element(self.id_add_task_title)
        self.click_on(self.id_add_task_title)
        time.sleep(1)
        self.write_text(self.id_add_task_title, task_title)
        self.click_on(self.id_add_task_done)

    def get_task_list(self):
        tasks_list = self.get_element(self.id_tasks_list)
        return self.get_web_elements(tasks_list, self.id_task_items)

    def star_task(self, task_title):
        list_items = self.get_task_list()
        for item in list_items:
            if item.tag_name == task_title:
                btn_star_task = item.find_element(*self.id_star_task)
                btn_star_task.click()

    def done_task(self, task_title):
        list_items = self.get_task_list()
        for item in list_items:
            if item.tag_name == task_title:
                btn_done_task = item.find_element(*self.id_done_task)
                btn_done_task.click()

    def click_properties_task(self, task_title):
        self.wait_clickable_element(self.id_tasks_list)
        list_items = self.get_task_list()
        for item in list_items:
            if item.tag_name == task_title:
                btn_properties_task = item.find_element(*self.id_properties_task)
                btn_properties_task.click()
                break

    def get_all_task_names(self):
        list_items = self.get_task_list()
        tasks_names = []
        for item in list_items:
            tasks_names.append(item.tag_name)
        return tasks_names

    def click_on_done_tasks(self):
        self.wait_clickable_element(self.id_expand_done_tasks)
        self.click_on(self.id_expand_done_tasks)

    def get_done_task_list(self):
        self.click_on_done_tasks()
        done_tasks = self.get_task_list()
        web_elements_task_done = []
        for done_task in done_tasks:
            if constants.text_task_done in done_task.tag_name:
                web_elements_task_done.append(done_task)

        return web_elements_task_done

    def get_all_done_task_names(self):
        list_items = self.get_done_task_list()
        tasks_names = []
        for item in list_items:
            tasks_names.append(item.tag_name.replace(constants.text_replace_done_item, ''))
        return tasks_names

    def is_task_done(self, task_title):
        return task_title in self.get_all_done_task_names()

    def get_done_ui_message_text(self):
        return self.get_element(self.id_done_notification).text
