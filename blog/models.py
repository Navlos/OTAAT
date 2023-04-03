from django.db import models
from datetime import datetime

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    post_image = models.ImageField(upload_to = "images/", blank= True)
    image_caption = models.CharField(max_length = 50)
    content = models.CharField(max_length=100000)
    date = models.DateTimeField(default=datetime.now, blank=False)
    
    
    def __str__(self):
        return self.title
        
    

        
