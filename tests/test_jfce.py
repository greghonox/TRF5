from trf.helper.jfce import JfCe
from trf.helper.driver import Driver


def test_called_once() -> None:
    dr = JfCe(driver_name="Test")
    assert isinstance(dr.driver, Driver)
    del dr


def test_get() -> None:
    cpfs = [
        "00387711368",
        "12080969315",
        "00114812349",
        "19478771353",
        "05214122349",
        "01822250544",
        "01266136215",
        "01821440382",
        "01886169349",
        "00358487315",
        "00387711368",
    ]
    dr = JfCe()
    dr.find_cpf_input(cpfs[0])
    dr.click_pesquisar()
    process = dr.get_len_process()
    content = dr.get_content_page()
    del dr
