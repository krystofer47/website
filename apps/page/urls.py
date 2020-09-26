from django.urls import path

from . import views

app_name = 'page'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:page>/', views.HomeView.as_view(), name='page'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('privacy/', views.PrivacyView.as_view(), name='privacy'),
]
