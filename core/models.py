from django.db import models
from django.conf import settings
from django.utils.text import slugify
from user.models import *
#from user.models import User

class Organization(models.Model):
    name= models.CharField(unique=True, max_length=200)
    logo=models.ImageField(upload_to="Organization/logo/")
    student_email = models.CharField(max_length=50,null=True)
    address=models.TextField()
    #short_name=models.CharField(max_length=50)
    #description=models.TextField()
    #website=models.URLField()

    def __str__(self):
        return self.name

'''
class Community(models.Model):
    community_name=models.CharField(max_length=200)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    followers=models.ManyToManyField(User, related_name='followed_users')  



    @property
    def total_upvotes(self):
        return self.communitypost_set.aggregate(total_upvotes=models.Sum('upvotes'))['total_upvotes'] or 0

    @property
    def total_downvotes(self):
        return self.communitypost_set.aggregate(total_downvotes=models.Sum('downvotes'))['total_downvotes'] or 0



    def __str__(self):
        return self.Organization.name

'''

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
