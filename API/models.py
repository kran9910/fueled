from django.db import models

class Car(models.Model):
    car_number = models.CharField(max_length=24)
    date = models.DateField(auto_now = True)

    def __str__(self):
        return "{} : {}".format(self.car_number, self.date)