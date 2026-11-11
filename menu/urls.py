from django.urls import path

from . import views

app_name = "menu"

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<str:name>/", views.hello, name="hello"),
]


