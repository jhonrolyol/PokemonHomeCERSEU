from django.urls import path
from . import views

urlpatterns = [
    path("meseros_list/", views.list_owner, name="meseros_list")
]

