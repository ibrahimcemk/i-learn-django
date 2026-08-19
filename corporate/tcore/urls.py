from django.urls import path
from .views import website_info

urlpatterns = [
    path('ibrahimcemkelesbilgi',website_info,),
]

