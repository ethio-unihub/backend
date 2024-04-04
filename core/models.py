from django.db import models
from django.conf import settings
from django.utils.text import slugify

from user.models import *

class Organization(models.Model):
    name= models.CharField(unique=True, max_length=200)
    logo=models.ImageField(upload_to="organization/logo/")
    student_email = models.CharField(max_length=50,null=True)
    address=models.TextField()

    def __str__(self):
        return self.name


class Hashtag(models.Model):
    name = models.CharField(max_length=200)
    organization = models.ForeignKey(Organization, related_name="hashtags", on_delete=models.CASCADE)
    subscribers = models.ManyToManyField(Profile, related_name="subscribed_hashtags", blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f'#{self.slug}'

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Hashtag.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)