from django.urls import path, include
from dataweb import views

urlpatterns = [
    path('home/', views.dataweb, name='dataweb'),
    path('customer/', include('customer.urls'))
]