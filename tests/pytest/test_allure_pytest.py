import allure

@allure.step('Opening browser')
def open_browser():
    with allure.step('Get browser'):
        ...

    with allure.step('Start browser'):
        ...

@allure.step('Creating course with title "{title}"')
def create_course(title: str):
    ...

@allure.step('Closing browser')
def close_browser():
    ...

def test_feature():
    open_browser()
    create_course('Locust')
    create_course('Python')
    create_course('Playwright')
    close_browser()