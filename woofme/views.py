""" System Module """
from django.shortcuts import render


def page_not_found(request, exception):
    """ 404 status code error page """
    return render(request, '404.html', status=404)


def bad_request(request, exception):
    """ 400 error page """
    return render(request, '400.html')


def custom_error(request, *args, **argv):
    """ 500 status code error page """
    return render(request, '500.html', status=500)
