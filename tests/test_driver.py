import pytest
from selenium.common.exceptions import WebDriverException

from trf.helper.driver import Driver


def test_called_once() -> None:
    dr = Driver()
    dr = Driver()
    assert dr is not None
    assert isinstance(dr, Driver)
    assert dr() is Driver().driver
    del dr


def test_get_google_page() -> None:
    dr = Driver()
    dr.get('https://www.google.com')
    assert 'Google' == dr().title
    del dr


def test_get_google_headless() -> None:
    dr = Driver(headless=True)
    dr.get('https://www.google.com')
    assert 'Google' == dr().title
    del dr


def test_get_not_found_page() -> None:
    dr = Driver()
    with pytest.raises(WebDriverException):
        dr.get('https://xxxx.com')
