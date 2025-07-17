import pytest
from playwright.sync_api import Page, Playwright
from collections.abc import Generator
import allure
from pages.authentication.registrartion_page import RegistrationPage
from _pytest.fixtures import SubRequest


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Generator[Page, None, None]:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context.new_page()

    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    browser.close()

    allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email='test@test.com', username='test_user', password='test_password')
    registration_page.click_registration_button()

    context.storage_state(path='browser-state.json')

    browser.close()


@pytest.fixture
def chromium_page_with_state(
        request: SubRequest, initialize_browser_state, playwright: Playwright
) -> Generator[Page, None, None]:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context.new_page()

    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    browser.close()

