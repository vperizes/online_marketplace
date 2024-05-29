from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import NewItemForm, EditItemForm


def browse(request):
    items = Item.objects.all()
    return render(request, "item/browse.html", {"items": items})


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
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            # create obj but does not save to db
            item = form.save(commit=False)
            # need to add created_by field and then save to db
            item.created_by = request.user
            item.save()

            return redirect("item:detail", pk=item.id)

    # if request is get then just show form
    else:
        form = NewItemForm()
    return render(
        request, "item/itemform.html", {"form": form, "title": "Add New Item"}
    )


@login_required
def deleteItem(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect("dashboard:index")


@login_required
def editItem(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect("item:detail", pk=item.id)

    else:
        form = EditItemForm(instance=item)
    return render(
        request,
        "item/itemform.html",
        {"form": form, "title": f"Edit Item: {item.name}"},
    )
