from django.urls import path
from . import views

urlpatterns = [
    path('',views.ShowAccount.as_view(), name='account'),
    path('logout', views.my_logout, name='logout'),
]