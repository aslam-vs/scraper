from django.db import models
from django.utils.translation import ugettext_lazy as _


class Page(models.Model):

    """Page Model"""
    link_url = models.URLField(null=False, blank=False)
    og_title = models.CharField(
        _('Og Title'), blank=True, null=True, max_length=255)
    twitter_title = models.CharField(
        _('Twitter Title'), blank=True, null=True, max_length=255)
    title = models.CharField(_('Title'), blank=True, null=True, max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    lastmod_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.link_url


class Images(models.Model):

    """Image Model"""
    image = models.ImageField(upload_to='images/')
    width = models.CharField(_('Width'), max_length=11)
    height = models.CharField(_('Height'), max_length=11)
    page = models.ForeignKey(Page)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.url
