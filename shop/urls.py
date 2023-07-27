from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('home_page', views.home_page, name='home_page'),
    path('tshirt_details', views.tshirt_details, name='tshirt_details'),
    path('hoodie_details', views.hoodie_details, name='hoodie_details'),
    path('payment_details', views.payment_details, name='payment_details'),
    path('show_page', views.index, name='show_page'),
]