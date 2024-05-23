from django.shortcuts import render, get_object_or_404
from .models import Item


def detail(request, primary_Key):
    item = get_object_or_404(Item, primary_Key=primary_Key)
    return render(request, "item/detail.html", {"item": item})
