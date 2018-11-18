from rest_framework import routers
from .Categoryy.views  import CategoryViewSet
from .todo.views import TodoViewSet

router = routers.SimpleRouter()
router.register(r'category',CategoryViewSet)
router.register(r'todos', TodoViewSet)
urlpatterns = router.urls
