from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,unique = True, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='photos/',null=True,default ='photos/default.jpg')
    bio = models.CharField(max_length=50)    
    projects = models.IntegerField(null=True)
    contact = models.CharField(max_length=20,null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    @classmethod
    def search_by_projects(cls,search_term):
        found = cls.objects.filter(projects__icontains=search_term)
        return found
class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    def __str__(self):
        return self.name