from django.shortcuts import render
from user.models import Site, InvestmentPlan





# Create your views here.
def HomePage(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    context = {'site':site}

    return render(request, 'index.html', context)

def AboutUS(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    context = {'site':site}
    return render(request, 'about_us.html', context)

def InvestmentPlans(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    plans = InvestmentPlan.objects.all()
    context = {'site':site, 'plans':plans}
    return render(request, 'plans.html', context)

def TermsAndConditions(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    context = {'site':site}
    return render(request, 'Terms_of_use.html', context)

def ContactUs(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    context = {'site':site}
    return render(request, 'contact.html', context)

def Privacy(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    context = {'site':site}
    return render(request, 'privacy.html', context)


def TOS(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    context = {'site':site}
    return render(request, 'tos.html', context)