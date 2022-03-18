from django.db import models
from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField
from unidecode import unidecode


# Create your models here.

class Menu(models.Model):
    """The Menu pages for the website"""
    title = models.CharField(max_length=120, unique=True)
    slug = AutoSlugField(populate_from='title_format')
    content = RichTextUploadingField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def title_format(self):
        return unidecode(self.title) # This is to create the slug, even if it uses hanzi


class Article(models.Model):
    """Articles/News posted in the website."""
    title = models.CharField(max_length=120, unique=True)
    slug = AutoSlugField(populate_from='title_format')
    content = RichTextUploadingField(blank=True, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def title_format(self):
        return unidecode(self.title)