from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('firstname', 'lastname', 'business_name', 'phone_number', 'email', 'country', 'state', 'city', 'zipcode', 'business_category', 'company_size')

    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('firstname', 'lastname', 'business_name', 'phone_number', 'email', 'country', 'state', 'city', 'zipcode', 'business_category', 'company_size')

