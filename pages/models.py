from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE, default=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("pages:post_detail", args=[str(self.pk)])
    