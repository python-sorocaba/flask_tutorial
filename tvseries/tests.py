import pytest


@pytest.mark.usefixtures('client_class')
class TestCore:

    @pytest.fixture
    def app(self):
        from tvseries.core import app
        return app

    def test_get_home(self):
        response = self.client.get("/")
        assert '<h1>Hello world!</h1>' in response.data.decode('utf-8')
        assert response.status_code == 200

    def test_get_name(self):
        response = self.client.get("/Rafael")
        assert '<h1>Hello Rafael!</h1>' in response.data.decode('utf-8')
        assert response.status_code == 200

    def test_get_add(self):
        response = self.client.get("/add")
        assert ('<input type="text" name="serie-name" id="id_serie-name">' in
                response.data.decode('utf-8'))
        assert response.status_code == 200

    def test_post_add(self):
        response = self.client.post("/add", data={"serie-name": "Teste"})
        from tvseries.core import series
        assert series == ['Teste']
        assert response.status_code == 302
