from django.shortcuts import render
from rest_framework import generics
from .serializers import AgentDetailSerializer, AgentListSerializer
from .models import Agent
from rest_framework_swagger.views import get_swagger_view
# Create your views here.

schema_view = get_swagger_view(title='Pastebin API')
print(schema_view)

class AgentCreateView(generics.CreateAPIView):
    serializer_class = AgentDetailSerializer


class AgentListView(generics.ListAPIView):
    serializer_class = AgentListSerializer
    queryset = Agent.objects.all()


class AgentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AgentDetailSerializer
    queryset = Agent.objects.all()



