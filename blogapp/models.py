from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime , date



# Create your models here.

class Catagory(models.Model):
    name = models.CharField(max_length=255)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str: 
        return self.name

    
    def get_absolute_url(self):
        return reverse("home")


class post(models.Model):
    imgup = models.ImageField(null=True , blank=True , upload_to='images/')
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    title_tags = models.CharField(max_length=255)
    catagory = models.CharField(max_length=255 , default='coding')
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User , related_name="blog_post")
    
    
    # postimg= models.ImageField(null=True, blank=True , upload_to='images/')


    def total_dislikes(self) : 
        return self.dislikes.count()
    
    def total_likes(self) : 
        return self.likes.count()

    def __str__(self) -> str: 
        return self.title + ' | ' + str(self.author)

    
    def get_absolute_url(self):
        return reverse("article", args=[str(self.id)])




class Coment(models.Model):
    post = models.ForeignKey(post , related_name="coments" , on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return '%s - %s' % (self.post.title , self.name)
    

