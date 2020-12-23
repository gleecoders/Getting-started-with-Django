from django.db import models


class User(models.Model):
    first_name = models.CharField("the person's first name", max_length=30)
    last_name = models.CharField("the person's last name", max_length=30)
    cars = models.ManyToManyField('Car', verbose_name="the user's cars")


STATUS_CHOICES = (
    ('R', 'Reviewed'),
    ('N', 'Not reviewed'),
    ('E', 'Error'),
    ('A', 'Accepted'),
)


class Website(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(unique=True)
    release_date = models.DateField()
    rating = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['rating']
        db_table = 'website_custom_table_name'
        verbose_name = 'the Website'
        verbose_name_plural = 'the websites'


class Car(models.Model):
    name = models.CharField(max_length=40, primary_key=True)


class Ox(models.Model):
    class Meta:
        verbose_name = 'ox'
        verbose_name_plural = 'oxen'
