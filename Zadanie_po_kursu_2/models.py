from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    card_number = models.CharField(max_length=16)
    pin = models.CharField(max_length=4)
    current_user = models.BooleanField(auto_created=False)


class Balance(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    rub = models.IntegerField(default=0)
    usd = models.IntegerField(default=0)
    eur = models.IntegerField(default=0)

