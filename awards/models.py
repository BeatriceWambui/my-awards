from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,unique = True, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='photos/',null=True,default ='photos/default.jpg')
    bio = models.CharField(max_length=50)    
    projects = models.IntegerField(null=True)
    contact = models.CharField(max_length=20,null=True)
    username = models.CharField(max_length=50,null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30,default="hello")
    email = models.EmailField()
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/',default ='photos/default.jpg')
    description = models.TextField()
    link = models.CharField(max_length=250)
    editor = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    profile_image = models.ForeignKey(User,null=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering =['title']
    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def all_project(cls):
        return cls.objects.all()
       
    @classmethod
    def search_project(cls,search_term):
        found = cls.objects.filter(title__icontains=search_term)
        return found

class Review(models.Model):
    review = models.CharField(max_length=250)
    image = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='review')
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='review')
    
    def __str__(self):
        return self.review