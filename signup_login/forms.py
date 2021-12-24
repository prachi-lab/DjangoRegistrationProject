from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
class CreateUserForm(UserCreationForm):
	username=forms.CharField(max_length=20)
	email = forms.EmailField()
	address = forms.CharField(max_length=20)

	class Meta :
		model = User
		fields = ['username', 'email', 'address', 'password1', 'password2']