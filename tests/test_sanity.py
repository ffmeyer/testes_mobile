# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from page.task_page import TaskPage
from page.task_properties_page import TaskPropertiesPage
from page.welcome_page import WelcomePage


class TestSanity:

    def test_list_tasks(self, open_app):

        wp = WelcomePage(open_app)
        wp.skip_welcome()
        tp = TaskPage(open_app)
        # print(tp.get_task_list())
        assert tp.get_task_list() is not None

    def test_list_done_tasks_names(self, open_app):
        wp = WelcomePage(open_app)
        wp.skip_welcome()
        tp = TaskPage(open_app)
        # print(tp.get_all_done_task_names())
        assert tp.get_all_done_task_names() is not None
