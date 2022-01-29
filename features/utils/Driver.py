from selenium import webdriver


def launch_browser(context, browser):
    if browser == "firefox":
        context.driver = webdriver.Firefox(executable_path=r'C:\Repos\pythonTestChallenge\drivers\geckodriver.exe')
        context.driver.implicitly_wait(10)
    else:
        context.driver = webdriver.Chrome(executable_path=r'C:\Repos\pythonTestChallenge\drivers\chromedriver.exe')
        context.driver.implicitly_wait(10)


def navigate_to_url(context, url):
    context.driver.get(url)