from django.db import models


# categories model for items
class Categories(models.Model):
    name = models.CharField(max_length=255)

    # fixes django adding another 's' at end of model name
    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Categories"

    # overrides default str rep -> returns name of each category in categories table
    def __str__(self):
        return self.name
