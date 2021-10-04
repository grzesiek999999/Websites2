from django.db import models
from datetime import datetime


class WebsiteCategory(models.Model):
    name = models.CharField(max_length=100, default=None, null=True, blank=True)
    description = models.CharField(max_length=100, default=None, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=None)

    def __str__(self):
        return self.name



class Website(models.Model):
    url = models.CharField(max_length=1000, default=None, null=True, blank=True)
    title = models.CharField(max_length=100, default=None, null=True, blank=True)
    meta_description = models.CharField(max_length=1000000, default=None, null=True, blank=True)
    alexa_rank = models.IntegerField(default=None)
    category = models.ForeignKey(WebsiteCategory, default=None, null=True, blank=True, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class WebPage(models.Model):
    website = models.ForeignKey(Website, default=None, null=True, blank=True, on_delete=models.CASCADE)
    url = models.CharField(max_length=1000, unique= True, default=None, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, default=None, null=True, blank=True)
    meta_description = models.CharField(max_length=1000000, default=None, null=True, blank=True)