from rest_framework import serializers
from tarefas.models import *



class SodaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Soda
        fields = '__all__'
