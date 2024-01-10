from .views import TeamViewSet, PersonViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'persons', PersonViewSet, basename='person')

urlpatterns = [
    path('', include(router.urls)),
]
