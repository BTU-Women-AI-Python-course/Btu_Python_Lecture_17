from rest_framework import routers

from blogs.views import BlogViewSet

router = routers.SimpleRouter()
router.register('', BlogViewSet)
urlpatterns = router.urls
