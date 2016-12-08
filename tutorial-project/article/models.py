from django.db import models
from django.core.urlresolvers import reverse


class Article(models.Model):
    article_name = models.CharField(max_length=50, verbose_name='Article Name')
    article_desc = models.CharField(max_length=500, verbose_name='Article Description')
    image = models.ImageField(null=False, verbose_name='Image')
    image_name = models.CharField(max_length=30, verbose_name='Image Alt Text')

    def __unicode__(self):
        return self.article_name
