from selenium import webdriver


def launch_browser(context, browser):
    # TODO These drivers variables should be set as environment variables
    if browser == "firefox":
        context.driver = webdriver.Firefox(executable_path=r'C:\Repos\behaveTestExample\drivers\geckodriver.exe')
        context.driver.implicitly_wait(10)
    else:
        context.driver = webdriver.Chrome(executable_path=r'C:\Repos\behaveTestExample\drivers\chromedriver.exe')
        context.driver.implicitly_wait(10)


def navigate_to_url(context, url):
    context.driver.get(url)
