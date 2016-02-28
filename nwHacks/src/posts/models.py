from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    course = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    preferred_location = models.CharField(max_length=50, blank=True, null=True)
    updated = models.DateTimeField(editable=False)
    timestamp = models.DateTimeField(editable=False)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)
    address_number = models.CharField(max_length=100)
    street_name = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100)
    # views = models.IntegerField() possible use later for counting number of times a post is viewed
    slug = models.SlugField(unique=True, editable=False)  # used for generating readable urls

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
        return super(Post, self).save(*args, **kwargs)

