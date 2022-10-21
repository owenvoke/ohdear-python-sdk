import requests_mock

from ohdear.ohdear import NotFoundException, OhDear

ohdear = OhDear("abcdefghijklmnopqrstuvwxyz123457890")


def test_cron_checks():
    with requests_mock.Mocker() as m:
        m.get(
            url='https://ohdear.app/api/sites/123/cron-checks',
            json={
                "data": [
                    {
                        "id": 123,
                        "uuid": "0d210b09",
                        "name": "cronjob number one",
                        "type": "simple",
                        "description": "a description goes here",
                        "frequency_in_minutes": 15,
                        "grace_time_in_minutes": 5,
                        "cron_expression": None,
                        "server_timezone": "Europe/Brussels",
                        "ping_url": "https://ping.ohdear.app/0d210b09",
                        "created_at": "2020-07-28 13:27:02",
                        "latest_result": "pingFinished",
                        "latest_ping_at": "2020-11-16 09:19:40"
                    }
                ]
            }
        )
        cron_checks = ohdear.cron_checks.show(123)

        assert type(cron_checks) == dict
        assert type(cron_checks.get('data')) == list
        assert type(cron_checks.get('data')[0]) == dict
        assert type(cron_checks.get('data')[0].get('id')) == int
