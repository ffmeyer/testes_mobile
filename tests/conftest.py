import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from faker import Faker

from page.welcome_page import WelcomePage


@pytest.fixture()
def load_appium_options():
    options = UiAutomator2Options()
    options.load_capabilities({
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": "com.google.android.apps.tasks",
        "appium:appActivity": "com.google.android.apps.tasks.ui.TaskListsActivity",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True
    })
    return options


@pytest.fixture()
def open_app(load_appium_options):
    options = load_appium_options
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.terminate_app('com.google.android.apps.tasks')
    driver.quit()


@pytest.fixture()
def create_task():
    fake = Faker()
    return f'{fake.lexify(text='?????????? task')}'
