from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    """
    About function linking the view when url is hit
    """
    return render(request, "homepage.html")


def about(request):
    """
    About function linking the view when url is hit
    """
    return render(request, "about.html")
