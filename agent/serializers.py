from rest_framework import serializers
from .models import *


class AgentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'


class AgentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'


