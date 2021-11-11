from django.views import View
from django.contrib import auth
from django.shortcuts import redirect

class Logout(View):

    def get(self, request):
        auth.logout(request)
        return redirect('home')