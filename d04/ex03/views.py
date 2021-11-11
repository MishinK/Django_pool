from django.shortcuts import render

def table(request):
    return render(request, 'ex03/index.html', {
		'rows': range(5, 255, 5),
		'stylesheet': 'ex03/style.css'
		})