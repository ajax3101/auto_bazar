from django.db import models

from cars.models import Car


class Order(models.Model):
    car = models.ForeignKey(Car, verbose_name="машина")
    name = models.CharField("имя", max_length=50)
    phone = models.CharField("телефон", max_length=50)
    date = models.DateField("дата", auto_now_add=True)
