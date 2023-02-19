from django.db import models
from django.contrib.auth.models import User 
from django.db.models.deletion import CASCADE 
from django.utils import timezone


gender = (
    ('Male','Male'),
    ('Female', 'Female'),
    ('NA','NA'),
)
class userProfiles(models.Model):
    user             = models.OneToOneField(User, related_name='userProfile', on_delete=models.CASCADE)
    userProfileImage = models.ImageField(null=True, blank=True, upload_to="userProfileImgs/") 
    gender           = models.CharField(max_length=45, choices=gender, default='NA')
    auth_token       = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.user)

