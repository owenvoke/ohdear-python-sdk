import pytest
import requests_mock
from ohdear import OhDear
from ohdear.ohdear import NotFoundException

ohdear = OhDear("abcdefghijklmnopqrstuvwxyz123457890")


def test_me():
    with requests_mock.Mocker() as m:
        m.get(
            url='https://ohdear.app/api/me',
            json={
                "id": 1,
                "name": "Owen Voke",
                "email": "development@voke.dev",
                "photo_url": "https://example.org/profile-1.jpg",
                "teams": [
                    {
                        "id": 1,
                        "name": "Dream Team"
                    }
                ]
            }
        )
        me = ohdear.me()

        assert type(me) == dict
        assert me.get('id') == 1
        assert me.get('name') == 'Owen Voke'
        assert me.get('email') == 'development@voke.dev'
        assert me.get('photo_url') == 'https://example.org/profile-1.jpg'
        assert me.get('teams')[0].get('id') == 1
        assert me.get('teams')[0].get('name') == 'Dream Team'


def test_authenticated():
    with requests_mock.Mocker() as m:
        m.get(
            url='https://ohdear.app/api/me',
            json={
                "id": 1,
                "name": "Owen Voke",
                "email": "development@voke.dev",
                "photo_url": "https://example.org/profile-1.jpg",
                "teams": [
                    {
                        "id": 1,
                        "name": "Dream Team"
                    }
                ]
            }
        )
        me = ohdear.authenticated()

        assert type(me) == bool
        assert me is True


def test_not_authenticated():
    with requests_mock.Mocker() as m:
        m.get(
            url='https://ohdear.app/api/me',
            status_code=401,
            json={"error": "Unauthorized."}
        )
        me = ohdear.authenticated()

        assert type(me) == bool
        assert me is False


def test_sites_all():
    with requests_mock.Mocker() as m:
        m.get(
            url='https://ohdear.app/api/sites',
            json={
                "data": [
                    {
                        "id": 1,
                        "url": "https://yoursite.tld",
                        "sort_url": "yoursite.tld",
                        "label": "your-site",
                        "team_id": 1,
                        "group_name": None,
                        "latest_run_date": "2019-09-16 07:29:02",
                        "summarized_check_result": "succeeded",
                        "created_at": "20171106 07:40:49",
                        "updated_at": "20171106 07:40:49",
                        "checks": [
                            {
                                "id": 100,
                                "type": "uptime",
                                "label": "Uptime",
                                "enabled": True,
                                "latest_run_ended_at": "2019-09-16 07:29:02",
                                "latest_run_result": "succeeded",
                                "summary": "Up"
                            }
                        ]
                    }
                ]
            }
        )
        all_sites = ohdear.sites.all()

        assert type(all_sites) == dict
        assert type(all_sites.get('data')) == list
        assert type(all_sites.get('data')[0]) == dict
        assert type(all_sites.get('data')[0].get('id')) == int


def test_sites_single():
    with requests_mock.Mocker() as m:
        m.get(
            url='https://ohdear.app/api/sites/12345',
            json={
                "id": 1,
                "url": "https://yoursite.tld",
                "sort_url": "yoursite.tld",
                "label": "your-site",
                "team_id": 1,
                "group_name": None,
                "latest_run_date": "2019-09-16 07:29:02",
                "summarized_check_result": "succeeded",
                "created_at": "20171106 07:40:49",
                "updated_at": "20171106 07:40:49",
                "checks": [
                    {
                        "id": 100,
                        "type": "uptime",
                        "label": "Uptime",
                        "enabled": True,
                        "latest_run_ended_at": "2019-09-16 07:29:02",
                        "latest_run_result": "succeeded",
                        "summary": "Up"
                    }
                ]
            }
        )
        site = ohdear.sites.show(12345)

        assert type(site) == dict
        assert type(site.get('id')) == int


def test_sites_single_for_another_user():
    with requests_mock.Mocker() as m:
        m.get(
            url='https://ohdear.app/api/sites/1',
            status_code=404,
            json={
                "message": "No query results for model [no-model]."
            }
        )
        with pytest.raises(NotFoundException):
            assert ohdear.sites.show(1)


def test_enables_check():
    with requests_mock.Mocker() as m:
        m.post(
            url='https://ohdear.app/api/checks/123/enable',
            json={
                "id": 405,
                "type": "uptime",
                "enabled": True
            }
        )
        status = ohdear.checks.enable(123)

        assert type(status) == bool
        assert status is True


def test_disables_check():
    with requests_mock.Mocker() as m:
        m.post(
            url='https://ohdear.app/api/checks/123/disable',
            json={
                "id": 405,
                "type": "uptime",
                "enabled": False
            }
        )
        status = ohdear.checks.disable(123)

        assert type(status) == bool
        assert status is False


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
