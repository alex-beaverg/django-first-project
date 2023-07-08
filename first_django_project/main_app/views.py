from django.shortcuts import render


def index(request):
    data = {
        'title': 'Main Page',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'main_app/index.html', data)


def about(request):
    return render(request, 'main_app/about.html')


def rules(request):
    return render(request, 'main_app/rules.html')