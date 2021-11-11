from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class Option(TemplateView):
    template_name = "option.html"
    context = {}

    def get(self, request):
        key = request.GET.get('key', None)
        if key and key == 'a':
            return redirect('save_game')
        elif key and key == 'b':
            return redirect('title')
        elif key and key == 'start':
            return redirect('worldmap')
        return render(request, self.template_name, self.context)
