from django.shortcuts import render


def index(request):
    data = {
        "title": "Test application",
        "user_name": "Mikhail",
        "array": [(i, i ** 2) for i in range(50)],
    }
    return render(request, 'testapp/index.html', data)
