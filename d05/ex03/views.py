from django.shortcuts import render, HttpResponse
from ex03.models import Movies

def populate(request):
	data = [
		{
			'title': "The Phantom Menace",
			'episode_nb': 1,
			'opening_crawl': None,
			'director': "George Lucas",
			'producer': "Rick McCallum",
			'release_date': "1999-05-19"
		},
		{
			'title': "Attack of the Clones",
			'episode_nb': 2,
			'opening_crawl': None,
			'director': "George Lucas",
			'producer': "Rick McCallum",
			'release_date': "2002-05-16"
		},
		{
			'title': "Revenge of the Sith",
			'episode_nb': 3,
			'opening_crawl': None,
			'director': "George Lucas",
			'producer': "Rick McCallum",
			'release_date': "2005-05-19"
		},
		{
			'title': "A New Hope",
			'episode_nb': 4,
			'opening_crawl': None,
			'director': "George Lucas",
			'producer': "Gary Kurtz, Rick McCallum",
			'release_date': "1977-05-25"
		},
		{
			'title': "The Empire Strikes Back",
			'episode_nb': 5,
			'opening_crawl': None,
			'director': "Irvin Kershner",
			'producer': "Gary Kurtz, Rick McCallum",
			'release_date': "1980-05-17"
		},
		{
			'title': "Return of the Jedi",
			'episode_nb': 6,
			'opening_crawl': None,
			'director': "Richard Marquand",
			'producer': "Howard G. Kazanjian, George Lucas, Rick McCallum",
			'release_date': "1983-05-25"
		},
		{
			'title': "The Force Awakens",
			'episode_nb': 7,
			'opening_crawl': None,
			'director': "J. J. Abrams",
			'producer': "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
			'release_date': "2015-12-11"
		},
	]
	try:
		for m in data:
			Movies(**m).save()
	except Exception as e:
		return HttpResponse(f'Error: {e}')
	return HttpResponse('OK')


def display(request):
	try:
		movies_lst = []
		for movie in Movies.objects.all():
			movies_lst.append([movie.title, movie.episode_nb, movie.opening_crawl, movie.director, movie.producer, movie.release_date])
		if len(movies_lst) > 0:
			return render(request, 'ex03/display.html', {
					'title' : 'ex03',
					'movies_lst': movies_lst,
			})
		else:
			return HttpResponse("No data available")
	except Exception as e:
		return HttpResponse(f'Error: {e}')