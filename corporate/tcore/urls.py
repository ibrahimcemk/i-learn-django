from django.urls import path
from .views import merhaba

urlpatterns = [
    path('',merhaba,name='index')
]

