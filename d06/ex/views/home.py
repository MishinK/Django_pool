
from django import db
from django.views import View
from django.shortcuts import render
from ..forms import TipForm, DeleteTipForm, VoteForm
from ..models import TipModel


class Home(View):
    template_name = "ex/base.html"

    def get(self, request):
        try:
            tips = TipModel.objects.all().order_by('-date')

        except db.DatabaseError:
            tips = []
        context = {
            'tipform': TipForm(),
            'tips': [{
                'id': tip.id,
                'content': tip.content,
                'author': tip.author,
                'date': tip.date,
                'up_votes': tip.up_votes,
                'down_votes': tip.down_votes,
                'deleteform': DeleteTipForm(tip.id),
                'voteform': VoteForm(tip.id),
            } for tip in tips],
        }
        return render(request, self.template_name, context)