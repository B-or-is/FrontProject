from django.urls import path, include
from frontend.views import BootstrapExample, LoginExample, ListExample, Report, DetailViewExample

urlpatterns = [
    path('front/', BootstrapExample.as_view(), name='front'),
    path('login/', LoginExample.as_view(), name='login'),
    path('accounts/profile/', ListExample.as_view(), name='all_users'),
    path('detail/<int:pk>/', DetailViewExample.as_view(), name='detail'),
    path('report/', Report.as_view(), name='report'),
]
