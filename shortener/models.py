from django.db import models
from datetime import date


class Url(models.Model):
    url_id = models.SlugField(max_length=7, primary_key=True)
    url = models.URLField(max_length=250)
    date_created = models.DateField(auto_now_add=True)
    days_to_expiry = models.IntegerField(default=90)

    def __str__(self):
        return self.url

    def check_expiry_date(self):
        if (date.today() - self.date_created).days > self.days_to_expiry:
            super(Url, self).delete()
            return False
        return True
