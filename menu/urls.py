from django.urls import path

from . import views

app_name = "menu"

urlpatterns = [
    path("", views.home, name="home"),
    path("item/<int:pk>/", views.item_detail, name="item_detail"),
    path("hello/<str:name>/", views.hello, name="hello"),
]
