from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=128)
	author = models.CharField(max_length=128)
	publish_date = models.DateField(default=None)
	ISBN = models.CharField(max_length=13, default=None, unique=True)
	price = models.FloatField(default=0)

	created = models.DateField(auto_now_add=True)
	updated = models.DateField(auto_now=True)
