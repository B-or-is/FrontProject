"""FrontProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import Index
from frontend.views import Report, LoginExample, \
    ListExample, DetailViewExample, DateDetailViewExample, \
    WeekArchiveViewExample, DeleteExample, CreateViewExample, UpdateExample

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('report/', Report.as_view(), name='report'),
    path('login/', LoginExample.as_view(), name='login'),
    path('accounts/profile/', ListExample.as_view(), name='all_user'),
    path('detail/<pk>/', DetailViewExample.as_view(), name='detail'),
    path('detail-date/<year>/<month>/<day>/<pk>',
         DateDetailViewExample.as_view(), name='detail_date'),
    path('week-archive/<week>/', WeekArchiveViewExample.as_view(), name='week_archive'),
    path('create/', CreateViewExample.as_view(), name='create'),
    path('delete/<pk>/', DeleteExample.as_view(), name='delete'),
    path('update/<pk>/', UpdateExample.as_view(), name='update'),
    path('frontend/', include('frontend.urls')),
    path('template/', include('jinja_app.urls')),
    # path('mail', include('send_email.urls')),
    # path('', include('reset_password_app.urls'))
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
