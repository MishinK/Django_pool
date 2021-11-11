from django.contrib import auth
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect
from ..forms import LoginForm
from django.views.generic import FormView
from django.urls import reverse_lazy
from typing import Any

class Login(FormView):
    template_name = "ex/login.html"
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form: LoginForm):
        user = auth.authenticate(self.request, username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
        auth.login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)