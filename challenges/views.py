from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Start a 30-day fitness challenge",
    "february": "Learn a new programming language",
    "march": "Read a book outside your usual genre",
    "april": "Take a daily walk and explore your neighborhood",
    "may": "Start a creative project (painting, writing, etc.)",
    "june": "Learn to cook a new recipe each week",
    "july": "Practice mindfulness and meditation daily",
    "august": "Take up a new hobby (photography, gardening, etc.)",
    "september": "Set and achieve a fitness goal (e.g., running a certain distance)",
    "october": "Volunteer or contribute to a community service project",
    "november": "Express gratitude daily in a journal",
    "december": "Learn a musical instrument or take music lessons"
}


# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalize_month = month.capitalize()
        redirect_path = reverse("monthly-challenge", args=[month])
        list_items += f"<li><a href={redirect_path}>{
            capitalize_month}</a></li>"
    return HttpResponse(f"<ul>{list_items}</ul>")


def monthly_challenge_by_number(request, month):

    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    forward_month = months[month - 1]

    redirect_path = reverse("monthly-challenge", args=[forward_month])

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):

    try:

        challenge_text = monthly_challenges[month]

        context = {"challenge_text": challenge_text,
                   "month": str(month).title()}
        return render(request, "challenges/challenge.html", context)
    except:

        return HttpResponseNotFound("This month is not supported!")
