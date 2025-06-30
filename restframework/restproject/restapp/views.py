from rest_framework import viewsets
from rest_framework.viewsets import ViewSet
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Ensure this is an instance, not the class itself
    serializer_class = BookSerializer
