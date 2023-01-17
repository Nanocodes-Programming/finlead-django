from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage, name='home' ),
    path("about_us/", views.AboutUS, name='about-us' ),
    path("investment-plans/", views.InvestmentPlans, name='plans' ),
    path("terms-and-conditions/", views.TermsAndConditions, name='terms' ),
    path("global-agents/", views.GlobalAgent, name='global-agent' ),
    path("contact/", views.ContactUs, name='contact' ),
    path("privacy/", views.Privacy, name='privacy' ),
    path("tos/", views.TOS, name='tos' ),
]