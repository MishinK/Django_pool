from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpRequest
from typing import Any


class ShowAccount(FormView):

    template_name = 'account/account.html'
    form_class = auth.forms.AuthenticationForm
    success_url = reverse_lazy('account')
    initial = {'key': 'value'}

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if self.request.user.is_authenticated:
            return render(request, 'account/logout.html', {"user":self.request.user.username})
        form = self.form_class(initial=self.initial)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = auth.forms.AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(request, username=name, password=password)
            print(name, password, user)
            if user is not None:
                auth.login(request, user=user)
                return self.get(request)
        return redirect('account')

@csrf_exempt
def my_logout(request)->HttpResponse:
    auth.logout(request)
    return redirect('account')