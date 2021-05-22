from django.shortcuts import render
from rest_framework import generics
from .serializers import TransactionDetailSerializer, TransactionListSerializer
from .models import Transaction, AgentFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class TransactionCreateView(generics.CreateAPIView):
    serializer_class = TransactionDetailSerializer


class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionListSerializer
    queryset = Transaction.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AgentFilter


class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionDetailSerializer
    queryset = Transaction.objects.all()


