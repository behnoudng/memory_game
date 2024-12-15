from django.db import models

class Card(models.Model):
    value = models.CharField(max_length=50)
    is_matched = models.BooleanField(default=False)

