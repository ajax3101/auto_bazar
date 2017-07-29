from django.db import models


# Create your models here.
class Car(models.Model):
    name = models.CharField("марка", max_length=50)
    model = models.CharField("модель", max_length=50)
    price = models.IntegerField("цена")
    description = models.TextField("описание")
    photo = models.ImageField("фотография", upload_to='cars/photos', default="", blank=True)

    class Meta:
        verbose_name = "машина"
        verbose_name_plural = "машины"
        ordering = ["name"]

    def __str__(self):
        # return "Объект номер {}".format(self.id)
        return self.name
