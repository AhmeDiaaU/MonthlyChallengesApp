from django.urls import path
from . import views
urlpatterns = [
    path("" ,views.index ) ,
    path("<int:month>" , views.challenges_by_numbers),# should be first to check when it passes numbers
    path("<str:month>" , views.monthly_challenges , name = "month-challenge") # take input if its string and return it
]# take the input if its int and return it
