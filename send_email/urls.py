from django.contrib import auth
from django.urls import path, include
# from send_email.views import SendTemplateView
from .views import contact, usersignup, activate_account

urlpatterns = [
    path('', contact, name='email'),
    # path('logout/', auth.LogoutView.as_view(template_name='index.html'), name='logout'),
    path(r'signup/', usersignup, name='register_user'),                         # вход
    # это адрес (линк), который приходит в почту после регистрации
    path(r'activate/<uidb64>/<token>/', activate_account, name='activate'),   # активация аккаунта
    # path("subscription/", subscription, name="subscription"),
]

# urlpatterns = [
#     path('test-email/', MyTemplateView.as_view(), 'email_template'),
# ]

#          name='logout'),
# from .views import usersignup, activate_account, subscription
# from django.contrib.auth import views as auth
#
# urlpatterns = [
#     path('logout/', auth.LogoutView.as_view(template_name='index.html'),
#          name='logout'),
#     path(r'signup/', usersignup, name='register_user'),
#     path(
#         r'activate/<uidb64>/<token>/',
#         activate_account, name='activate'),
#     path("subscription/", subscription, name="subscription"),
# ]
