from django.forms import forms
from django.forms import ModelForm
from ..models import UserFavouriteArticle


class AddFavoriteArticleForm(ModelForm):
	class Meta:
		model = UserFavouriteArticle
		fields = []