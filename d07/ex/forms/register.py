from django.contrib import auth
from django import forms

class RegisterForm(forms.Form):
	username = forms.CharField(max_length=64, required=True)
	password = forms.CharField(max_length=64, required=True, widget=forms.PasswordInput())
	confirm_password = forms.CharField(max_length=64, required=True, widget=forms.PasswordInput())
	def clean(self):
		super(RegisterForm, self).clean()
		try:
			auth.get_user_model().objects.get(username=self.cleaned_data.get('username'))
			self.add_error('username', 'The username is aleready taken.')
		except auth.get_user_model().DoesNotExist:
			pass
		if self.cleaned_data.get('password') != self.cleaned_data.get('confirm_password'):
			self.add_error('confirm_password', "The confirmation and password didn't match.")