from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=20)


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, related_name='posts')



class Comment(models.Model):
    author = models.CharField(max_length=30)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
