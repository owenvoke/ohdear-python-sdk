import requests_mock

from ohdear.ohdear import OhDear

ohdear = OhDear("abcdefghijklmnopqrstuvwxyz123457890")


def test_enables_check():
    with requests_mock.Mocker() as m:
        m.get(
            url="https://ohdear.app/api/mixed-content/123",
            json={
                "data": [
                    {
                        "element_name": "img",
                        "mixed_content_url": "http://example.com/image.jpg",
                        "found_on_url": "https://example.com",
                    }
                ]
            },
        )
        mixed_contents = ohdear.mixed_contents.show(123)

        assert type(mixed_contents) == dict
        assert type(mixed_contents.get("data")) is list
        assert type(mixed_contents.get("data")[0]) is dict
        assert mixed_contents.get("data")[0].get("element_name") == "img"
        assert (
            mixed_contents.get("data")[0].get("mixed_content_url")
            == "http://example.com/image.jpg"
        )
        assert (
            mixed_contents.get("data")[0].get("found_on_url") == "https://example.com"
        )
