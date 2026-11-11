from django.http import HttpResponse
from django.shortcuts import render
from django.utils.html import escape


def home(request):
    context = {
        "restaurant_name": "The Little Bistro",
        "is_open": True,
        "specials": ["Tomato soup", "Grilled salmon", "Chocolate cake"],
    }
    return render(request, "menu/home.html", context)


def hello(request, name):
    return HttpResponse(f"Hello, {escape(name)}!")  # Security for XSS(cross-site scripting)

