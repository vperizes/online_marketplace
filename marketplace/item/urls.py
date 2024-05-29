from django.urls import path
from . import views

# add app name to refer to in index.html href
app_name = "item"
urlpatterns = [
    path("new/", views.newItem, name="newItem"),
    path("browse/", views.browse, name="browse"),
    path("<int:pk>", views.detail, name="detail"),
    path("<int:pk>/delete/", views.deleteItem, name="deleteItem"),
    path("<int:pk>/edit/", views.editItem, name="editItem"),
]
