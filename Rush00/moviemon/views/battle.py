from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.http.response import HttpResponseNotFound
from moviemon.utils.jwt import get_moviemonid
from moviemon.utils.load import load_midd
from moviemon.utils.game import load_session_data, GameData, save_session_data
from moviemon.utils.other import clip
import random

battleState = {
    "id": "",
    "text": "KEK Gotcha! {} ",
    "button-text": "🅰 Launch MovieBall   🅱 To escape",
}

class Battle(TemplateView):
    template_name = "battle.html"
    context = {}

    def calculate_winning_rate(self, game, moviemon_id):
        getchance = (
            50
            - game.moviemon[moviemon_id].rating * 10
            + game.get_strength() * 5
        )
        return clip(getchance, (1, 90))

    def useball(self, game, request, moviemon_id):
        getchance = self.calculate_winning_rate(game, moviemon_id)
        if getchance >= random.randrange(1, 101):
            battleState["text"] = "KEK Gotcha! {} "
            battleState["button-text"] = "🅰 Continue"
            game.captured_list.append(moviemon_id)
            save_session_data(game.dump())
        else:
            battleState["text"] = "You missed LOL!"
        return redirect(request.path)

    @load_midd
    def get(self, request, moviemon_id, key=None):
        game = GameData.load(load_session_data())
        moviemon_id = get_moviemonid(moviemon_id)
        if moviemon_id is None or game.moviemon.get(moviemon_id, None) is None:
            return HttpResponseNotFound(request)
        key = request.GET.get("key", None)
        if moviemon_id not in game.captured_list:
            if moviemon_id != battleState["id"]:
                battleState["text"] = "Wild {} appeared. GG VP"
                battleState["button-text"] = "🅰 Launch MovieBall   🅱 To escape"
                battleState["id"] = moviemon_id
        else:
            battleState["text"] = "KEK Gotcha! {} "
            battleState["button-text"] = "🅱 Continue"
        if key and key == "a":
            if moviemon_id not in game.captured_list:
                if game.movieballCount < 1:
                    return redirect(request.path)
                game.movieballCount -= 1
                save_session_data(game.dump())
                return self.useball(game, request, moviemon_id)
        elif key and  key == "b":
            battleState["text"] = "Wild {} appeared. GG VP"
            return redirect("worldmap")
        self.context = {
            "moviemon_id": moviemon_id,
            "movie_title": game.moviemon[moviemon_id].title,
            "movie_poster": game.moviemon[moviemon_id].poster,
            "movie_rating": game.moviemon[moviemon_id].rating,
            "user_rating": game.get_strength(),
            "user_text": battleState["text"].format(game.moviemon[moviemon_id].title),
            "pocketball_number": game.movieballCount,
            "button_text": battleState["button-text"],
            "user_winning_rate": "⚔️ {}%".format(
                str(self.calculate_winning_rate(game, moviemon_id))
            ),
        }
        return render(request, self.template_name, self.context)
