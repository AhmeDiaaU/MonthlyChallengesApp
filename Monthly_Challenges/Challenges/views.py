from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse
monthly_challenges_dct = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for at least 30 minutes every day",
    "march": "Read a book for at least 15 minutes every day",
    "april": "Practice yoga for at least 10 minutes every day",
    "may": "Eat no meat for the entire month",
    "june": "Walk for at least 30 minutes every day",
    "july": "Read a book for at least 15 minutes every day",
    "august": "Practice yoga for at least 10 minutes every day",
    "september": "Eat no meat for the entire month",
    "october": "Walk for at least 30 minutes every day",
    "november": "Read a book for at least 15 minutes every day",
    "december": None
}


def index(request):
    list_items = ""
    months = list(monthly_challenges_dct.keys())
    for month in months :
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge" , args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    print(list_items)
    response_list = f"<ul>{list_items}</ul>"
    return HttpResponse(response_list)

 
def challenges_by_numbers(request , month):
    """
    Takes number and changes it into string then redirects it to /cha/"month name"
    302 which is a redirect response, any response start with 300 its redirect
    """
    months = list(monthly_challenges_dct.keys())    
    if month >len(months):
        return HttpResponse("Invalid input")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge" , args=[redirect_month])  # get path of that name which linked with url in proj urls , we concatinate it with ars=[month] => which is a lst with one item
    return HttpResponseRedirect(redirect_path)

def monthly_challenges(request , month):
    try:
        challenge_month = monthly_challenges_dct[month]
        response_data = f"<h1>{challenge_month}<h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("error in name ")  
