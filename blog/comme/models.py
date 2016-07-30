from __future__ import unicode_literals
from django.db import models
from posts.models import Post
from django.core.urlresolvers import reverse

class Commentario(models.Model):
    commfield = models.TextField()
    pubdate = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Post, null=True)

    def __unicode__(self):
        return self.commfield

    def get_absolute_url(self):
        return reverse("comme:detail", kwargs={"id": self.id})

# Create your models here.
