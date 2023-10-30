from trf.helper.base import BaseClass


class JfCe(BaseClass):
    url_base = "https://www.jfce.jus.br/consultaProcessual/cons_proca.asp"

    def __init__(self, headless: bool = False, driver_name: str = "JfCe"):
        super().__init__(headless, driver_name)
        self.driver.get(self.url_base)

    def execute(self) -> None:
        pass

    def find_cpf_input(self, cpf: str) -> None:
        id = "NumDocPess"
        self.driver.find_by_element("id", id, "send_keys", cpf)

    def click_pesquisar(self) -> None:
        id = "Pesquisar"
        self.driver.find_by_element("id", id, "click")

    def get_content_page(self) -> str:
        _class = "link-preto"
        return self.driver.find_by_element("class name", _class, "text")

    def get_len_process(self) -> int:
        _class = """textarea_1"""
        return self.driver.find_by_element("class name", _class, "text")
