from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from moviemon.utils.game import load_slot, load_slot_info

optionState = {
    'slot': 0,
    'isLoad': False,
}

class Load(TemplateView):
    template_name = "load.html"
    context = {
        "btnA": "Load"
    }

    def get(self, request):
        key = request.GET.get('key', None)
        if key and key == 'up':
            optionState['isLoad'] = False
            optionState['slot'] -= 1 if optionState['slot'] > 0 else 0
        elif key and key == 'down':
            optionState['isLoad'] = False
            optionState['slot'] += 1 if optionState['slot'] < 2 else 0
        if key and key == 'a':
            if optionState['isLoad'] == True:
                optionState['isLoad'] = False
                return redirect('worldmap')
            elif load_slot(('A', 'B', 'C')[optionState['slot']]):
                optionState['isLoad'] = True
        elif key and key == 'b':
            return redirect('title')
        slots = load_slot_info()
        score = 'Free' if slots.get('A', None) is None else slots.get('A').get('score', 'Free')
        self.context['A'] = "Slot 🅰 : {}".format(score)
        score = 'Free' if slots.get('B', None) is None else slots.get('B').get('score', 'Free')
        self.context['B'] = "Slot 🅱 : {}".format(score)
        score = 'Free' if slots.get('C', None) is None else slots.get('C').get('score', 'Free')
        self.context['C'] = "Slot 🅲 : {}".format(score)
        self.context['active'] = optionState['slot']
        self.context['btnA'] = 'Load'
        if optionState['isLoad'] == True:
            self.context['btnA'] = 'Start game'
        return render(request, self.template_name, self.context)
