import requests_mock

from ohdear.ohdear import OhDear

ohdear = OhDear("abcdefghijklmnopqrstuvwxyz123457890")


def test_enables_check():
    with requests_mock.Mocker() as m:
        m.post(
            url="https://ohdear.app/api/checks/123/enable",
            json={"id": 405, "type": "uptime", "enabled": True},
        )
        status = ohdear.checks.enable(123)

        assert type(status) == bool
        assert status is True


def test_disables_check():
    with requests_mock.Mocker() as m:
        m.post(
            url="https://ohdear.app/api/checks/123/disable",
            json={"id": 405, "type": "uptime", "enabled": False},
        )
        status = ohdear.checks.disable(123)

        assert type(status) == bool
        assert status is False
