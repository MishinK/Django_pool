from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [

    path('', views.Home.as_view(), name='home'),
	path('articles/', views.Articles.as_view(), name='articles'),
	path('publications/', views.Publications.as_view(), name='publications'),
	path('favourites/', views.Favourites.as_view(), name='favourites'),
	path('articles/<int:pk>/', views.ArticleDetail.as_view(), name='post_detail'),
	path('articles/new/', views.ArticleNew.as_view(), name='post_new'),
	path('articles/<int:pk>/edit/', views.ArticleEdit.as_view(), name='post_edit'),
	path('articles/<int:pk>/delete/', views.ArticleDelete.as_view(), name='post_delete'),

	path('articles/<int:pk>/add_favourite/', login_required(views.ArticleDetail.as_view()), name='post_add_favourite'),
	

	path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('register/', views.Register.as_view(), name='register'),

]