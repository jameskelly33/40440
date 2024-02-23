from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('details/<int:goal_id>',views.details, name='details')
]