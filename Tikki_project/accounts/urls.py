from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as v
from .forms import CustomUserCreationForm

urlpatterns = [
    path('signup', v.signup, name='signup'),
    path('signin', auth_views.LoginView.as_view(template_name='accounts/tryin.html', authentication_form=CustomUserCreationForm), name='signin')
]