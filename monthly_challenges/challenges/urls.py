from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_of_months),
    path("<int:month>", views.monthly_challenges_by_number),
    path("<str:month_any>", views.Monthly_Challenges, name="month-challenge")
]
