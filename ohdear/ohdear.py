import requests
from typing import cast
from ohdear.models import UserInfo, SitesCollection, Site

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

        self.sites: Sites = Sites(self)

    def get(self, url: str):
        response = requests.get(self.base_uri + url, headers=self.headers)
        if response.status_code == 401:
            raise UnauthorizedException(response.json().get('error'))
        if response.status_code == 404:
            raise NotFoundException(response.json().get('error'))
        if response.status_code >= 400:
            raise OhDearException(response.json().get('error') or 'Unknown error')
        return response.json()

    def authenticated(self) -> bool:
        try:
            return self.me().get('id') is not None
        except UnauthorizedException:
            return False

    def me(self) -> UserInfo:
        return cast(UserInfo, self.get('/me'))


class Sites:
    def __init__(self, client: OhDear):
        self.client = client

    def all(self) -> SitesCollection:
        return cast(SitesCollection, self.client.get('/sites'))

    def show(self, site_id: int) -> Site:
        return cast(Site, self.client.get(f'/sites/{str(site_id)}'))
