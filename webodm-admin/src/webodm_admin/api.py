import requests
import logging


class WebODMAPI:
    # The permission groups are Django identifiers for WebODM permission types
    # The right permissions are already available in the Default group

    def __init__(self, baseurl: str = "http://localhost:8000"):
        self.baseurl = baseurl
        self._token = None

    def auth_headers(self):
        token = self.read_token()
        return {"Authorization": f"JWT {token}", "Content-type": "application/json"}

    def read_token(self):
        if not self._token:
            with open(".token", "r") as input:
                self._token = input.read()

        return self._token

    def auth_token(self, username: str, password: str):
        """
        Make a request for an authentication token (as an admin)
        curl -X POST -d "username=testuser&password=testpass" http://localhost:8000/api/token-auth/

        Returns a dict that looks like this
        {"token":"eyJ0eXAiO..."}
        """
        params = {"username": username, "password": password, "groups":[1]}
        try:
            response = requests.post(self.baseurl + "/api/token-auth/", json=params)
        except Exception as err:
            logging.error(err)
            raise (err)

        assert response.status_code == 200
        # Write a token to reuse. It expires after 6 hours
        token = response.json()["token"]
        with open(".token", "w") as out:
            out.write(token)

        return token

    def create_user(
        self, username: str, password: str, groups: list = [1], permissions: list = []
    ):
        """Creates a new WebODM user with the name passed in
        /api/admin/users/{id}/
        """

        params = {
            "username": username,
            "password": password,
            "groups": groups,
            "user_permissions": permissions,
        }

        url = self.baseurl + "/api/admin/users/"
        try:
            response = requests.post(url, json=params, headers=self.auth_headers())

        except Exception as err:
            logging.error(err)
            raise (err)

        if (
            response.status_code == 400
            and "already exists" in response.json()["username"]
        ):
            return
        if response.status_code == 404:
            raise Exception(response.content)

        return response

    def get_user(self, userid: int):
        """read a user's details
        /api/admin/users/{id}/
        """

        url = self.baseurl + f"/api/admin/users/{userid}/"

        try:
            response = requests.get(url, headers=self.auth_headers())

        except Exception as err:
            logging.error(err)
            raise (err)

        assert response.status_code == 200
        return response.json()

    def groups(self):
        """read a list of groups
        /api/admin/users/{id}/
        """

        url = self.baseurl + "/api/admin/groups/"

        try:
            response = requests.get(url, headers=self.auth_headers())

        except Exception as err:
            logging.error(err)
            raise (err)

        assert response.status_code == 200
        return response.json()
