from django.contrib.humanize.templatetags.humanize import ordinal
from django.db import models
from django.utils.html import escape
from django.utils.translation import ugettext as _
from datetime import datetime
import pytz

REFERENCE_TYPE_CHOICES = (
    ('BK', _('Book')),
    ('EJL', _('Electronic Journal')),
    ('JL', _('Journal')),
    ('WB', _('Website')),
)


class Reference(models.Model):
    type = models.CharField(_('Type'), max_length=3, choices=REFERENCE_TYPE_CHOICES, default='BK')
    slug = models.CharField(_('Slug'), max_length=128, unique=True)

    author = models.CharField(_('Author'), max_length=512)
    title = models.CharField(_('Title'), max_length=512)
    year = models.IntegerField(_('Year'), default=2000)

    series = models.CharField(_('Series'), max_length=512, blank=True, null=True)
    volume = models.IntegerField(_('Volume'), blank=True, null=True)
    edition = models.IntegerField(_('Edition'), blank=True, null=True)

    isbn = models.CharField(_('ISBN'), max_length=17, blank=True, null=True)
    url = models.URLField(_('URL'), blank=True, null=True)

    publisher = models.CharField(_('Publisher'), max_length=128, blank=True, null=True)
    place = models.CharField(_('Place'), max_length=128, blank=True, null=True)

    abstract = models.TextField(_('Abstract'), blank=True, null=True)
    comments = models.TextField(_('Comments'), blank=True, null=True)
    keywords = models.TextField(_('Keywords'), blank=True, null=True)

    accessed = models.DateField(_('Accessed'), default=datetime.now(pytz.utc))

    class Meta:
        verbose_name = _('Reference')
        verbose_name_plural = _('References')
        ordering = ['author']

    def __unicode__(self):
        return u'{0}, {1} [{2}]'.format(self.author, self.title, self.slug)

    def build_citation(self):
        """
        Formats a specific citation based on the type of reference
        """
        citation = u"{0} ({1}) <i>{2}</i>".format(
            escape(self.author), escape(self.year), escape(self.title))

        if self.edition and self.edition > 1:
            citation += u" " + ordinal(self.edition) + u" ed"

        if self.publisher:
            citation += u". {0}{1}".format(
                escape(self.publisher), ": " + escape(self.place) if self.place else "")

        if self.url:
            citation += _(u" [Online]. Available from  <a href='{0}'>{0}</a>").format(
                escape(self.url))

        citation += "."
        return citation.encode('utf-8')

    citation = property(build_citation)
