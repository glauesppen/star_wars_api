from rest_framework import routers
from planet.views import PlanetViewSet

router = routers.SimpleRouter()
router.register(r'planets', PlanetViewSet, 'Planet')

urlpatterns = router.urls