from django.urls import path
from ex00 import views

urlpatterns = [
	path('init', views.init, name="index"),
]