from rest_framework import routers

from .category.views import CategoriesViewSet
from .todo.views import TodolistViewSet

router = routers.SimpleRouter()
router.register(r'category',CategoriesViewSet)
router.register(r'todo', TodolistViewSet)
urlpatterns = router.urls