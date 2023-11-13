from rest_framework.serializers import ModelSerializer
from .models import Book


class BookSerializer(ModelSerializer):
	class Meta:
		model = Book
		fields = ['pk', 'title', 'author', 'publish_date', 'ISBN', 'price']