import pytest
import httpx
from fastapi import FastAPI
from fastapi.testclient import TestClient
from .simple_apis import (app)

client = TestClient(app)


def test_check_balance_valid():
    account_no = 3032158102

    # makes a POST request to the /check_balance/ endpoint
    response = client.get(f"/check_balance/{account_no}")

    # checks that the api request was successful
    assert response.status_code == 200

    # checks the content returned by the api matches the one we sent
    assert response.json() == 11257.35
