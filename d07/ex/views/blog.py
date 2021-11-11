from django.views.generic import ListView, DetailView, RedirectView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Article, UserFavouriteArticle
from ..forms import AddFavoriteArticleForm

class Home(RedirectView):
	url = reverse_lazy('articles')

class Articles(ListView):
	model = Article
	template_name = 'ex/articles.html'
	queryset = Article.objects.filter().order_by('-created')
 
class Publications(ListView):
    model = Article
    template_name = 'ex/publications.html' 

class Favourites(ListView):
    model = UserFavouriteArticle
    template_name = 'ex/favourites.html' 

class ArticleDetail(DetailView, FormView):
	model = Article
	template_name = 'ex/post_detail.html'
	form_class = AddFavoriteArticleForm
	success_url = reverse_lazy('favourites')
	
	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		form = self.get_form()
		if form.is_valid():
			item = form.save(commit=False)
			item.user = self.object.author
			item.article = self.object
			if not UserFavouriteArticle.objects.filter(user=item.user, article=item.article).exists():
				item.save()
			return self.form_valid(form)
		else:
			return self.form_invalid(form)
 
class ArticleNew(CreateView): 
	model = Article
	template_name = 'ex/post_new.html'
	fields = ['title', 'synopsis', 'content']
	
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super(ArticleNew, self).form_valid(form)

class ArticleEdit(UpdateView): 
    model = Article
    template_name = 'ex/post_edit.html'
    fields = ['title', 'synopsis', 'content']

class ArticleDelete(DeleteView):
    model = Article
    template_name = 'ex/post_delete.html'
    success_url = reverse_lazy('home')

