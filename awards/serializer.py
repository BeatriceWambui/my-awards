from rest_framework import serializers
from .models import Project

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title','image','description','link','editor','date')