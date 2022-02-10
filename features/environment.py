# capture screenshot of failed tests
import os


def after_step(context, step):
    cwd = os.getcwd()
    if step.status == 'failed':
        step_name = step.name
        context.driver.save_screenshot(cwd + '/features/screenshots/failed-' + step_name + '.png')
