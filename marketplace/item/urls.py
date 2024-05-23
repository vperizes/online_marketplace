from django.urls import path
from . import views

path("<int:primary_Key>", views.detail, name="detail")
