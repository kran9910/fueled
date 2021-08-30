from API.models import Car
import datetime
from API.constants import *

cars_to_delete = Car.objects.filter(date__lt = (datetime.datetime.now() - datetime.timedelta(days = expiry_days)))
print(cars_to_delete)
for car in cars_to_delete:
    car.delete()

