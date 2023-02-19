from django.db import models
from django.contrib.auth.models import User 
from django.db.models.deletion import CASCADE 
from django.utils import timezone

class blogs(models.Model):
    author = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE)
    title = models.TextField(max_length=100, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="blogImg/")
    description = models.TextField(max_length=300, null=True)
    content = models.TextField(max_length=1000, null=True)
    publishedAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user)