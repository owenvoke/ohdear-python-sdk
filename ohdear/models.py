from datetime import datetime
from typing import TypedDict, Optional


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
