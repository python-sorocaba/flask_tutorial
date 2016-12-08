from datetime import date

import pytest

from tvseries.core.forms import TVSerieForm
from tvseries.config import TestConfig


@pytest.mark.usefixtures('client_class')
class TestCoreForms:

    @pytest.fixture
    def app(self):
        from tvseries import create_app
        app = create_app(TestConfig)
        return app

    def test_form_valid(self):
        description = (
            "Há muito tempo, em um tempo esquecido, uma força "
            "destruiu o equilíbrio das estações. Em uma terra "
            "onde os verões podem durar vários anos e o inverno "
            "toda uma vida, as reivindicações e as forças sobrenaturais "
            "correm as portas do Reino dos Sete Reinos. A irmandade "
            "da Patrulha da Noite busca proteger o reino de cada "
            "criatura que pode vir de lá da Muralha, mas já não tem "
            "os recursos necessários para garantir a segurança de "
            "todos. Depois de um verão de dez anos, um inverno "
            "rigoroso promete chegar com um futuro mais sombrio. "
            "Enquanto isso, conspirações e rivalidades correm no jogo "
            "político pela disputa do Trono de Ferro, o símbolo do "
            "poder absoluto."
        )
        form_serie = TVSerieForm(name="Game of Thrones",
                                 description=description,
                                 author="George R.R. Martin",
                                 year=date(2011, 1, 1))
        assert form_serie.validate()
