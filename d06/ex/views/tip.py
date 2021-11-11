from django.http.request import HttpRequest
from ex.forms.tip import DeleteTipForm, VoteForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import View
from django.db import DatabaseError
from ..forms import TipForm
from ..models import TipModel


class Tip(LoginRequiredMixin, View):
	http_method_names = ['post', 'put', 'delete']
	
	def dispatch(self, *args, **kwargs):
		method = self.request.POST.get('_method', '').lower()
		if method == 'put':
			return self.put(*args, **kwargs)
		if method == 'delete':
			return self.delete(*args, **kwargs)
		return super(Tip, self).dispatch(*args, **kwargs)
		
	def post(self, request):
		form = TipForm(request.POST)
		if form.is_valid():
			try:
				TipModel.objects.create(
					content=form.cleaned_data['content'],
					author=self.request.user
				)
			except DatabaseError:
				pass
		return redirect('home')
		
	def delete(self, request: HttpRequest):
		form = DeleteTipForm(None, request.POST)
		if form.is_valid():
			try:
				tip: TipModel = TipModel.objects.get(id=form.cleaned_data['id'])
				tip.delete()
			except TipModel.DoesNotExist:
				pass
			except DatabaseError:
				pass
		return redirect('home')
		
	def put(self, request):
		form = VoteForm(None, request.POST)
		if form.is_valid():
			try:
				tip: TipModel = TipModel.objects.get(id=form.cleaned_data['id'])
				if form.cleaned_data['type']:
					tip.upvote(request.user)
				else:
					tip.downvote(request.user)
			except TipModel.DoesNotExist:
				pass
			except DatabaseError:
				pass
		return redirect('home')