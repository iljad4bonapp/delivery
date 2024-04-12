from hello_app import app


def test_root():
    response = app.test_client().get("/")
    assert response.status_code == 200


def test_about():
    response = app.test_client().get("/about")
    assert response.status_code == 308


def test_contact():
    response = app.test_client().get("/contact")
    assert response.status_code == 308


def test_hello():
    response = app.test_client().get("/hello/test")
    assert response.status_code == 200
    assert b"Hello there, test!" in response.data
