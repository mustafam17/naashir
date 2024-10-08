from urllib.parse import urlparse, parse_qs
from pydantic import HttpUrl


def parse_auth_code_from_url(url: HttpUrl) -> str:
    parsed_url = urlparse(url)
    auth_code = parse_qs(parsed_url.query).get("code")[0]
    return auth_code
