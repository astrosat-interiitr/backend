from rest_framework.routers import SimpleRouter
from astrosat import views


router = SimpleRouter()

router.register(r'satellite', views.SatelliteViewSet, 'Satellite')
router.register(r'cosmicsource', views.CosmicSourceViewSet, 'CosmicSource')
router.register(r'publication', views.PublicationViewSet, 'Publication')

urlpatterns = router.urls
