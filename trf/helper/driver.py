from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import logging


class Driver:
    __instance = None

    def __new__(cls, headless=False):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.instance_log()
            ChromeDriverManager().install()
            chrome_options = Options()
            if headless:
                chrome_options.add_argument("--headless")
            cls.__instance.logger.info("Driver instance created")
            cls.__instance.driver = webdriver.Chrome(options=chrome_options)
        else:
            cls.__instance.logger.info("client are try instance created")

        return cls.__instance

    def __call__(self):
        return self.__instance.driver

    @classmethod
    def instance_log(cls) -> None:
        cls.__instance.logger = logging.getLogger("Driver")
        cls.__instance.logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        cls.__instance.logger.addHandler(console_handler)
        cls.__instance.logger.info("Driver instance created")

    def __del__(self):
        self.__instance.logger.info("closed driver")
        self.__instance.driver.quit()
