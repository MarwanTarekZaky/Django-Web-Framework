from django.shortcuts import get_object_or_404, render

from .models import MenuItem


def home(request):
    items = MenuItem.objects.filter(is_available=True)
    context = {
        "restaurant_name": "The Little Bistro",
        "items": items,
    }
    return render(request, "menu/home.html", context)


def item_detail(request, pk):
    item = get_object_or_404(MenuItem, pk=pk, is_available=True)
    return render(request, "menu/item_detail.html", {"item": item})


def hello(request, name):
    return render(request, "menu/hello.html", {"name": name})
