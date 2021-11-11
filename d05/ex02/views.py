from django.shortcuts import redirect, render, HttpResponse
from django.views.generic import TemplateView
import psycopg2
from psycopg2 import sql

def init(request):
	try:
		conn = psycopg2.connect(
			database = 'django_db',
			user = 'django_user',
			password = 'secret',
			host = 'localhost'
			)
		curr = conn.cursor()
		curr.execute(""" CREATE TABLE IF NOT EXISTS ex02_movies (
			title 			varchar(64) 	UNIQUE NOT NULL,
			episode_nb		serial			PRIMARY KEY, 
			opening_crawl 	text,
			director 		varchar(32) 	NOT NULL,
			producer 		varchar(128) 	NOT NULL,
			release_date 	date 			NOT NULL
			)
			""")
		conn.commit()
		conn.close()
	except psycopg2.Error as e:
		return HttpResponse(str(e.pgerror).replace('\n', '<br />'))
	return HttpResponse('OK')

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
		conn = psycopg2.connect(
			database = 'django_db',
			user = 'django_user',
			password = 'secret',
			host = 'localhost'
		)
		cur = conn.cursor()
		cur.execute('DELETE FROM ex02_movies')
		for m in data:
			values = [m['episode_nb'], m['title'], m['director'], m['producer'], m['release_date']]
			insert = sql.SQL('INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date) VALUES ({})').format(sql.SQL(',').join(map(sql.Literal, values)))
			cur.execute(insert)
		conn.commit()
		conn.close()
	except psycopg2.Error as e:
		return HttpResponse(str(e.pgerror).replace('\n', '<br />'))
	return HttpResponse('OK')


def display(request):
	try:
		conn = psycopg2.connect(
			database = 'django_db',
			user = 'django_user',
			password = 'secret',
			host = 'localhost'
		)
		cur = conn.cursor()
		cur.execute("SELECT * FROM ex02_movies")
		movies_lst = cur.fetchall()
		conn.close()
		if movies_lst:
			return render(request, 'ex02/display.html', {
					'title' : 'ex02',
					'movies_lst': movies_lst,
			})
		else:
			return HttpResponse("No data available")
	except psycopg2.Error as e:
		return HttpResponse("No data available")