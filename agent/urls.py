from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
app_name = 'agent'
urlpatterns = [
    path('agent/create', AgentCreateView.as_view()),
    path('agent/all', AgentListView.as_view()),
    path('agent/detail/<int:pk>/', AgentDetailView.as_view()),
]
