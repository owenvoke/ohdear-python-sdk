import pytest
import requests_mock

from ohdear import NotFoundException, OhDear

ohdear = OhDear("abcdefghijklmnopqrstuvwxyz123457890")


def test_sites_all():
    with requests_mock.Mocker() as m:
        m.get(
            url="https://ohdear.app/api/sites",
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
                                "summary": "Up",
                            }
                        ],
                    }
                ]
            },
        )
        all_sites = ohdear.sites.all()

        assert type(all_sites) == dict
        assert type(all_sites.get("data")) == list
        assert type(all_sites.get("data")[0]) == dict
        assert type(all_sites.get("data")[0].get("id")) == int


def test_sites_single():
    with requests_mock.Mocker() as m:
        m.get(
            url="https://ohdear.app/api/sites/12345",
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
                        "summary": "Up",
                    }
                ],
            },
        )
        site = ohdear.sites.show(12345)

        assert type(site) == dict
        assert type(site.get("id")) == int


def test_sites_single_for_a_non_existent_site():
    with requests_mock.Mocker() as m:
        m.get(
            url="https://ohdear.app/api/sites/1",
            status_code=404,
            json={"message": "No query results for model [no-model]."},
        )
        with pytest.raises(NotFoundException):
            assert ohdear.sites.show(1)
