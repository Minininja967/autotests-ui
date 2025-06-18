import pytest


@pytest.mark.xfail(reason="Найден баг из-за которого падает тест")
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail(reason="Баг исправлен, но на тест все еще висит маркировка xfail")
def test_without_bug():
    ...
