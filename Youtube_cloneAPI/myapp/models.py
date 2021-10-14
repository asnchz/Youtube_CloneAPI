from django.db import models

# Create your models here.
class Comment(models.Model):
    comment = models.CharField(max_length=150)
    videoId = models.CharField(max_length=150)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reply = models.CharField(max_length=150)