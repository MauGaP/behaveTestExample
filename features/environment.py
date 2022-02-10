# capture screenshot of failed tests
import os

import allure


def after_step(context, step):
    if step.status == 'failed':
        cwd = os.getcwd()
        step_name = step.name
        screenshot_name = cwd + '/features/screenshots/failed-' + step_name + '.png'
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name=screenshot_name, attachment_type=allure.attachment_type.PNG
        )
