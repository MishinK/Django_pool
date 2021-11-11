from django.contrib import auth
from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(max_length=64, required=True)
	password = forms.CharField(max_length=64, required=True, widget=forms.PasswordInput())
	
	def clean(self):
		super(LoginForm, self).clean()
		try:
			auth.get_user_model().objects.get(username=self.cleaned_data.get('username'))
			if not auth.authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password')):
				self.add_error("password", "User does not exist !")
		except auth.get_user_model().DoesNotExist:
			self.add_error("username", "User does not exist !")
