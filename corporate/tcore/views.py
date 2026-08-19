from django.http import HttpResponse


def merhaba(request):
    result="Merhaba Django Sayfası"

    return HttpResponse(result)