from rest_framework import viewsets
from . import serializers, models

class BooksViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.BooksSerializer
	queryset = models.Books.objects.all()
