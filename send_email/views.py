from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import TemplateView


# class MyTemplateView(TemplateView):
#     template_name = 'hello_email.html'
#
#     def get(self, request):
#
#         send_mail('Subject', 'some_text',
#                   'from@bbb.com', ['to@bbb.com'],
#                   fail_silently=True)   # при ошибке продолжить выполнение
#
#         return render(request, self.template_name)
