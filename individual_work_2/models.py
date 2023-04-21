from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    department = models.ForeignKey('Department', on_delete=models.PROTECT, null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
