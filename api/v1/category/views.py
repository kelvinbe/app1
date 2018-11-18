from category.models import Categories
from rest_framework import viewsets
from .category import CategorySerializer

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
