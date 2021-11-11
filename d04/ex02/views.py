from django.shortcuts import render
from datetime import datetime
from django.conf import settings
from django.http import HttpResponseRedirect
from .forms import StrForm

def get_logs():
	try:
		with open(settings.LOGFILE, 'r') as fd:
			data_logs = fd.readlines()
			return data_logs
	except IOError as e:
		return []
		
def write_log(content):
	date = datetime.now()
	with open(settings.LOGFILE, 'a+') as fd:
		fd.write("%s: %s\n" % (date.strftime("%b %d %Y %H:%M:%S"), content))

def index(request):
    form = StrForm()
    return render(request, 'ex02/index.html', {
        'form': form,
		'history': get_logs(),
		'stylesheet': 'ex02/style.css'
		})

def post(request):
	if request.method == 'POST':
		write_log(request.POST.get('your_note'))
		return HttpResponseRedirect('/ex02')
