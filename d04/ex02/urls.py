from django.conf.urls import url
from ex02 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post', views.post, name='post'),
]