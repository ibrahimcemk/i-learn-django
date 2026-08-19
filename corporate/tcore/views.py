from django.http import HttpResponse
from django.shortcuts import render


def welcome_user(request):
    user_name="İbrahim Cem"

    return render(request, "welcome_user.html",{'user_name':user_name})