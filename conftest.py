from fixture.application import Application
import pytest


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    fixture.session.login(login="admin", password="secret")

    def fin():
        fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture
