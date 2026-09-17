from pathlib import Path

from streamlit.testing.v1 import AppTest

APP = str(Path(__file__).resolve().parents[1] / "app" / "streamlit_app.py")


def run_app() -> AppTest:
    at = AppTest.from_file(APP, default_timeout=60)
    at.run()
    assert not at.exception, at.exception
    return at


def test_app_loads_and_flags_challenge_file():
    at = run_app()
    assert any("NÃO APTO" in e.value for e in at.error)
    assert len(at.tabs) == 4


def test_every_dimension_renders_without_error():
    at = run_app()
    select = at.selectbox[0]
    for option in select.options:
        select.set_value(option).run()
        assert not at.exception, (option, at.exception)


def test_incomplete_contract_is_blocked():
    at = run_app()
    at.button[0].click().run()  # formulário vazio
    assert any("BLOQUEADO" in e.value for e in at.error)


def test_example_experiment_gets_a_decision():
    at = run_app()
    assert any("Sugestão" in m.value for m in at.markdown)
