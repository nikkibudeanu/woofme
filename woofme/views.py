""" System Module """
from django.shortcuts import render


def page_not_found_view(request, exception):
    """ 404 status code error page """
    return render(request, '404.html', status=404)


def error_403(request, exception):
    """ 403  status code error page """
    return render(request, '403.html')   

def my_custom_error_view(request, *args, **argv):
    """ 500 status code error page """
    return render(request, '500.html', status=500)


