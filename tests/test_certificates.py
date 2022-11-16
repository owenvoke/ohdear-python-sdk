import requests_mock

from ohdear.ohdear import OhDear

ohdear = OhDear("abcdefghijklmnopqrstuvwxyz123457890")


def test_enables_check():
    with requests_mock.Mocker() as m:
        m.get(
            url="https://ohdear.app/api/certificate-health/123",
            json={
                "certificate_details": {
                    "issuer": "Let's Encrypt Authority X3",
                    "valid_from": "2019-09-10 15:16:01",
                    "valid_until": "2019-12-09 15:16:01",
                },
                "certificate_checks": [
                    {
                        "type": "notFound",
                        "label": "Certificate present",
                        "passed": True,
                    },
                    {
                        "type": "expiresSoon",
                        "label": "Will not expire in the next 14 days",
                        "passed": True,
                    },
                    {
                        "type": "invalidChain",
                        "label": "Has a valid chain",
                        "passed": True,
                    },
                    {
                        "type": "coversWrongDomain",
                        "label": "Covers the right domain",
                        "passed": True,
                    },
                    {
                        "type": "doesNotConnectWithRootCertificate",
                        "label": "Connects with a root certificate",
                        "passed": True,
                    },
                    {
                        "type": "notYetActive",
                        "label": "Is currently active",
                        "passed": True,
                    },
                    {
                        "type": "isSelfSigned",
                        "label": "Is not self signed",
                        "passed": True,
                    },
                    {
                        "type": "usesInvalidHash",
                        "label": "Uses valid hash",
                        "passed": True,
                    },
                    {"type": "hasExpired", "label": "Has not expired", "passed": True},
                    {
                        "type": "hasChanged",
                        "label": "Unchanged since last checked",
                        "passed": True,
                    },
                ],
                "certificate_chain_issuers": [
                    "US, Let's Encrypt, Let's Encrypt Authority X3",
                    "Digital Signature Trust Co., DST Root CA X3",
                ],
            },
        )
        certificate = ohdear.certificates.show(123)

        assert type(certificate) == dict
        assert type(certificate.get("certificate_details")) is dict
        assert (
            certificate.get("certificate_details").get("issuer")
            == "Let's Encrypt Authority X3"
        )
        assert (
            certificate.get("certificate_details").get("valid_from")
            == "2019-09-10 15:16:01"
        )
        assert (
            certificate.get("certificate_details").get("valid_until")
            == "2019-12-09 15:16:01"
        )
        assert type(certificate.get("certificate_checks")) is list
        assert certificate.get("certificate_checks")[0].get("type") == "notFound"
        assert (
            certificate.get("certificate_checks")[0].get("label")
            == "Certificate present"
        )
        assert certificate.get("certificate_checks")[0].get("passed") is True
        assert type(certificate.get("certificate_chain_issuers")) is list
        assert (
            certificate.get("certificate_chain_issuers")[0]
            == "US, Let's Encrypt, Let's Encrypt Authority X3"
        )
