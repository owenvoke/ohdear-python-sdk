import requests
from typing import cast
from ohdear.types import UserInfo, SitesCollection, Site, CronChecksCollection, BrokenLinksCollection

TIMEOUT = 3
API_BASE_URI = 'https://ohdear.app/api'


class OhDearException(RuntimeError):
    """Unknown error"""


class UnauthorizedException(OhDearException):
    """Unauthorized"""


class NotFoundException(OhDearException):
    """Not Found"""


class OhDear:
    def __init__(self, api_token: str, base_uri: str = API_BASE_URI) -> None:
        self.api_token: str = api_token
        self.base_uri: str = base_uri
        self.headers: dict = {
            'Authorization': 'Bearer {0}'.format(self.api_token)
        }

        self.broken_links: BrokenLinks = BrokenLinks(self)
        self.checks: Checks = Checks(self)
        self.cron_checks: CronChecks = CronChecks(self)
        self.sites: Sites = Sites(self)

    def authenticated(self) -> bool:
        try:
            return self.me().get('id') is not None
        except UnauthorizedException:
            return False

    def me(self) -> UserInfo:
        return cast(UserInfo, self.get('/me'))

    def get(self, url: str):
        return self.__request('GET', url)

    def post(self, url: str, data: dict = None):
        return self.__request('POST', url, data)

    def __request(self, method: str, url: str, params: dict = None):
        if params is None:
            params = {}

        if method == 'GET':
            response = requests.get(self.base_uri + url, params=params, headers=self.headers)
        elif method == 'POST':
            response = requests.post(self.base_uri + url, json=params, headers=self.headers)
        else:
            raise RuntimeError('Invalid request method provided')

        if response.status_code == 401:
            raise UnauthorizedException(response.json().get('error'))
        if response.status_code == 404:
            raise NotFoundException(response.json().get('error'))
        if response.status_code >= 400:
            raise OhDearException(response.json().get('error') or 'Unknown error')
        return response.json()


class BrokenLinks:
    def __init__(self, client: OhDear):
        self.client = client

    def show(self, site_id: int) -> BrokenLinksCollection:
        return cast(BrokenLinksCollection, self.client.get(f'/broken-links/{site_id}'))


class Checks:
    def __init__(self, client: OhDear):
        self.client = client

    def enable(self, check_id: int) -> bool:
        return self.client.post(f'/checks/{check_id}/enable').get('enabled')

    def disable(self, check_id: int) -> bool:
        return self.client.post(f'/checks/{check_id}/disable').get('enabled')


class CronChecks:
    def __init__(self, client: OhDear):
        self.client = client

    def show(self, site_id: int) -> CronChecksCollection:
        return cast(CronChecksCollection, self.client.get(f'/sites/{site_id}/cron-checks'))


class Sites:
    def __init__(self, client: OhDear):
        self.client = client

    def all(self) -> SitesCollection:
        return cast(SitesCollection, self.client.get('/sites'))

    def show(self, site_id: int) -> Site:
        return cast(Site, self.client.get(f'/sites/{site_id}'))
