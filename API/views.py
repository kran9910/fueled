import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from API.constants import *
from API.models import Car
from API.serializers import CarSerializer

def hasRecentlyFueled(car):
    expiry_date = datetime.datetime.now() - datetime.timedelta(days= expiry_days)
    cars_date = car.date
    if cars_date < expiry_date:
        return False
    else:
        return True

class AddCarView(APIView):
    def post(self, request, format = None):
        data = self.request.data
        car_number = data['car_number']
        password = data['password']
        day = datetime.datetime.now() - datetime.timedelta(days= expiry_days)
        expiry = datetime.datetime(day.year, day.month, day.day)
        if password == day_password:
            try:
                if Car.objects.filter(car_number = car_number).exists():
                    curr_car = Car.objects.filter(car_number = car_number)[0]
                    curr_car_date = datetime.datetime(curr_car.date.year, curr_car.date.month, curr_car.date.day)
                    if (curr_car_date < expiry):
                        Car.objects.filter(car_number = car_number)[0].delete()
                        car = Car(car_number=car_number)
                        car.save()
                        return Response({'status':'success' , 'message' : 'Car Added'})
                    else:
                        return Response({"status":"error" , "message":"Car Filled Tank Recently!"})
                else:
                    car = Car(car_number=car_number)
                    car.save()
                    return Response({'status':'success' , 'message' : 'Car Added'})
            except Exception as e:
                return Response({'status':'error', 'message': str(e)})

        else:
            return Response({'error' : 'Wrong Password!'})

class GetAllCars(APIView):
    def get(self,request, format=None):
        try:
            cars = Car.objects.all()
            cars = CarSerializer(cars, many=True)
            return Response(cars.data)
        except Exception as e:
            return Response({'error': str(e)})
