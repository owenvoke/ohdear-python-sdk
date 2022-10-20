import requests

TIMEOUT = 3
API_BASE_URI = 'https://ohdear.app/api'


class OhDearException(RuntimeError):
    """Unknown error"""


class UnauthorizedException(OhDearException):
    """Unauthorized"""


class OhDear:
    def __init__(self, api_token: str, base_uri: str = API_BASE_URI) -> None:
        self.api_token = api_token
        self.base_uri = base_uri
        self.headers = {
            'Authorization': 'Bearer {0}'.format(self.api_token)
        }

        self.sites = Sites(self)

    def get(self, url: str):
        response = requests.get(self.base_uri + url, headers=self.headers)
        if response.status_code == 401:
            raise UnauthorizedException(response.json().get('error'))
        if response.status_code >= 400:
            raise OhDearException(response.json().get('error') or 'Unknown error')
        return response.json()

    def authenticated(self) -> bool:
        try:
            return self.me().get('id') is not None
        except UnauthorizedException:
            return False

    def me(self):
        return self.get('/me')


class Sites:
    def __init__(self, client: OhDear):
        self.client = client

    def all(self):
        return self.client.get('/sites').get('data')

    def show(self, site_id: int):
        return self.client.get('/sites/{0}'.format(str(site_id)))
