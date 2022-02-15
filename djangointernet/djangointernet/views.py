from django.http import HttpResponse


def homepage(request):
    """
    About function linking the view when url is hit
    """
    return HttpResponse("homepage")


def about(request):
    """
    About function linking the view when url is hit
    """
    return HttpResponse("About")
