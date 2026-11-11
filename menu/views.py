from django.http import HttpResponse
from django.utils.html import escape


def home(request):
    return HttpResponse("Welcome to the Little Bistro!")


def hello(request, name):
    return HttpResponse(f"Hello, {escape(name)}!")  # Security for XSS(cross-site scripting)

