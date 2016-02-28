from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.template.defaultfilters import slugify
from googlemaps import Client
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    course = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(editable=False)
    timestamp = models.DateTimeField(editable=False)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100, blank=True, null=True)
    # views = models.IntegerField() possible use later for counting number of times a post is viewed
    slug = models.SlugField(unique=True, editable=False)  # used for generating readable urls
    lat = models.FloatField(blank=True, null=True, editable=False)
    lon = models.FloatField(blank=True, null=True, editable=False)
    attendees = models.IntegerField(default=1)
    
    def __unicode__(self):
        return self.title

    # On save, update timestamp and updated and generate slug
    def save(self, *args, **kwargs):
        # only update timestamp when the object is first created
        # when id is not set yet
        if not self.id:
            self.timestamp = timezone.now()
        self.updated = timezone.now()
        self.slug = slugify(self.title)
        gmaps = Client(key="AIzaSyDPPebmy_mg8ho15JXng1WD2ByUsYrT7bY")
        results = gmaps.geocode(address=self.address + ", " + self.city, region="CA")
        if results:
            self.lat = results[0]['geometry']['location']['lat']
            self.lon = results[0]['geometry']['location']['lng']

        return super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    user = models.ForeignKey(User)
    content = models.TextField(max_length=1000)
    post = models.ForeignKey(Post)
    timestamp = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        # only update timestamp when the object is first created
        # when id is not set yet
        if not self.id:
            self.timestamp = timezone.now()
        self.updated = timezone.now()
        return super(Comment, self).save(*args, **kwargs)
