from rest_framework.routers import SimpleRouter
from astrosat import views
from django.urls import path, include


router = SimpleRouter()

router.register(r'satellite', views.SatelliteViewSet, 'Satellite')
router.register(r'cosmicsource', views.CosmicSourceViewSet, 'CosmicSource')
router.register(r'astrosat', views.CosmicSourceViewSet, 'Astrosat')

urlpatterns = router.urls


urlpatterns += [
    path("publication", views.PublicationListView.as_view()),
    path("publication/<pk>", views.PublicationGetView.as_view()),
    path('generate', views.GeneratePdf),
    path("health-check", views.HealthCheck.as_view()),
]
