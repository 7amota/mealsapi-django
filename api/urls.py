from django.urls import path ,include
from . import views
from .views import *
from rest_framework.routers import DefaultRouter
router =    DefaultRouter()
router.register('meals' , Meals)
router.register('rate' , Rate)
router.register('users' , UserViewSet)
urlpatterns = [
    path('' ,include(router.urls))
]
