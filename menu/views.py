from django.shortcuts import render


def home(request):
    context = {
        "restaurant_name": "The Little Bistro",
        "is_open": True,
        "specials": ["Tomato soup", "Grilled salmon", "Chocolate cake"],
    }
    return render(request, "menu/home.html", context)


def hello(request, name):
    return render(request, "menu/hello.html", {"name": name})
