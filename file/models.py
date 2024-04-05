from django.db import models

from user.models import Profile
from post.models import Tag

# Create your models here.

class File(models.Model):
    name = models.CharField(max_length=500)
    file = models.FileField(upload_to='files/user-upload/')
    tag = models.ManyToManyField(Tag, related_name='tagged_files')
    upvote = models.ManyToManyField(Profile, related_name='upvoted_files', blank=True)
    downvote = models.ManyToManyField(Profile, related_name='downvoted_files', blank=True)
    author = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, related_name='my_files')
    save = models.ManyToManyField(Profile, related_name='saved_files', blank=True)
    download = models.ManyToManyField(Profile, related_name='downloaded_files', blank=True)
    