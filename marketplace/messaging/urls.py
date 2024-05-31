from django.urls import path
from . import views

app_name = "messaging"

urlpatterns = [
    path("", views.inbox, name="inbox"),
    path("new_message/<int:item_pk>/", views.new_conversation, name="new_message"),
]
