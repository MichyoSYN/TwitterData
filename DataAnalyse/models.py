import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Twitter(models.Model):
    id = models.AutoField(primary_key = True)
    text_content = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    event = models.CharField(max_length = 50, default = 'test')

    def __str__(self): # Show text_content
        return self.text_content

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)
    # was_published_recently.admin_order_field = 'pub_date'
    # was_published_recently.boolean = True
    # was_published_recently.short_description = 'Published recently?'