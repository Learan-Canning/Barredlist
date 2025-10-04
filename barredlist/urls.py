from . import views
from django.urls import path

urlpatterns = [
    path('barredlist/', views.PostList.as_view(), name='home'),
]