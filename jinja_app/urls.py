from django.urls import path

from jinja_app import views

urlpatterns = [
    path('jinja2/', views.jinja_test, name='jinja2'),
    path('django/', views.django_test, name='django'),
]






