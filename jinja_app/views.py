# проверка подключения обоих templates (Django и Jinja)
from django.shortcuts import render


def jinja_test(request):
    print("It's Jinja template")
    return render(request, 'index_jinja.html',
                  context={'user_data': {'name': 'Jinja Template (my work)!'},
                           'user_info': {'key1': 'value1',
                                         'key2': 'value2'}},
                  using='my_backend')

    # {'user_data': {'name': 'Jinja Template (my work)!'},
    # 'user_info': {'key1': 'value1', 'key2': 'value2'},
    # 'request': <WSGIRequest: GET '/template/jinja2/'>,
    # 'my_template': 'this is custom'}


def django_test(request):
    print("It's Django template")
    return render(request, 'index_django.html',
                  context={'user_data': [{'name': 'First'},
                                         {'name': 'Second'}]})
    # return render(request, 'index_django.html',
    #               context={'user_data': {'name': 'template'}})
