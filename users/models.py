from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    lasts_name = models.CharField(max_length=30)

class Website(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    release_date = models.DateField()
    rating = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
