from django.core.mail import send_mail
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import TemplateView
from django.forms import ModelForm

# class SendTemplateView(TemplateView):
#     template_name = 'send_email/hello_email.html'
#
#     def get(self, request):
#
#         send_mail('Subject', 'some_text',
#                   'from@bbb.com', ['to@bbb.com'],
#                   fail_silently=True)                   # при ошибке продолжить выполнение
#
#         return render(request, self.template_name)


# если требуется положить письмо в базу
class ContactUsForm(ModelForm):
    class Meta:
        # model = MailBox
        fields = ['subject', 'message', 'sender' ]


def contact_us(request):
    path_back = request.META.get('HTTP_REFERER','/')

    if request.method == 'POST': # If the form has been submitted...
        contact_form = ContactUsForm(request.POST) # A form bound to the POST data
        if contact_form.is_valid(): # All validation rules pass
            subject = contact_form.cleaned_data['subject']
            sender = contact_form.cleaned_data['sender']
            message = 'Письмо было отправлено с сайта, адрес для ответа %s \r\n \r\n' %sender
            message += contact_form.cleaned_data['message']
            #recipients = ['Bureau@smolgu.ru']
            recipients = ['skymorr@yandex.ru']

            # Положим копию письма в базу на всякий случай
            # MailBox.objects.create(subject=subject, sender=sender, message=message)

            # и отправим его
            try:
                send_mail(subject, message, sender, recipients, fail_silently=False)
            except:
                send_mail(subject, message, sender, recipients, fail_silently=False)

            return render('web_site/success.html', {'path_back': path_back}, context_instance=RequestContext(request))

    return render('web_site/fail.html', context_instance=RequestContext(request))