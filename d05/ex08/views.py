from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
import psycopg2
from psycopg2 import sql
from .utilities import pars_planet, pars_people

def init(request):
	try:
		conn = psycopg2.connect(
			database = 'django_db',
			user = 'django_user',
			password = 'secret',
			host = 'localhost'
			)
		curr = conn.cursor()
		curr.execute(""" CREATE TABLE IF NOT EXISTS ex08_planets (
			id 					SERIAL 		PRIMARY KEY,
			name  				VARCHAR(64) UNIQUE NOT NULL,
			climate				VARCHAR,
			diameter			INT,
			orbital_period		INT,
			population			BIGINT,
			rotation_period		INT,
			surface_water		REAL,
			terrain				VARCHAR(128)
			) ;
			""")
		conn.commit()
		curr.execute(""" CREATE TABLE IF NOT EXISTS ex08_people (
			id					SERIAL 		PRIMARY KEY,
			name				VARCHAR(64) UNIQUE NOT NULL,
			birth_year			VARCHAR(32),
			gender				VARCHAR(32),
			eye_color			VARCHAR(32),
			hair_color			VARCHAR(32),
			height				INT,
			mass				REAL,
			homeworld			VARCHAR(64)	REFERENCES ex08_planets(name)
			) ;
			""")
		conn.commit()
		conn.close()
	except psycopg2.Error as e:
		return HttpResponse(str(e.pgerror).replace('\n', '<br />'))
	return HttpResponse('OK')

def populate(request):
	try:
		conn = psycopg2.connect(
			database = 'django_db',
			user = 'django_user',
			password = 'secret',
			host = 'localhost'
		)
		cur = conn.cursor()
		cur.execute('ALTER SEQUENCE ex08_people_id_seq RESTART WITH 1 ; DELETE FROM ex08_people ;')
		cur.execute('ALTER SEQUENCE ex08_planets_id_seq RESTART WITH 1 ; DELETE FROM ex08_planets ;')
		conn.commit()
		with open("data/planets.csv", 'r') as f:
			planets = [pars_planet(line) for line in f.readlines()]
		with open("data/people.csv", 'r') as f:
			people = [pars_people(line) for line in f.readlines()]
		for planet in planets:
			values = [
					planet['name'],
                    planet['climate'],
                    planet['diameter'],
                    planet['orbital_period'],
                    planet['population'],
                    planet['rotation_period'],
                    planet['surface_water'],
                    planet['terrain'],
					]
			insert = sql.SQL('INSERT INTO ex08_planets (name, climate, diameter, orbital_period, population, rotation_period, surface_water, terrain) VALUES ({})').format(sql.SQL(',').join(map(sql.Literal, values)))
			cur.execute(insert)
		for person in people:
			values = [
				    person['name'],
                    person['birth_year'],
                    person['gender'],
                    person['eye_color'],
                    person['hair_color'],
                    person['height'],
                    person['mass'],
                    person['homeworld'],
					]
			insert = sql.SQL('INSERT INTO ex08_people (name, birth_year, gender, eye_color, hair_color, height, mass, homeworld) VALUES ({})').format(sql.SQL(',').join(map(sql.Literal, values)))
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
		cur.execute("""
		    SELECT
			ex08_people.name,
			ex08_people.homeworld,
			ex08_planets.climate
            FROM
			ex08_planets RIGHT JOIN ex08_people
			ON
			ex08_people.homeworld = ex08_planets.name
            WHERE
            ex08_planets.climate
            LIKE '%windy%'
            ORDER BY ex08_people.name;
		""")
		movies_lst = cur.fetchall()
		conn.close()
		if movies_lst:
			return render(request, 'ex08/display.html', {
					'title' : 'ex08',
					'movies_lst': movies_lst,
			})
		else:
			return HttpResponse("No data available")
	except psycopg2.Error as e:
		return HttpResponse("No data available")
