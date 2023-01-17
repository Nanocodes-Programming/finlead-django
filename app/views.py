from django.shortcuts import render




# Create your views here.
def HomePage(request):
    context = {}
    return render(request, 'index.html', context)

def AboutUS(request):
    context = {}
    return render(request, 'about_us.html', context)

def InvestmentPlans(request):
    context = {}
    return render(request, 'plans.html', context)

def TermsAndConditions(request):
    context = {}
    return render(request, 'Terms_of_use.html', context)

def GlobalAgent(request):
    context = {}
    return render(request, 'global_agent.html', context)

def ContactUs(request):
    context = {}
    return render(request, 'contact.html', context)

def Privacy(request):
    context = {}
    return render(request, 'privacy.html', context)


def TOS(request):
    context = {}
    return render(request, 'tos.html', context)