from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path('helloworld/', include("hello.urls")),
    path('admin/', admin.site.urls)
]
