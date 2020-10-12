from django.urls import path, include
from . import views as v


urlpatterns = [
    path('', v.HomePage, name='index'),
    path('signup', v.RegisterPage, name='signup'),
    path('signin', v.SignInPage, name='signin')
]