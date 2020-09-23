from django.urls import path

from . import views

app_name = 'page'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:page>', views.HomeView.as_view(), name='page')
]
