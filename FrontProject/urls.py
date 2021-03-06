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
from django.urls import re_path

# для GraphQL
from django.views.decorators.csrf import csrf_exempt
# from graphene_django.views import GraphQLView
# from .schema import schema
from .views import Index, url
from graph_app.views import plug_graphql
from frontend.views import Report, LoginExample, \
    ListExample, DetailViewExample, DateDetailViewExample, \
    WeekArchiveViewExample, DeleteExample, CreateViewExample, UpdateExample

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('detail-date/<int:year>/<month>/<int:day>/<int:pk>/', DateDetailViewExample.as_view(), name='detail_date'),
    # Example: /week-archive/2022/week/22/
    path('week-archive/<int:year>/week/<int:week>/', WeekArchiveViewExample.as_view(), name="week_archive"),
    path('create/', CreateViewExample.as_view(), name='create'),
    path('update/<pk>/', UpdateExample.as_view(), name='update'),
    path('delete/<pk>/', DeleteExample.as_view(), name='delete'),
    path('login-user/', LoginExample.as_view(), name='login_user'),
    path('frontend/', include('frontend.urls')),
    path('template/', include('jinja_app.urls')),
    path('email/', include('send_email.urls')),
    path('reset/', include('reset_password_app.urls')),
    # re_path(r'^graphql', csrf_exempt(GraphQLView.as_view(graphiql=True)), name='test_graphql'),
    re_path(r'^graphql', plug_graphql, name='plug_graphql'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
