from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def hello_view(request: HttpResponse) -> HttpResponse:
    return HttpResponse("Hello World!")
