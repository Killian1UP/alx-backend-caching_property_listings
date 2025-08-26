from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['property_id', 'title', 'description', 'price', 'location', 'created_at']
        read_only_fields = ['property_id', 'created_at']
        
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value
