from django.shortcuts import render

def django(request):
    return render(request, 'ex01/content.html', {
        'title': 'Ex01: Django, framework web.',
        'stylesheet': 'ex01/style1.css',
        'iframe_src': 'https://ru.wikipedia.org/wiki/Django'}
    )

def display(request):
    return render(request, 'ex01/content.html', {
        'title': 'Ex01: Display process of a static page.',
        'stylesheet': 'ex01/style1.css',
        'iframe_src': 'https://ru.wikipedia.org/wiki/Статический_сайт'}
    )

def templates(request):
    return render(request, 'ex01/content.html', {
        'title': 'Ex01: Template engine.',
        'stylesheet': 'ex01/style2.css',
        'iframe_src': 'https://www.youtube.com/embed/M01sApK6yS4'}
    )