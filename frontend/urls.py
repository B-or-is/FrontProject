from django.contrib import admin
from django.urls import path, include

from FrontProject.views import Index
from frontend.views import BootstrapExample, LoginExample, ListExample, Report, DetailViewExample

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', Index.as_view(), name='index-front'),
    path('front/', BootstrapExample.as_view(), name='front'),
    path('login/', LoginExample.as_view(), name='login'),
    path('accounts/profile/', ListExample.as_view(), name='all_users'),
    path('detail/<int:pk>/', DetailViewExample.as_view(), name='detail'),
    path('report/', Report.as_view(), name='report'),
    # path('', include('jinja_app.urls'))
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
