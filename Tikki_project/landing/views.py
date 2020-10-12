from django.shortcuts import render

# Create your views here.

def HomePage(request):
    return render(request, 'landing/index.html', context={})

def RegisterPage(request):
    return render(request, 'landing/signup.html', context=None)


def SignInPage(request):
    return render(request, 'landing/signin.html', context=None)