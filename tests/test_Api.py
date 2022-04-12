import json

from fastapi.testclient import TestClient
from api import app  # importing app from api.py file
from requests.auth import HTTPBasicAuth
import os


class TestApi:

    def test_home_route_redirection(self):
        """
            Used to test if the request is well redirected to the mission path
        """
        client = TestClient(app)
        auth = HTTPBasicAuth(os.environ["NASA_USER"], os.environ["NASA_PASS"])
        response = client.get("/", auth=auth, json={"script": "5 5 1 1 E MM"})
        assert response.history[0].status_code == 307
        assert response.history[0].headers['location'] == '/mission'

    def test_home_route_invalid_auth(self):
        """
            Used to test if the request was not completed because valid authentication information is missing for
            home route
        """
        client = TestClient(app)
        auth = HTTPBasicAuth("test", "test")
        response = client.get("/", auth=auth, json={"script": "5 5 1 1 E MM"})
        assert response.status_code == 401

    def test_mission_route_invalid_auth(self):
        """
            Used to test if the request was not completed because valid authentication information is missing for
            mission route
        """
        client = TestClient(app)
        auth = HTTPBasicAuth("test", "test")
        expected_text_response = {"detail": "Incorrect email or password"}
        response = client.get("/", auth=auth, json={"script": "5 5 1 1 E MM"})
        assert response.status_code == 401
        assert json.loads(response.text) == expected_text_response

    def test_mission_route_no_auth(self):
        """
            Used to test if the request was not completed because no authentication information is filled in using the
            mission route
        """
        client = TestClient(app)
        expected_text_response = {"detail": "Not authenticated"}
        response = client.get("/", json={"script": "5 5 1 1 E MM"})
        assert response.status_code == 401
        assert json.loads(response.text) == expected_text_response

    def test_mission_result(self):
        """
            Used to test if the query returns a result
        """
        client = TestClient(app)
        auth = HTTPBasicAuth(os.environ["NASA_USER"], os.environ["NASA_PASS"])
        response = client.get("/mission", auth=auth, json={"script": "5 5 1 1 E MM"})
        assert response.text is not None
        assert response.status_code == 200
