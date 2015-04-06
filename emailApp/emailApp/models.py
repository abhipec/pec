from jsonfield import JSONField

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Rule(models.Model):

    name = models.CharField(max_length=50, null = True)

    description = models.TextField(null = True, blank = True)

    rule = models.TextField(null = True, blank = True)

    RULE_TYPES = [('',''),('category', 'Category'), ('sender', 'Sender')]

    ruleType = models.CharField(max_length=20, choices=RULE_TYPES, default = '')


    def __unicode__(self):
        return self.name


class Email(models.Model):

    messageId = models.SlugField(max_length=100, unique=True)

    sender = models.EmailField(max_length=254, unique = False)

    timeStamp = models.DateTimeField()

    subject = models.CharField(max_length=998, null = True)

    textPlain = models.TextField(null = True, blank = True)

    textHtml = models.TextField(null = True, blank = True)

    textCleanPlain = models.TextField(null = True, blank = True)

    textCleanHtml = models.TextField(null = True, blank = True)

    CATEGORIES = [('NULL','Not categorized'),('promotional', 'Promotional'), ('spam', 'Spam'), ('human', 'Human'), ('notification', 'Notification'), ('others', 'Others')]

    category = models.CharField(max_length=15, choices=CATEGORIES, default='')

    attachments = models.TextField(null = True, blank = True)


    def __unicode__(self):
        return self.sender

    def getUrl(self):
        return reverse('messagePage', args=[str(self.messageId)])

class Dashboard(models.Model):

    data = models.TextField(null = True, blank = True)

    source = models.OneToOneField(Email)

    timeStamp = models.DateTimeField()

    validTill = models.DateTimeField()

    def __unicode__(self):
        return self.data
