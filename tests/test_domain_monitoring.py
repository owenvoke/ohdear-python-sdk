import requests_mock

from ohdear import OhDear

ohdear = OhDear("abcdefghijklmnopqrstuvwxyz123457890")


def test_broken_links():
    with requests_mock.Mocker() as m:
        m.get(
            url="https://ohdear.app/api/sites/123/domain",
            json={
                "expires_at": "2028-09-14 04:00:00",
                "registered_at": "1997-09-15 04:00:00",
                "last_changed_at": "2019-09-09 15:39:04",
                "last_updated_in_rdap_db_at": "2022-06-11 00:32:59",
                "domain_statuses": {
                    "client delete prohibited": True,
                    "client transfer prohibited": True,
                    "client update prohibited": True,
                    "server delete prohibited": True,
                    "server transfer prohibited": True,
                    "server update prohibited": True,
                },
                "rdap_domain_response": {
                    "links": [
                        {
                            "rel": "self",
                            "href": "https:\\/\\/rdap.verisign.com\\/com\\/v1\\/domain\\/GOOGLE.COM",
                            "type": "application\\/rdap+json",
                            "value": "https:\\/\\/rdap.verisign.com\\/com\\/v1\\/domain\\/GOOGLE.COM",
                        },
                        {
                            "rel": "related",
                            "href": "https:\\/\\/rdap.markmonitor.com\\/rdap\\/domain\\/GOOGLE.COM",
                            "type": "application\\/rdap+json",
                            "value": "https:\\/\\/rdap.markmonitor.com\\/rdap\\/domain\\/GOOGLE.COM",
                        },
                    ],
                    "events": [
                        {
                            "eventDate": "1997-09-15T04:00:00Z",
                            "eventAction": "registration",
                        },
                        {
                            "eventDate": "2028-09-14T04:00:00Z",
                            "eventAction": "expiration",
                        },
                        {
                            "eventDate": "2019-09-09T15:39:04Z",
                            "eventAction": "last changed",
                        },
                        {
                            "eventDate": "2022-06-11T00:32:59Z",
                            "eventAction": "last update of RDAP database",
                        },
                    ],
                    "handle": "2138514_DOMAIN_COM-VRSN",
                    "status": [
                        "client delete prohibited",
                        "client transfer prohibited",
                        "client update prohibited",
                        "server delete prohibited",
                        "server transfer prohibited",
                        "server update prohibited",
                    ],
                    "ldhName": "GOOGLE.COM",
                    "notices": [
                        {
                            "links": [
                                {
                                    "href": "https:\\/\\/www.verisign.com\\/domain-names\\/registration-data-access-protocol\\/terms-service\\/index.xhtml",
                                    "type": "text\\/html",
                                }
                            ],
                            "title": "Terms of Use",
                            "description": ["Service subject to Terms of Use."],
                        },
                        {
                            "links": [
                                {
                                    "href": "https:\\/\\/icann.org\\/epp",
                                    "type": "text\\/html",
                                }
                            ],
                            "title": "Status Codes",
                            "description": [
                                "For more information on domain status codes, please visit https:\\/\\/icann.org\\/epp"
                            ],
                        },
                        {
                            "links": [
                                {
                                    "href": "https:\\/\\/icann.org\\/wicf",
                                    "type": "text\\/html",
                                }
                            ],
                            "title": "RDDS Inaccuracy Complaint Form",
                            "description": [
                                "URL of the ICANN RDDS Inaccuracy Complaint Form: https:\\/\\/icann.org\\/wicf"
                            ],
                        },
                    ],
                    "entities": [
                        {
                            "roles": ["registrar"],
                            "handle": "292",
                            "entities": [
                                {
                                    "roles": ["abuse"],
                                    "vcardArray": [
                                        "vcard",
                                        [
                                            ["version", [], "text", "4.0"],
                                            ["fn", [], "text", ""],
                                            [
                                                "tel",
                                                {"type": "voice"},
                                                "uri",
                                                "tel:+1.2086851750",
                                            ],
                                            [
                                                "email",
                                                [],
                                                "text",
                                                "abusecomplaints@markmonitor.com",
                                            ],
                                        ],
                                    ],
                                    "objectClassName": "entity",
                                }
                            ],
                            "publicIds": [
                                {"type": "IANA Registrar ID", "identifier": "292"}
                            ],
                            "vcardArray": [
                                "vcard",
                                [
                                    ["version", [], "text", "4.0"],
                                    ["fn", [], "text", "MarkMonitor Inc."],
                                ],
                            ],
                            "objectClassName": "entity",
                        }
                    ],
                    "secureDNS": {"delegationSigned": False},
                    "nameservers": [
                        {"ldhName": "NS1.GOOGLE.COM", "objectClassName": "nameserver"},
                        {"ldhName": "NS2.GOOGLE.COM", "objectClassName": "nameserver"},
                        {"ldhName": "NS3.GOOGLE.COM", "objectClassName": "nameserver"},
                        {"ldhName": "NS4.GOOGLE.COM", "objectClassName": "nameserver"},
                    ],
                    "objectClassName": "domain",
                    "rdapConformance": [
                        "rdap_level_0",
                        "icann_rdap_technical_implementation_guide_0",
                        "icann_rdap_response_profile_0",
                    ],
                },
                "created_at": "2022-06-10 20:33:06",
            },
        )

        domain = ohdear.domain_monitoring.domain(123)

        assert type(domain) == dict
        assert domain.get("expires_at") == "2028-09-14 04:00:00"
        assert domain.get("registered_at") == "1997-09-15 04:00:00"
        assert domain.get("last_changed_at") == "2019-09-09 15:39:04"
        assert domain.get("last_updated_in_rdap_db_at") == "2022-06-11 00:32:59"
        assert domain.get("domain_statuses").get("client delete prohibited") is True
        assert type(domain.get("rdap_domain_response").get("links")) == list
        assert domain.get("created_at") == "2022-06-10 20:33:06"
