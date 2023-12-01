# Map url to view functions
from django.urls import path
from . import views

# URLConf
urlpatterns = [
    # Not calling this function (say_hello), just passing a reference to this funciton
    path('hello', views.say_hello)
]
