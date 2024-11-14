from django.urls import path
from . import views

urlpatterns = [
    path("autenticacion/", views.autenticacion, name="autenticacion"),
]
