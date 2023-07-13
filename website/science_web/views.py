from django.shortcuts import render
from django.http import HttpResponse


def base(request):
    return HttpResponse('home')


def field(request):
    return HttpResponse()


def mathematics(request):
    return HttpResponse()


def fisics(request):
    return HttpResponse()


def chemistry(request):
    return HttpResponse()


def informatics(request):
    return HttpResponse()


def history(request):
    return HttpResponse()


def shop(request):
    return HttpResponse()
