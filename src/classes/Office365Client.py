from msal import ConfidentialClientApplication
import requests

from auth_secrets.office365_secrets import Office365Secrets
from lib.utils.web_auth_automation import get_auth_code_from_request_url


class Office365Client:
    def __init__(self):
        self.client = self._create_client()
        self.scopes = ["Notes.Read"]
        self.auth_request_url = self._generate_auth_request_url()
        self.access_token = ""
        self._authenticate_client()

    def _create_client(self):
        return ConfidentialClientApplication(
            client_id=Office365Secrets.CLIENT_ID,
            client_credential=Office365Secrets.CLIENT_SECRET,
            authority=Office365Secrets.AUTHORITY_URL,
        )

    def _generate_auth_request_url(self):
        return self.client.get_authorization_request_url(self.scopes)

    def _authenticate_client(self):
        auth_code = get_auth_code_from_request_url(
            self.auth_request_url,
            Office365Secrets.USER_EMAIL,
            Office365Secrets.USER_PASSWORD,
        )

        token = self.client.acquire_token_by_authorization_code(
            code=auth_code,
            scopes=self.scopes,
        )

        if "access_token" in token:
            self.access_token = token["access_token"]
            print("Office365 authenticated successfully")
        else:
            raise RuntimeError("Failed to authenticate Office365")

    def get_notebooks(self):
        headers = {"Authorization": "Bearer " + self.access_token}
        response = requests.get(Office365Secrets.GRAPH_ENDPOINT, headers=headers)
        notebooks = response.json()
        print(notebooks)
        return notebooks
