from rest_framework import serializers
from .models import Things

class ThingsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','author','title','body','created_at')
        model = Things