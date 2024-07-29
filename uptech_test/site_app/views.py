from http.client import HTTPResponse
from django.shortcuts import render


def main_view(request) -> HTTPResponse:
    if request.method == 'GET':

        return render(request, 'site_app/index.html')


def second_view(request) -> HTTPResponse:
    if request.method == 'GET':

        return render(request, 'site_app/index.html')


def third_view(request) -> HTTPResponse:
    if request.method == 'GET':

        return render(request, 'site_app/index.html')


def fourth_view(request) -> HTTPResponse:
    if request.method == 'GET':

        return render(request, 'site_app/index.html')


def fifth_view(request) -> HTTPResponse:
    if request.method == 'GET':

        return render(request, 'site_app/index.html')


def sixth_view(request) -> HTTPResponse:
    if request.method == 'GET':

        return render(request, 'site_app/index.html')
