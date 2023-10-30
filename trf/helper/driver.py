import logging
from typing import Union, Literal
from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    WebDriverException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


BY_ELEMENT = Union[
    Literal["id"],
    Literal["xpath"],
    Literal["tag name"],
    Literal["link text"],
    Literal["class name"],
    Literal["css selector"],
    Literal["partial link text"],
]
BY = {
    "id": By.ID,
    "element": None,
    "xpath": By.XPATH,
    "tag name": By.TAG_NAME,
    "link text": By.LINK_TEXT,
    "class name": By.CLASS_NAME,
    "css selector": By.CSS_SELECTOR,
    "partial link text": By.PARTIAL_LINK_TEXT,
}

ACTIONS = Union[Literal["click"], Literal["send_keys"], Literal["text"]]


class Driver:
    __instance = None
    __driver_name = "Driver"

    def __new__(cls, headless: bool = False, driver_name: str = "Driver"):
        if cls.__instance is None:
            cls.__driver_name = driver_name
            cls.__instance = super().__new__(cls)
            cls.instance_log()
            ChromeDriverManager().install()
            chrome_options = Options()
            if headless:
                chrome_options.add_argument("--headless")
            cls.logger("Driver instance created")
            cls.__instance.driver = webdriver.Chrome(options=chrome_options)
        else:
            cls.logger("client are try instance created")

        return cls.__instance

    @classmethod
    def get(cls, url: str) -> None:
        cls.logger(f"get url: {url}", 1)
        try:
            cls.__instance.driver.get(url)
        except NoSuchElementException as error:
            cls.logger(f"Element exception {error}", 2)
            del cls.__instance

    @classmethod
    def find_by_element(
        cls,
        types: BY_ELEMENT,
        tag: str,
        action: ACTIONS,
        text_input: Union[str, None] = None,
    ) -> None:
        cls.logger(
            f"find element by '{types}' {tag} id: action: '{action}' text: '{text_input}'",
            0,
        )
        try:
            element = cls.__instance.driver.find_element(BY[types], tag)
            actions = {
                "click": element.click,
                "send_keys": lambda text: element.send_keys(text_input),
                "text": lambda: element.text,
            }

            if action == "text":
                return actions[action]()
            elif action == "click":
                return actions[action]()
            elif action == "send_keys":
                assert text_input, "text_input is required"
                return actions[action](text_input)
            elif action == "element":
                return element
            raise Exception("action not found")
        except WebDriverException as error:
            cls.logger(f"Exception found {error}", 2)
            del cls.__instance

    @classmethod
    def logger(cls, msg, type: int = 0) -> None:
        if type == 0:
            cls.__instance.logger.info(msg)
        if type == 1:
            cls.__instance.logger.warning(msg)
        if type == 2:
            cls.__instance.logger.error(msg)
        else:
            cls.__instance.logger.debug(msg)

    @classmethod
    def instance_log(cls) -> None:
        cls.__instance.logger = logging.getLogger(cls.__driver_name)
        cls.__instance.logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        cls.__instance.logger.addHandler(console_handler)
        cls.logger("Driver instance created")

    def __del__(self):
        self.__instance.logger.info("closed driver")
        self.__instance.driver.quit()
