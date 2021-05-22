from django.db import models

from django_filters import rest_framework as filters
from agent.models import Agent
class Cart:
    Agent = models.ManyToManyField(Agent)

# Create your models here.

class Transaction(models.Model):
    id = models.CharField(verbose_name='id', db_index=True, primary_key=True, max_length=64, unique=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()


class AgentFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class AgentFilter(filters.FilterSet):
    agent = AgentFilterInFilter(field_name='agent_id', lookup_expr='in')

    class Meta:
        model = Transaction
        fields = ['agent']


