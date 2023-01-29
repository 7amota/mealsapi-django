from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
# \\ MealSerializer //
class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'mealtitle', 'descraption', 'no_of_ratings', 'avg_rating')

# \\ RateSerializer // 
class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username' , 'email' , 'password')
        extra_kwargs = {'password':{'write_only':True, 'required':True}}