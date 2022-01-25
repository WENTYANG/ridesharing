from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile #,Driverinfo

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','licence', 'max_passengers', 'vehicle_type', 'special_info']

# class DriverInfoForm(forms.ModelForm):
#     class Meta:
#         model = Driverinfo
#         fields = ['licence', 'max_passengers', 'vehicle_type', 'special_info']