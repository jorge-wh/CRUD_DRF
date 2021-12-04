# Django
from django.conf.urls import url
from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse

# Django-Rest-Framework
from rest_framework import viewsets  

# Models
from .models import Libro

# Serialzers
from .serializers import BookSerializer, BookFormSerializer

# Thirds
import requests

# Create your views here.
class BookViewSetAPI(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = BookSerializer


def listbooks(request):
    headers = {'Content-Type': 'application/json'}
    response_get = requests.get(url="http://127.0.0.1:8000/books/api/", headers=headers)

    response_json_text = []
    if response_get.status_code == 200:
        response_json_text = response_get.json()

    return render(request, "list_books.html", {'object_list': response_json_text})

