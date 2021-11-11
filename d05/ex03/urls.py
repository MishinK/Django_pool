from django.urls import path
from ex03 import views

urlpatterns = [
	path("populate", views.populate, name="populate"),
	path("display", views.display, name="display"),
]