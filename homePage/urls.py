from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homePage'),
    path('user/', views.userPage, name="userPage")
]

