from trf.helper.driver import Driver
import pytest


def test_called_once() -> None:
    dr = Driver()
    dr = Driver()
    assert dr is not None
    assert isinstance(dr, Driver)
    assert dr() is Driver().driver
    del dr


def test_get_google_page() -> None:
    dr = Driver()
    dr().get("https://www.google.com")
    assert "Google" == dr().title
    del dr
