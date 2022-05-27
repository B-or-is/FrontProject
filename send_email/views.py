from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse

from .token_generator import account_activation_token
from .forms import ContactForm, UserSignUpForm

from django.views.generic import TemplateView
from django.template import RequestContext
from django.forms import ModelForm

# def homepage(request):
#     return render(request, "send_email/home.html")


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Пробное сообщение"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            # объединяем body в один текст с разбиением построчно значений ключей словаря
            message = "\n".join(body.values())
            try:
                send_mail(subject, message,
                          'admin@example.com',
                          ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect("index")       # перенаправление на главную страницу

    form = ContactForm()
    return render(request, "send_email/contact.html", {'form': form})


# регистрация пользователя
def usersignup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            email_subject = 'Activate Your Account'
            message = render_to_string('send_email/activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            return HttpResponse(
                'We have sent you an email, please confirm your email address to complete registration')
    else:
        form = UserSignUpForm()
    return render(request, 'send_email/signup.html', {'form': form})


# проверка токена и активация пользователя
def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)            # активация пользователя
        return HttpResponse('Your account has been activate successfully')
    else:
        return HttpResponse('Activation link is invalid!')


######
# test
######
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

#######################################
# если требуется положить письмо в базу
#######################################
# class ContactUsForm(ModelForm):
#     class Meta:
#         model = MailBox
#         fields = ['subject', 'message', 'sender' ]
#
#
# def contact_us(request):
#     path_back = request.META.get('HTTP_REFERER','/')
#
#     if request.method == 'POST': # If the form has been submitted...
#         contact_form = ContactUsForm(request.POST) # A form bound to the POST data
#         if contact_form.is_valid(): # All validation rules pass
#             subject = contact_form.cleaned_data['subject']
#             sender = contact_form.cleaned_data['sender']
#             message = 'Письмо было отправлено с сайта, адрес для ответа %s \r\n \r\n' %sender
#             message += contact_form.cleaned_data['message']
#             #recipients = ['Bureau@smolgu.ru']
#             recipients = ['skymorr@yandex.ru']
#
#             # Положим копию письма в базу на всякий случай
#             # MailBox.objects.create(subject=subject, sender=sender, message=message)
#
#             # и отправим его
#             try:
#                 send_mail(subject, message, sender, recipients, fail_silently=False)
#             except:
#                 send_mail(subject, message, sender, recipients, fail_silently=False)
#
#             return render('web_site/success.html', {'path_back': path_back}, context_instance=RequestContext(request))
#
#     return render('web_site/fail.html', context_instance=RequestContext(request))
