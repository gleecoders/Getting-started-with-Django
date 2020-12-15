from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    lasts_name = models.CharField(max_length=30)
