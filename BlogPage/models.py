from django.db import models

# Create your models here.
class blogs(models.Model):
    Title = models.CharField(max_length=90)
    PrevBlog = models.CharField(max_length=150)

    def __str__(self):
        return self.Title

class BlogContent(models.Model):
    Title = models.CharField(max_length=90)
    Content = models.TextField()
    # blog_id = models.AutoField    

    def __str__(self):
        return self.Title