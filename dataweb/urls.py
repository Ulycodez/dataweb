from django.urls import path
from dataweb import views

urlpatterns = [
    path('', views.dataweb, name='dataweb'),
]