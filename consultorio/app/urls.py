from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name='login'),
    path("create_doc", views.create_doc, name='create_doc'),
]