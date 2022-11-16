from datetime import datetime
from typing import Optional, TypedDict


class Team(TypedDict):
    id: int
    name: str


class UserInfo(TypedDict):
    id: int
    name: str
    email: str
    photo_url: str
    teams: list[Team]


class Check(TypedDict):
    id: int
    type: str
    label: str
    enabled: bool
    latest_run_ended_at: datetime
    latest_run_result: str
    summary: str


class Site(TypedDict):
    id: int
    url: str
    sort_url: str
    friendly_name: Optional[str]
    label: str
    team_id: int
    latest_run_date: Optional[datetime]
    summarized_check_result: str
    uses_https: Optional[bool]
    checks: list[Check]
    broken_links_check_include_external_links: Optional[bool]
    broken_links_whitelisted_urls: Optional[list[str]]
    created_at: Optional[datetime]
    update_at: Optional[datetime]


class SitesCollection(TypedDict):
    data: list[Site]


class CronCheck(TypedDict):
    id: int
    uuid: str
    name: str
    type: str
    description: str
    frequency_in_minutes: str
    grace_time_in_minutes: str
    cron_expression: Optional[str]
    server_timezone: str
    ping_url: str
    created_at: datetime
    latest_result: str
    latest_ping_at: Optional[datetime]


class CronChecksCollection(TypedDict):
    data: list[CronCheck]


class BrokenLink(TypedDict):
    crawled_url: str
    status_code: int
    found_on_url: str


class BrokenLinksCollection(TypedDict):
    data: list[BrokenLink]


class CertificateDetails(TypedDict):
    issuer: str
    valid_from: datetime
    valid_until: datetime


class CertificateCheck(TypedDict):
    type: str
    label: str
    passed: bool


class CertificateHealth(TypedDict):
    certificate_details: CertificateDetails
    certificate_checks: list[CertificateCheck]
    certificate_chain_issuers: list[str]


class MixedContent(TypedDict):
    element_name: str
    mixed_content_url: str
    found_on_url: str


class MixedContentsCollection(TypedDict):
    data: list[MixedContent]
