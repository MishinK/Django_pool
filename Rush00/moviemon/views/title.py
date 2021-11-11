from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from moviemon.utils.game import GameData, save_session_data

class Title(TemplateView):
    template_name = "title.html"

    def get(self, request):
        key = request.GET.get('key', None)
        if (key is not None):
            if (key == 'a'):
                save_session_data(GameData.load_default_settings().dump())
                return redirect('worldmap')
            elif (key == 'b'):
                return redirect('load_game')
        return render(request, self.template_name)
