import requests_mock

from ohdear import OhDear

ohdear = OhDear("abcdefghijklmnopqrstuvwxyz123457890")


def test_me():
    with requests_mock.Mocker() as m:
        m.get(
            url="https://ohdear.app/api/me",
            json={
                "id": 1,
                "name": "Owen Voke",
                "email": "development@voke.dev",
                "photo_url": "https://example.org/profile-1.jpg",
                "teams": [{"id": 1, "name": "Dream Team"}],
            },
        )
        me = ohdear.me()

        assert type(me) == dict
        assert me.get("id") == 1
        assert me.get("name") == "Owen Voke"
        assert me.get("email") == "development@voke.dev"
        assert me.get("photo_url") == "https://example.org/profile-1.jpg"
        assert me.get("teams")[0].get("id") == 1
        assert me.get("teams")[0].get("name") == "Dream Team"


def test_authenticated():
    with requests_mock.Mocker() as m:
        m.get(
            url="https://ohdear.app/api/me",
            json={
                "id": 1,
                "name": "Owen Voke",
                "email": "development@voke.dev",
                "photo_url": "https://example.org/profile-1.jpg",
                "teams": [{"id": 1, "name": "Dream Team"}],
            },
        )
        me = ohdear.authenticated()

        assert type(me) == bool
        assert me is True


def test_not_authenticated():
    with requests_mock.Mocker() as m:
        m.get(
            url="https://ohdear.app/api/me",
            status_code=401,
            json={"error": "Unauthorized."},
        )
        me = ohdear.authenticated()

        assert type(me) == bool
        assert me is False
