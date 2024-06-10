from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenge_info = {
    "january": "This works!",
    "february": "Doing it on my own.Yey!",
    "march": "Third trial!",
    "april": "Practising Django",
    "may": "the fifth month",
    "june": "The sixth month",
    "july": "Looking forward to graduating",
    "august": "excited to learn new skills",
    "september": "2024 has been a different year",
    "october": "Looking forward to all my plans",
    "november": "Never giving up",
    "december": None
}


def index_of_months(request):
    months = list(monthly_challenge_info.keys())
    
    return render(request, "challenges/index.html",{
        "months": months})


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenge_info.keys())
    if month > len(months):
        return HttpResponseNotFound("Month not valid")
    else:
        forward_month = months[month-1].lower()
        redirect_path = reverse("month-challenge", args=[forward_month])
        return HttpResponseRedirect(redirect_path)

        # or you can use if statement


def Monthly_Challenges(request, month_any):
    try:
        challenge_information = monthly_challenge_info[month_any]
        return render(request, "challenges/challenge.html", {"text": challenge_information,
                                                             "month_name": month_any})
    except:
        raise Http404
