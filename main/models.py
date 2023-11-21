from django.db import models
import uuid
from django.contrib.auth.models import User
from .validators import file_size


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    media_file =models.FileField(upload_to='mediafiles',validators=[file_size], null=True, blank=True)
    caption = models.TextField()
    tags = models.ManyToManyField('Tag', blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    id = models.CharField(max_length=100, unique=True, primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-date_posted']
 
class Tag(models.Model):
    name = models.CharField(max_length=20,null=True, blank=True)
    slug = models.SlugField(max_length=20, null=True, blank=True)
    order = models.IntegerField()
    
    def __str__(self):
        return self.name
    class Meta:
        ordering =['order']
 
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middlename = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='profilepics', default='blank-profile-picture.png',null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)
    alternate_email = models.EmailField(max_length=255, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.user)

    
from django.db import models
from embed_video.fields import EmbedVideoField

class Item(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    video = EmbedVideoField()  # same like models.URLField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return str(self.video)