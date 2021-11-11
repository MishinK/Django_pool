from django.views import View
from django.shortcuts import render

class Home(View):
	template_name = "ex/base.html"
	context = {'user': 'best user',}
	
	def get(self, request):
		return render(request, self.template_name, self.context)