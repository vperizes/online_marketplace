from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import NewItemForm


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(
        pk=pk
    )[0:3]
    return render(
        request, "item/detail.html", {"item": item, "related_items": related_items}
    )


# requires that user is logged in to add a new item. If auth fails then user is redirected to login page
@login_required
def newItem(request):
    form = NewItemForm()
    return render(
        request, "item/newitemform.html", {"form": form, "title": "Add New Item"}
    )
