from django.urls import path
from ex06 import views
from django.conf.urls import url

urlpatterns = [
    path("init", views.init, name="init"),
	path("populate", views.populate, name="populate"),
	path("display", views.display, name="display"),
	path("update", views.update, name="update"),
	url(r'^post', views.post, name='post'),
]