from django.urls import path

from . import views

'''
Aqui temos que criar algumas rotas
'''

urlpatterns = [
    path("", views.index, name="home"),
    path("user/", views.userPage, name="userPage")
]