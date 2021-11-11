from django.urls import path
from ex05 import views
from django.conf.urls import url

urlpatterns = [
	path("populate", views.populate, name="populate"),
	path("display", views.display, name="display"),
	path("remove", views.remove, name="remove"),
	url(r'^post', views.post, name='post'),
]