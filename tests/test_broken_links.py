import requests_mock

from ohdear import OhDear

ohdear = OhDear("abcdefghijklmnopqrstuvwxyz123457890")


def test_broken_links():
    with requests_mock.Mocker() as m:
        m.get(
            url="https://ohdear.app/api/broken-links/123",
            json={
                "data": [
                    {
                        "crawled_url": "https://example.com/broken",
                        "status_code": 404,
                        "found_on_url": "https://example.com",
                    }
                ]
            },
        )
        cron_checks = ohdear.broken_links.show(123)

        assert type(cron_checks) == dict
        assert type(cron_checks.get("data")) == list
        assert type(cron_checks.get("data")[0]) == dict
        assert type(cron_checks.get("data")[0].get("crawled_url")) == str
        assert type(cron_checks.get("data")[0].get("status_code")) == int
        assert type(cron_checks.get("data")[0].get("found_on_url")) == str
