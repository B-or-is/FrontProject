import json
import urllib.request
import random

from django.shortcuts import render
from django.views.generic import TemplateView


url = urllib.request.urlopen("https://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
words = json.loads(url.read())


class Index(TemplateView):
    template_name = 'main/index.html'

    # заполнение словаря, отправляющего переменные на фронтенд (список из 10 рандомных слов с адреса выше)
    def get_context_data(self, **kwargs):
        return {'some_data': [random.choice(words)
                              for i in range(10)]}

