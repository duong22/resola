from .views import BookViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'book', BookViewSet, basename='Book')

urlpatterns = router.urls