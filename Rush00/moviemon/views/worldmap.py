from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.conf import settings
from moviemon.utils.load import load_midd
from moviemon.utils.other import Engine
from moviemon.utils.message import Message
from moviemon.utils.jwt import get_moviemon_token
from moviemon.utils.game import GameData, save_session_data, load_session_data

states = {"flush": None}
msg = Message("none")
worldstate = None


class Worldmap(TemplateView):
    template_name = "worldmap.html"
    context = {}

    def checkwin(self, game):
        if len(game.captured_list) >= len(game.moviemon):
            states["flush"] = "win"
        elif states["flush"] == "win":
            states["flush"] = None

    @load_midd
    def get(self, request):
        game = GameData.load(load_session_data())
        self.checkwin(game)
        key = request.GET.get('key', None)
        if key and key == "a" and states["flush"] == "win":
            return redirect("title")
        engine = Engine(
            settings.MAP_SIZE,
            settings.SCREEN_SIZE,
            settings.SCREEN_OFFSET,
            game.pos,
            game.movieballCount,
            len(game.moviemon),
            len(game.captured_list),
            game.map,
        )
        if not states["flush"] and msg.key == "battle":
            msg("none", single=True)
        if key and not states["flush"] == "win":	
            if not states["flush"]:
                if key == "up":
                    engine.move(0, -1)
                elif key == "down":
                    engine.move(0, 1)
                elif key == "left":
                    engine.move(-1, 0)
                elif key == "right":
                    engine.move(1, 0)
                elif key == "start":
                    return redirect("options")
                elif key == "select": 
                    return redirect("moviedex")
            if key == "a" and states["flush"] == "battle":
                states["flush"] = None
                return redirect(
                            "battle",
                            moviemon_id=get_moviemon_token(game.get_random_movie()),
                        )
            game.pos = (engine.px, engine.py)
            game.map = engine.map
            game.movieballCount = engine.movball
            save_session_data(game.dump())

            if engine.state == "battle":
                states["flush"] = "battle"
                msg(engine.state)
            elif engine.state:
                msg(engine.state)
    
        self.context = {
            "flush": states["flush"],
            "engine": engine.render(),
            "movieballs": game.movieballCount,
            "message": str(msg),
            "moviemons": len(game.moviemon),
        }
        return render(request, self.template_name, self.context)
