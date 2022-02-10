import os

from selenium import webdriver


def launch_browser(context, browser):
    cwd = os.getcwd()
    if browser == "firefox":
        context.driver = webdriver.Firefox(executable_path=cwd + '\drivers\geckodriver.exe')
        context.driver.implicitly_wait(10)
    else:
        context.driver = webdriver.Chrome(executable_path=cwd + '\drivers\chromedriver.exe')
        context.driver.implicitly_wait(10)


def navigate_to_url(context, url):
    context.driver.get(url)
