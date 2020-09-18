from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail')
]
