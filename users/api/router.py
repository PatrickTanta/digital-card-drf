from django.urls import path
from rest_framework.routers import DefaultRouter
from users.api.views import UserApiViewSet, UserDetailView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

router_user = DefaultRouter()
router_user.register(r'users', UserApiViewSet, basename='users')

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/me/', UserDetailView.as_view(), name='user-detail')
]