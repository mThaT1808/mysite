from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'


class Contractor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    job = models.ForeignKey('Job', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подрядчик'
        verbose_name_plural = 'Подрядчики'


class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'
