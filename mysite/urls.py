from django.urls import path
from . import views

app_name = "mysite"

urlpatterns = [
    path("add/", views.AddPicture.as_view(), name="add"),
]