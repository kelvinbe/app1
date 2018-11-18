from category.models import Categories
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ('id', 'name')
