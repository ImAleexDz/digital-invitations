from rest_framework import routers
from .api import FamilyViewSet, ConfirmationViewSet

router = routers.DefaultRouter()

router.register('api/family', FamilyViewSet, 'family')

router.register('api/confirmations', ConfirmationViewSet, 'confirmations')

urlpatterns = router.urls