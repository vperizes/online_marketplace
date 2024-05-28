from django.urls import path
from . import views

# add app name to refer to in index.html href
app_name = "item"
urlpatterns = [
    path("new/", views.newItem, name="newItem"),
    path("<int:pk>", views.detail, name="detail"),
]
