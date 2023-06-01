from sample_auth.ext.auth import create_user, delete_user, verify_login
from sample_auth.models import User


def test_dynaconf_is_on_testing_env(app):
    assert app.config.current_env == "testing"


def test_create_user(app, admin_user):
    existing_user = admin_user
    assert existing_user


def test_verify_login(app):
    my_user = create_user(
        username="my_awesome_user", password="my_awesome_password"
    )
    assert verify_login(
        {"username": "my_awesome_user", "password": "my_awesome_password"}
    )
    assert not verify_login(
        {"username": "my_awesome_user", "password": "bad_password"}
    )
    assert not verify_login(
        {"username": "bad_user", "password": "my_awesome_password"}
    )
    assert not verify_login({"username": "my_awesome_user"})
    assert not verify_login({"password": "my_awesome_password"})

    delete_user(my_user.username)


def test_pw_storage_not_plaintext(app):
    my_user = create_user(
        username="my_awesome_user", password="my_awesome_password"
    )
    assert not (my_user.pwhash == "my_awesome_password")
    delete_user(my_user.username)
