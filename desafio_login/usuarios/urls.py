from django.urls import path
from django.views.generic import RedirectView
from .views import login_view, registrar_view, menu_view

urlpatterns = [
    path("", RedirectView.as_view(url="/login/")),
    path("login/", login_view, name="login"),
    path("registrar/", registrar_view, name="registrar"),
    path("menu/", menu_view, name="menu"),
]