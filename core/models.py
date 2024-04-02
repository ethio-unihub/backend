from django.db import models
from django.conf import settings

user_model = settings.AUTH_USER_MODEL

class Organization(models.Model):
    name= models.CharField(unique=True, max_length=200)
    logo=models.ImageField(upload_to="")
    address=models.CharField(max_length=150)


class Hashtag(models.Model):
    name=models.CharField(max_length=200)
    organization=models.ForeignKey(Organization, related_name="hashtags",on_delete=models.CASCADE)
    subscribers=models.PositiveBigIntegerField(null=True)
    slug=models.SlugField(unique=True)
