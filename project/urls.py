from rest_framework import routers
from .api import FamilyViewSet, ConfirmationViewSet, Bf_FamilyViewSet, FriendsViewSet

router = routers.DefaultRouter()

router.register('api/family/gf', FamilyViewSet, 'family')
router.register('api/family/bf', Bf_FamilyViewSet, 'bf_family')
router.register('api/friends', FriendsViewSet, 'friends')

router.register('api/confirmations', ConfirmationViewSet, 'confirmations')

urlpatterns = router.urls