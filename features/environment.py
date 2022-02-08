import time


# capture screenshot of failed tests
def after_step(context, step):
    if step.status == 'failed':
        step_name = step.name
        context.driver.save_screenshot('C:/Repos/behaveTestExample/features/screenshots/failed-' + step_name + '.png')
