from django.urls import path
from ex04 import views
from django.conf.urls import url

urlpatterns = [
    path("init", views.init, name="init"),
	path("populate", views.populate, name="populate"),
	path("display", views.display, name="display"),
	path("remove", views.remove, name="remove"),
	url(r'^post', views.post, name='post'),
]