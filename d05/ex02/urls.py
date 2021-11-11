from django.urls import path
from ex02 import views

urlpatterns = [
    path("init", views.init, name="init"),
	path("populate", views.populate, name="populate"),
	path("display", views.display, name="display"),
]