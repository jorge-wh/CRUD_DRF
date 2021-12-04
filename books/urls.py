# Django
from django.urls import path
from django.urls.conf import include

# Django-Rest-Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import BookViewSetAPI, listbooks

# Router API
router = DefaultRouter()
router.register(r'api', BookViewSetAPI, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    path('list-books/', listbooks, name="list_books")
]