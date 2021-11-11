from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from moviemon.utils.game import load_session_data, GameData
from moviemon.utils.jwt import get_moviemon_token
from moviemon.utils.load import load_midd

MoviedexState = {
    'posistion': 0
}

class Moviedex(TemplateView):
    template_name = "moviedex.html"
    context = {}

    @load_midd
    def get(self, request):
        game = GameData.load(load_session_data())
        if MoviedexState['posistion'] >= len(game.captured_list):
            MoviedexState['posistion'] = 0
        key = request.GET.get('key', None)
        if key and key == 'left':
            if MoviedexState['posistion'] > 0:
                MoviedexState['posistion'] -= 1
        elif key and key == 'right':
            if (MoviedexState['posistion'] < len(game.captured_list) - 1):
                MoviedexState['posistion'] += 1
        if key and key == 'a':
            if len(game.captured_list):
                moviemon_id=get_moviemon_token(game.captured_list[MoviedexState['posistion']])
                return redirect('moviedex_detail', moviemon_id=moviemon_id)
        elif key and key == 'select':
            return redirect('worldmap')

        self.context['movies'] = []
        if MoviedexState['posistion'] > 0:
            id = game.captured_list[MoviedexState['posistion'] - 1]
            self.context['movies'].append({
                'poster': game.moviemon[id].poster,
                'class': 'moviedex-blur'
            })
        if len(game.captured_list) > 0:
            id = game.captured_list[MoviedexState['posistion']]
            self.context['movies'].append({
                'poster': game.moviemon[id].poster,
                'class': 'moviedex-ative '
            })
        if MoviedexState['posistion'] + 1 < len(game.captured_list):
            id = game.captured_list[MoviedexState['posistion'] + 1]
            self.context['movies'].append({
                'poster': game.moviemon[id].poster,
                'class': 'moviedex-blur'
            })
        return render(request, self.template_name, self.context)
