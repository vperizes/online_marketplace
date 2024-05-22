from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ("name",)

    # overrides default str rep -> returns the value of name
    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField("item name", max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to="item_images", blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, related_name="items", on_delete=models.CASCADE
    )
    created_by = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
