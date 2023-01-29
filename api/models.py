from django.db import models
import uuid
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator ,MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
# \\ meal //
class Meal(models.Model):
    id = models.AutoField(primary_key=True)
    mealtitle = models.CharField(max_length=50)
    descraption = models.TextField()
    def no_of_ratings(self):
        ratings = Rating.objects.filter(meal=self)
        return len(ratings)
    
    def avg_rating(self):
        # sum of ratings stars  / len of rating hopw many ratings 
        sum = 0
        ratings = Rating.objects.filter(meal=self) # no of ratings happened to the meal 

        for x in ratings:
            sum += x.stars

        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0






# \\ rateing //
class Rating(models.Model):
    id = models.AutoField(primary_key=True)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey( User ,on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MaxValueValidator(5) , MinValueValidator(1)])
# ==> this code means the user and meal cannot be together any more !.
    class Meta:
        unique_together = ('user','meal')
        index_together = ('user' , 'meal')

@receiver(post_save ,sender=settings.AUTH_USER_MODEL)
def createtoken(created, instance , sender, **kwargs ):
    if created:
       token = Token.objects.create(user=instance)