from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
import requests


def get_graph_token():
    url = settings.AD_URL
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
        }
    data = {
        "grant_type": "client_credentials",
        "client_id": settings.CLIENT_ID,
        "client_secret": settings.CLIENT_SECRET,
        "scope": settings.SCOPE,
    }

    response = requests.post(url=url, headers=headers, data=data)
    return response.json()


def login_successful(request):
    if graph_token := get_graph_token():
        print(f'access_token: {graph_token["access_token"]}')
        url = f"{settings.GRAPH_MICROSOFT_USERS_URL}{request.user.username}"
        headers = {
            "Authorization": f'Bearer {graph_token["access_token"]}'
        }

        response = requests.get(url=url, headers=headers)
        print(f"response: {response.json()}")

    return HttpResponse("Your're login successful")