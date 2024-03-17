from django.urls import path
from . import views
urlpatterns = [
    path('hello/', views.sayhello),
    path('create/', views.create_my_model),
]
