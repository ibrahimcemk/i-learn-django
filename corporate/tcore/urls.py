from django.urls import path
from .views import welcome_user

urlpatterns = [
    path('yeni-kullanici',welcome_user,),
]

