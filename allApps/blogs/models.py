from django.db import models
from django.contrib.auth.models import User 
from django.db.models.deletion import CASCADE 
from django.utils import timezone

class blogs(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    imageUrl = models.URLField(max_length=200, null=True)
    description = models.CharField(max_length=300, null=True)
    content = models.CharField(max_length=1000, null=True)
    publishedAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)