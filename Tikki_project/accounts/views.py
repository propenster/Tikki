from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def signup(request):
    if(request.method == 'POST'):
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('index')
    else:
        f = CustomUserCreationForm()

    return render(request, 'accounts/try.html', {'form':f})


