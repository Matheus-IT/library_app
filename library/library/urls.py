from django.urls import path, include
from rest_framework.routers import DefaultRouter

from books import views as booksviews

router = DefaultRouter()
router.register(r'books', booksviews.BooksViewSet, basename='books')

urlpatterns = [
    path('', include(router.urls))
]
