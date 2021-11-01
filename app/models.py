from django.db import models

# Create your models here.




class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    post = models.TextField()
    date_added = models.DateTimeField(auto_created=True)
    
    class Meta:
        ordering = ['title']
        verbose_name_plural='Blog'
        
class UserModel(models.Model):
    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField(unique=True)
    class Meta:
        ordering = ['username']











