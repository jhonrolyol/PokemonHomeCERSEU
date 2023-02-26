from django.urls import path
from . import views

urlpatterns = [
    path("owner_list/", views.list_owner, name = "owner_list")
]
