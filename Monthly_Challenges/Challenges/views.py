from django.shortcuts import render # replace render_to_string and return static file directly
from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
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
    """_summary_
    request : https://docs.djangoproject.com/en/5.1/ref/request-response/

    Args:
        request (_type_): request of the user
        month (_type_): name of month to return the month challenge

        why didnt we add the file to Template directly ?
        its more cleaner to add a app name because if you have multiple apps it will be a mess
    Returns:
        static template by render_to_string
    """
    try:
        challenge_month = monthly_challenges_dct[month]
        return render(request , "Challenges/challenge.html") # render extract data frrom html file
    except:
        return HttpResponseNotFound("error in name ")  
