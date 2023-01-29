from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import *
from .models import *
from .serializer import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    def create(self , request , *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        token = Token.objects.get(user=serializer.instance)
       
        return Response({'token' : token.key,} , status.HTTP_200_OK)
    def list(self , request , *args, **kwargs):
        response = {'message' : 'sorry, you don`t have permissions to do that .'}
        return Response(response , status.HTTP_423_LOCKED)
        


# \\ VST Meals //
class Meals(viewsets.ModelViewSet):
    queryset=  Meal.objects.all()
    serializer_class = MealSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    @action(methods=['post'], detail=True)
    def rate_meal(self, request , pk=None):
        if 'stars' in request.data:
            meal = Meal.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            try:
                rate = Rating.objects.get(user=user.id , meal=meal.id)
                rate.stars = stars
                rate.save()
                serializerupdate = RateSerializer(rate , many=False)
                json = {
                    'message' : 'updated',
                    'data': serializerupdate.data
                }
                return Response(json, status.HTTP_200_OK)

            
            except:
                createrate = Rating.objects.create(
                    meal=meal , user=user , stars=stars
                )
                serializer = RateSerializer(createrate, many=False)
                json = {
                    'message' : 'created',
                    'data' : serializer.data
                }
                return Response(json, status=status.HTTP_200_OK)
        else:
            json = {
                'message': 'stars not provided'
            }
            return Response(json , status=status.HTTP_400_BAD_REQUEST)



# \\ VST Rate //
class Rate(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def update(self , request , *args, **kwargs):
        json = {'message' : 'invaild way to update !'}
        return Response(json,  status=status.HTTP_400_BAD_REQUEST)
    def create(self , request , *args, **kwargs):
        json = {'message' : 'invaild way to create !'}
        return Response(json,  status=status.HTTP_400_BAD_REQUEST)

