import pytest

from tvseries.core.models import TVSerie
from tvseries.config import TestConfig


@pytest.mark.usefixtures('client_class')
class TestCore:

    @pytest.fixture
    def app(self):
        from tvseries import create_app
        app = create_app(TestConfig)
        return app

    def test_get_home(self, db):
        response = self.client.get("/")
        assert '<div class="banner">' in response.data.decode('utf-8')
        assert response.status_code == 200

    def test_get_add_status_code(self):
        response = self.client.get("/add")
        assert response.status_code == 200

    def test_get_add_content(self):
        response = self.client.get("/add")
        expected = (
            'name="serie-name" id="id_serie-name"',
            'name="serie-description" id="id_serie-description"',
            'name="serie-author" id="id_serie-author"',
            'name="serie-episodies_number" id="id_serie-episodies_number"',
        )
        for field in expected:
            assert field in response.data.decode('utf-8')

    def test_post_add(self, db):
        response = self.client.post("/add", data={
            "serie-name": "Game of Thrones",
            "serie-author": "George R.R. Martin",
            "serie-description": "Teste",
        })
        result = TVSerie.query.filter(TVSerie.name == 'Game of Thrones')
        assert response.status_code == 302 and result.count() == 1

    def test_navbar(self, db):
        response = self.client.get("/")
        assert ('<nav class="navbar navbar-default"' in
                response.data.decode('utf-8'))
        assert response.status_code == 200

    @pytest.fixture
    def db(self, app, request):
        from tvseries.ext import db as db_test

        def teardown():
            db_test.drop_all()

        db_test.app = app
        db_test.create_all()

        request.addfinalizer(teardown)
        return db_test

    def test_insert_on_model_tvserie(self, db):
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
        serie = TVSerie(name="Game of Thrones",
                        description=description,
                        author="George R.R. Martin")
        db.session.add(serie)
        db.session.commit()
        assert TVSerie.query.count() == 1

    def test_repr_on_model_tvserie(self, db):
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
        serie = TVSerie(name="Game of Thrones",
                        description=description,
                        author="George R.R. Martin")
        assert repr(serie) == (
            "TVSerie(id=None, name='Game of Thrones', "
            "description='Há muito t...', episodies_number=None)"
        )
