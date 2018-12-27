from django import forms
from django.core import validators
from django.contrib.auth.models import User
from profile_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
	password = forms.CharField(widget= forms.PasswordInput)
	class Meta:
		model = User
		fields = ('first_name','last_name', 'username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
	class Meta:
		model = UserProfileInfo
		fields = ('bio', 'profile_pic')


class LoginForm(forms.Form):
	username = forms.CharField(max_length=150)
	password = forms.CharField(widget=forms.PasswordInput())
	def clean(self):
		all_clean_data = super().clean()
		return all_clean_data