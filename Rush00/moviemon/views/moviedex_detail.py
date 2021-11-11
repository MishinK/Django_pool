from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.http.response import HttpResponseNotFound
from moviemon.utils.jwt import get_moviemonid
from moviemon.utils.game import GameData, load_session_data
from moviemon.utils.load import load_midd

class Moviedex_detail(TemplateView):
    template_name = "moviedex_detail.html"
    context = {}

    @load_midd
    def get(self, request, moviemon_id):
        game = GameData.load(load_session_data())
        moviemon_id = get_moviemonid(moviemon_id)
        if moviemon_id is None:
            return HttpResponseNotFound(request)
        key = request.GET.get("key", None)
        if key and key == "b":
            return redirect("moviedex")
        self.context = {
            "actors": game.get_movie(moviemon_id).actors,
            "director": game.get_movie(moviemon_id).director,
            "plot": game.get_movie(moviemon_id).plot,
            "poster": game.get_movie(moviemon_id).poster,
            "title": game.get_movie(moviemon_id).title,
            "rating": game.get_movie(moviemon_id).rating,
            "year": game.get_movie(moviemon_id).year,
        }
        return render(request, self.template_name, self.context)
