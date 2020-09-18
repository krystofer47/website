from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('<str:user>/', views.ProfilView.as_view(), name="profile")
]
