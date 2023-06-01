import sys
import pytest

from sample_auth import create_app
from sample_auth.ext.auth import create_user, delete_user
from sample_auth.ext.commands import populate_db
from sample_auth.ext.database import db


@pytest.fixture(scope="session")
def app():
    app = create_app(FORCE_ENV_FOR_DYNACONF="testing")
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture(scope="session")
def products(app):
    with app.app_context():
        return populate_db()


@pytest.fixture(scope="session")
def admin_user(app):
    with app.app_context():
        admin_user = create_user(username="admin", password="asdf")
        yield admin_user
        delete_user(admin_user.username)


# each test runs on cwd to its temp dir
@pytest.fixture(autouse=True)
def go_to_tmpdir(request):
    # Get the fixture dynamically by its name.
    tmpdir = request.getfixturevalue("tmpdir")
    # ensure local test created packages can be imported
    sys.path.insert(0, str(tmpdir))
    # Chdir only for the duration of the test.
    with tmpdir.as_cwd():
        yield
