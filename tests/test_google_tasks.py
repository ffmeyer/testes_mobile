# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from page.star_page import StarPage
from page.task_page import TaskPage
from page.task_properties_page import TaskPropertiesPage
from page.welcome_page import WelcomePage
from utils import constants


class TestTask:

    def test_create_task(self, open_app, create_task):
        wp = WelcomePage(open_app)
        wp.skip_welcome()
        task_title = create_task
        tp = TaskPage(open_app)
        tp.add_task(task_title=task_title)
        assert task_title in tp.get_all_task_names(), f"{task_title} is not in the list."

    def test_star_task(self, open_app, create_task):
        wp = WelcomePage(open_app)
        wp.skip_welcome()
        sp = StarPage(open_app)
        task_title = create_task
        tp = TaskPage(open_app)
        tp.add_task(task_title=task_title)
        tp.star_task(task_title=task_title)
        sp.click_on_starred_tasks()
        assert task_title in sp.get_all_starred_task_titles(tp), f"The starred task {task_title} is not in the list."

    def test_mark_done_task(self, open_app, create_task):
        wp = WelcomePage(open_app)
        wp.skip_welcome()
        task_title = create_task
        tp = TaskPage(open_app)
        tp.add_task(task_title)
        tp.done_task(task_title=task_title)
        assert tp.get_done_ui_message_text() == constants.ui_lbl_task_done
        assert tp.is_task_done(task_title=task_title), f"The completed task {task_title} is not in the list."

    def test_remove_task(self, open_app, create_task):
        wp = WelcomePage(open_app)
        wp.skip_welcome()
        tp = TaskPage(open_app)
        tpp = TaskPropertiesPage(open_app)
        task_title = create_task
        tp.add_task(task_title)
        tp.click_properties_task(task_title=task_title)
        tpp.delete_task()
        assert tpp.get_delete_ui_message_text() == constants.ui_lbl_task_deleted


