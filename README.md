# Oh Dear Python

[![Latest Version on PyPi][ico-version]][link-pypi]
[![Software License][ico-license]](LICENSE.md)
[![Build Status][ico-github-actions]][link-github-actions]
[![Buy us a tree][ico-treeware-gifting]][link-treeware-gifting]

An SDK to easily work with the [Oh Dear API](https://ohdear.app/docs/integrations/the-oh-dear-api)

## Install

Via Pip

```shell
pip install ohdear-sdk
```

## Usage

```python
from ohdear import OhDear

ohdear = OhDear(api_token="your-token")

sites = ohdear.sites.all()
```

| Available Methods                 | Description                                                                                         |
|:----------------------------------|:----------------------------------------------------------------------------------------------------|
| `ohdear.me()`                     | Retrieve a `UserInfo` dict with details about the currently authenticated user.                     |
| `ohdear.authenticated()`          | Retrieve a `boolean` response indicating whether the current user is authenticated.                 |
| `ohdear.broken_links.show(123)`   | Retrieve a `BrokenLinksCollection` dict with details about broken links for a specific site.        |
| `ohdear.certificates.enable(123)` | Retrieve a `CertificateHealth` dict containing details about the certificate and it's health.       |
| `ohdear.checks.enable(123)`       | Retrieve a `boolean` indicating whether a check was enabled successfully.                           |
| `ohdear.checks.disable(123)`      | Retrieve a `boolean` indicating whether a check was disabled successfully.                          |
| `ohdear.cron_checks.show(123)`    | Retrieve a `CronChecksCollection` dict with details about the cron checks for a specific site.      |
| `ohdear.mixed_contents.show(123)` | Retrieve a `MixedContentsCollection` dict with details about the mixed content for a specific site. |
| `ohdear.sites.all()`              | Retrieve a `SitesCollection` dict with details about all sites.                                     |
| `ohdear.sites.show(123)`          | Retrieve a `Site` dict with details about a specific site.                                          |

## Change log

Please see [CHANGELOG](CHANGELOG.md) for more information on what has changed recently.

## Testing

```shell
hatch shell

hatch run test
```

## Security

If you discover any security related issues, please email security@voke.dev instead of using the issue tracker.

## Credits

- [Owen Voke][link-author]
- [All Contributors][link-contributors]

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.

## Treeware

You're free to use this package, but if it makes it to your production environment you are required to buy the world a tree.

It’s now common knowledge that one of the best tools to tackle the climate crisis and keep our temperatures from rising above 1.5C is to plant trees. If you support this package and contribute to the Treeware forest you’ll be creating employment for local families and restoring wildlife habitats.

You can buy trees [here][link-treeware-gifting].

Read more about Treeware at [treeware.earth][link-treeware].

[ico-version]: https://img.shields.io/pypi/v/ohdear-sdk.svg?style=flat-square
[ico-license]: https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square
[ico-github-actions]: https://img.shields.io/github/workflow/status/owenvoke/ohdear-python-sdk/Tests.svg?style=flat-square
[ico-treeware-gifting]: https://img.shields.io/badge/Treeware-%F0%9F%8C%B3-lightgreen?style=flat-square

[link-pypi]: https://pypi.org/project/ohdear-sdk
[link-github-actions]: https://github.com/owenvoke/ohdear-python-sdk/actions
[link-treeware]: https://treeware.earth
[link-treeware-gifting]: https://ecologi.com/owenvoke?gift-trees
[link-author]: https://github.com/owenvoke
[link-contributors]: https://github.com/owenvoke/ohdear-python-sdk/contributors
