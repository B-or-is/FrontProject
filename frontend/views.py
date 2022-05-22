import json
import urllib.request
import random

from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView, DateDetailView,
                                  WeekArchiveView, DeleteView, CreateView, UpdateView, FormView)
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User

from .forms import LoginForm, SignUpForm

#
# def front(request):
#     print('front')
#     return render(request, 'frontend/main/front.html')

# class Index(TemplateView):
#     template_name = 'index.html'
    # template_name = 'frontend/main/index_front.html'


url = urllib.request.urlopen("https://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
words = json.loads(url.read())


class BootstrapExample(TemplateView):
    template_name = 'frontend/main/front.html'

    # заполнение словаря, отправляющего переменные на фронтенд (список из 10 рандомных слов с адреса выше)
    def get_context_data(self, **kwargs):
        return {'some_data': [random.choice(words)
                              for i in range(10)]}


class Report(TemplateView):
    template_name = 'main/../FrontProject/templates/main/report.html'


class LoginExample(LoginView):
    pass


class ListExample(ListView):
    template_name = 'frontend/accounts/profile.html'
    queryset = User.objects.all()
    context_object_name = "users"


class DetailViewExample(DetailView):
    template_name = 'frontend/detail.html'
    model = User


class DateDetailViewExample(DateDetailView):
    template_name = 'frontend/date_detail.html'
    model = User
    date_field = "date_joined"


# Example http://127.0.0.1:8000/detail-date/2020/feb/24/2


class WeekArchiveViewExample(WeekArchiveView):
    template_name = 'frontend/week_archive.html'
    year = 2020
    model = User
    date_field = "date_joined"
    context_object_name = "week_users_archive"
#     http://127.0.0.1:8000/detail-date/2020/feb/24/2


class CreateViewExample(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = '/'


class UpdateExample(UpdateView):
    model = User
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = '/'


class DeleteExample(DeleteView):
    model = User
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = '/'
