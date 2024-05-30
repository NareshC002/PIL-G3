
from django.shortcuts import render





def inscription_views(request):
    return render(request, 'Both/inscription.html')

def inscription(request):
    return render(request, 'Both/inscription.html')

def index(request):
    return render(request, 'Both/index.html')


def login_views(request):
    return render(request, 'Both/login.html')

def informations_views(request):
    return render(request, 'Both/informations_personelles.html')

def contact_views(request):
    return render(request, 'Both/contact.html')
