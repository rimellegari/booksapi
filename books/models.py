from django.db import models
from uuid import uuid4

# Create your models here.

class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.IntegerField()
    state = models.CharField(max_length=20)
    pages = models.IntegerField()
    Publisher = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)