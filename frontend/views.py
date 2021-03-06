import json
import urllib.request
import random

from django.views.generic import (TemplateView, ListView, DetailView, DateDetailView,
                                  WeekArchiveView, DeleteView, CreateView, UpdateView, FormView)
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User

from .forms import LoginForm, SignUpForm


url = urllib.request.urlopen("https://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
words = json.loads(url.read())


class BootstrapExample(TemplateView):
    template_name = 'frontend/main/front.html'

    # заполнение словаря, отправляющего переменные на фронтенд (список из 10 рандомных слов с адреса выше)
    def get_context_data(self, **kwargs):
        return {'some_data': [random.choice(words)
                              for i in range(10)]}


class Report(TemplateView):
    template_name = 'frontend/main/report.html'


class LoginExample(LoginView):
    template_name = 'frontend/registration/login.html'


class ListExample(ListView):
    template_name = 'frontend/accounts/profile.html'
    queryset = User.objects.all()
    # print(queryset)
    context_object_name = "users"


class DetailViewExample(DetailView):
    template_name = 'frontend/accounts/detail.html'
    model = User


# Example http://127.0.0.1:8000/detail-date/2022/may/23/2
class DateDetailViewExample(DateDetailView):
    template_name = 'frontend/date_detail.html'
    model = User
    date_field = "date_joined"


# Example http://127.0.0.1:8000/week-archive/2022/week/21
class WeekArchiveViewExample(WeekArchiveView):     # показывает все объекты за определенную неделю
    template_name = 'frontend/week_archive.html'
    model = User
    date_field = "date_joined"
    context_object_name = "week_users_archive"  # контекст для цикла в html

    queryset = User.objects.all()
    week_format = "%W"                  # неделя начинается в понедельник
    allow_future = True                 # отображаются объекты с датой в будущем


class CreateViewExample(CreateView):
    form_class = SignUpForm
    template_name = 'frontend/signup.html'
    success_url = '/'


# Example http://127.0.0.1:8000/update/<pk>
class UpdateExample(UpdateView):
    model = User
    form_class = SignUpForm
    template_name = 'frontend/signup.html'
    success_url = '/'


# http://127.0.0.1:8000/delete/<pk>
class DeleteExample(DeleteView):
    model = User
    form_class = SignUpForm
    template_name = 'frontend/signup.html'
    success_url = '/'


