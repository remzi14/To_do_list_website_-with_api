from .models import Do
from rest_framework import serializers



class DoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Do
        fields='__all__'











