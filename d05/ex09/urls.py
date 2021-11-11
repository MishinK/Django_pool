from django.urls import path
from ex09 import views

urlpatterns = [
	path("display", views.display, name="display"),
]