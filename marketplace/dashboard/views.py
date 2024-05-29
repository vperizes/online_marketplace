from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from item.models import Item


# @login_required checks if user is logged in. If not, then redirects to login page
@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request, "dashboard/index.html", {"items": items})
