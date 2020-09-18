from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from tinymce import HTMLField

class TagModel(models.Model):
    tag_name = models.CharField(max_length=35)
    tag_slug = models.SlugField(unique=True, max_length=35)
    tag_added = models.DateTimeField(auto_now_add=True)
    tag_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tag_name

    class Meta:
        ordering = ['tag_name']
        verbose_name = 'Tags'
        verbose_name_plural = 'All Tags'


class BookModel(models.Model):
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=100)
    book_slug = models.SlugField(max_length=100, unique=True)
    book_author = models.CharField(max_length=120)
    author_quote = models.CharField(max_length=250, blank=True)
    author_description = models.TextField(blank=True)
    book_image_url = models.TextField()
    book_summary = HTMLField('book_summary')
    tag = models.ManyToManyField(TagModel, blank=True)
    book_publish_on = models.DateField(default=datetime.now)
    publish_status = models.BooleanField(default=True)
    book_added = models.DateTimeField(auto_now_add=True)
    book_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book_title

    class Meta:
        ordering = ['-book_added']


class SuggestionModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    book_name = models.CharField(max_length=100, blank=True)
    suggestion = models.TextField()
    suggestion_added = models.DateTimeField(auto_now_add=True)
    suggestion_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name) + '-'  + str(self.email)
