# проверка подключения обоих templates (Django и Jinja)
from django.shortcuts import render


def jinja_test(request):
    # print("It's Jinja template")
    return render(request, 'index_django.html',
                  context={'user_data': {'name': 'First'},
                           'user_info': {'key1': 'value1',
                                         'key2': 'value2'}},
                  using='my_backend')


def django_test(request):
    print("It's Django template")
    return render(request, 'index_django.html',
                  context={'user_data': [{'name': 'First'},
                                         {'name': 'Second'}]})
