from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_image = models.ImageField(upload_to='photos/',null=True,default ='photos/default.jpg')
    bio = models.CharField(max_length=50)        
    username = models.OneToOneField(User,unique = True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.username.username} Profile'
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
 