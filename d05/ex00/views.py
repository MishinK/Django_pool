from django.shortcuts import HttpResponse
import psycopg2

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
		retStr = str(e.pgerror).replace('\n', '<br />')
		return HttpResponse(retStr)
	return HttpResponse('OK')