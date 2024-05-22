from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ("name",)

    # overrides default str rep -> returns the value of name
    def __str__(self):
        return self.name
