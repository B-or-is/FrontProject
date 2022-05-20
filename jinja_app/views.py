# проверка подключения обоих templates (Django и Jinja)
from django.shortcuts import render


def jinja_test(request):
    print("It's Jinja template")
    return render(request, 'jinja_app/index_jinja.html',
                  context={'user_data': [{'name': 'Иванов'},
                                         {'name': 'Сидоров'}],
                           'user_info': {'key1': 'value1',
                                         'key2': 'value2'}},
                  using='jinja2')
                  # using='my_backend')


def django_test(request):
    print("It's Django template")
    return render(request, 'jinja_app/index_django.html',
                  context={'user_data': [{'name': 'Петров'},
                                         {'name': 'Козлов'}]})
    # return render(request, 'index_django.html',
    #               context={'user_data': {'name': 'template'}})
