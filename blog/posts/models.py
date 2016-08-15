from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 120)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})

class Commentario(models.Model):
    commfield = models.TextField()
    pubdate = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Post, null=True, related_name="comments")

    def __unicode__(self):
            return self.commfield

    def get_absolute_url(self):
         return reverse("posts:detail", kwargs={"pk": self.pk})



