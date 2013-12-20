from django.db import models


class Reference(models.Model):
    slug = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=512)
    description = models.TextField(blank=True, null=True)
    isbn = models.CharField(max_length=17, blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return u'[%s]: %s' % (self.slug, self.title)
