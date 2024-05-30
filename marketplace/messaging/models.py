from django.db import models
from django.contrib.auth.models import User
from item.models import Item


class Messages(models.Model):
    item = models.ForeignKey(Item, related_name="messages", on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-modified_at",)


class Message(models.Model):
    messages = models.ForeignKey(
        Messages, related_name="conversation", on_delete=models.CASCADE
    )
    msg_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name="created_msgs", on_delete=models.CASCADE
    )
