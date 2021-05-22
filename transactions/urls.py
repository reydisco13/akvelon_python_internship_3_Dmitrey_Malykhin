from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'transaction'
urlpatterns = [
    path('transaction/create', TransactionCreateView.as_view()),
    path('transaction/all/', TransactionListView.as_view()),
    path('transaction/all/<int:pk>/', TransactionListView.as_view()),
    path('transaction/detail/<int:pk>/', TransactionDetailView.as_view()),


]
