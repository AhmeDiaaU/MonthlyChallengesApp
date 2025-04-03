from django.urls import path
from . import views
urlpatterns = [
    path("" ,views.index , name = "index" ) , # name of the index or / is index which can be used in my html by url  
    path("<int:month>" , views.challenges_by_numbers),# should be first to check when it passes numbers
    path("<str:month>" , views.monthly_challenges , name = "month-challenge") # take input if its string and return it
]# take the input if its int and return it
