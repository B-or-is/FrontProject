from django.contrib import admin
from django.urls import path, include

from FrontProject.views import Index
from frontend.views import BootstrapExample

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', Index.as_view(), name='index-front'),
    path('front/', BootstrapExample.as_view(), name='front'),
    # path('', include('jinja_app.urls'))
]
