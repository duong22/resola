import imp
from .serializers import BookSerializer
from .models import Book
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
import math


class BookViewSet(ModelViewSet):

	serializer_class = BookSerializer
	queryset = Book.objects.all()
	permission_classes = [IsAuthenticatedOrReadOnly]
