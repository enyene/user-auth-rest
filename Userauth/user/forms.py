from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import CustomerUser

class CustomerUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomerUser
        fields = ['email']

class CustomerUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomerUser
        fields = ['email']
        
