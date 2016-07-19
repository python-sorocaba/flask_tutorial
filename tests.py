import pytest


@pytest.mark.usefixtures('client_class')
class TestCore:

    @pytest.fixture
    def app(self):
        from app import app
        return app

    def test_get_home(self):
        response = self.client.get("/")
        assert response.data.decode('utf-8') == '<h1>Hello world!</h1>'
        assert response.status_code == 200

    def test_get_name(self):
        response = self.client.get("/Rafael")
        assert response.data.decode('utf-8') == '<h1>Hello Rafael!</h1>'
        assert response.status_code == 200
