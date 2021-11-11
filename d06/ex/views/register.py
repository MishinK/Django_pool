from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect
from ..forms import RegisterForm
from django.views.generic import FormView
from django.contrib import auth
from django.urls import reverse_lazy
from typing import Any

class Register(FormView):
    template_name = "ex/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form: RegisterForm):
        user = auth.get_user_model().objects.create_user(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
        auth.login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)