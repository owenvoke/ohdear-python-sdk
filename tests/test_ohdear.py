from ohdear import OhDear
import requests_mock

from ohdear.models import Site

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