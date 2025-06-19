import pytest


@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOSE] отправляем данные в сервиис аналитики")


@pytest.fixture(scope="session")
def settings():
    print("[SESSION] инициализируем настройки автотестов")


@pytest.fixture(scope="class")
def user():
    print("[CLASS] создаем данные пользователя один раз на тестовый класс")


@pytest.fixture(scope="function")
def browser():
    print("[FUNCTION] открываем браузер на каждый автотест")


class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        ...

    def test_user_can_create_course(self, settings, user, browser):
        ...


class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        ...
